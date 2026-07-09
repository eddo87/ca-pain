# Ricevitore target: legge dalla chat "TARGET <nome> 0x<seriale>" (inviato da
# share_target.py), imposta l'ultimo target, lo annuncia nel giornale (sempre
# visibile) e mostra un banner sopra la testa (se il target e' in vista).
# Avviare come macro normale con Loop OFF: si autoregola.

from Assistant import Engine

MARCATORE     = "TARGET"               # deve combaciare con il mittente
AUTO_ATTACCO  = True                   # mischia: attacca da solo (entro distanza). Maghi: False.
DISTANZA_MAX  = 10                      # 0 = nessun limite; >0 = attacca solo entro N caselle
BANNER_FMT    = ">>> TARGET (%s) <<<"  # %s = nome del target
BANNER_COLORE = 33                     # colore del banner / annuncio
EVIDENZIA_HUE = 1173                   # rehue del target chiamato: teal/aqua (0 = disattivato)
CALLER_HUE    = 53                     # rehue di chi chiama il target: giallo (0 = disattivato)
BANNER_MS     = 2800                  # ogni quanto rinfrescare il banner
SCANSIONE_MS  = 150                   # ogni quanto leggere il giornale

HELP_MARKER   = "HELP ME"              # grido d'aiuto in alliance chat
HELP_INVIA    = True                   # manda HELP ME quando i TUOI hp scendono sotto soglia
HELP_PCT      = 65                     # soglia: percento degli hp massimi
HELP_HUE      = 1166                   # rosa: chi chiede aiuto viene rehue-ato per tutti (0 = off)
HELP_COOLDOWN_MS = 8000                # minimo tra due HELP inviati
HELP_DURATA_MS   = 8000                # rosa: durata massima
HELP_FINE_PCT    = 85                  # rosa: via anche prima, se gli hp risalgono oltre questa %

# solo questi nomi possono chiamare il target (lista vuota = accetta tutti)
CALLER_AMMESSI = ["PASO ADELANTE", "uno"]

ultimo_seriale = 0
ultimo_nome = "?"
caller_seriale = 0
help_seriale = 0
help_ticks = 0
help_cd = 0


def estrai_seriale(testo):
    # ID esadecimale (0x...) o decimale; gestisce anche apici 'nome' 'id'
    parti = testo.split("'")
    if len(parti) >= 3:
        token = parti[-2].strip()
        try:
            if token.lower().startswith("0x"):
                return int(token, 16)
            return int(token)
        except:
            pass
    i = testo.find("0x")
    if i >= 0:
        cifre = ""
        for c in testo[i + 2:]:
            if c in "0123456789abcdefABCDEF":
                cifre += c
            else:
                break
        if cifre:
            return int(cifre, 16)
    return 0


def estrai_nome(testo):
    # nome del target: tutto tra "TARGET" e "0x"  (es: "... TARGET Mad Maniak 0xADBE")
    i = testo.find(MARCATORE)
    if i < 0:
        return ""
    resto = testo[i + len(MARCATORE):]
    j = resto.find("0x")
    if j >= 0:
        resto = resto[:j]
    return resto.replace("'", " ").strip()


def estrai_caller(testo, marcatore=MARCATORE):
    # chi parla, da testo tipo "<Alliance> PASO ADELANTE: TARGET ..." (name=System)
    i = testo.find(marcatore)
    if i <= 0:
        return ""
    prefisso = testo[:i]
    if ">" in prefisso:                  # togli il tag canale <Alliance>/<Guild>
        prefisso = prefisso.split(">", 1)[1]
    prefisso = prefisso.strip()
    if prefisso.endswith(":"):
        prefisso = prefisso[:-1].strip()
    return prefisso


def caller_ammesso(voce, testo):
    # True se l'autore (voce.Name) OPPURE chi parla nel testo e' autorizzato (esatto).
    if not CALLER_AMMESSI:
        return True
    ammessi = [a.strip().lower() for a in CALLER_AMMESSI]
    if voce.Name and voce.Name.strip().lower() in ammessi:
        return True
    c = estrai_caller(testo).strip().lower()
    if c and c in ammessi:
        return True
    return False


def trova_caller_seriale(voce, testo, marcatore=MARCATORE):
    # seriale del caller cercandolo per nome tra le mobile caricate (0 se fuori vista)
    nome = (voce.Name or "").strip()
    if not nome or nome.lower() == "system":
        nome = estrai_caller(testo, marcatore)
    nome = nome.strip().lower()
    if not nome:
        return 0
    try:
        for m in Engine.Mobiles.GetMobiles():
            if m and m.Name and m.Name.strip().lower() == nome:
                return m.Serial
    except:
        pass
    return 0


def parse_target(voce):
    # (seriale, nome) se la voce e' una chiamata TARGET valida, altrimenti (0, "")
    testo = voce.Text
    if not testo or MARCATORE not in testo:
        return 0, ""
    if not caller_ammesso(voce, testo):
        return 0, ""
    s = estrai_seriale(testo)
    if not s:
        return 0, ""
    return s, estrai_nome(testo)


def a_portata(seriale):
    try:
        if not FindObject(seriale):
            return False
        if Dead(seriale):                 # non attaccare un cadavere
            return False
        if DISTANZA_MAX > 0 and Distance(seriale) > DISTANZA_MAX:
            return False
        return True
    except:
        return False


def mostra_banner(seriale, nome):
    HeadMsg(BANNER_FMT % nome, seriale, BANNER_COLORE)


banner_ogni = max(1, BANNER_MS // SCANSIONE_MS)
contatore = 0
annunciato = False

# i maghi non attaccano in mischia come i guerrieri: con Magery > 99 disattivo l'auto-attacco
if Skill("Magery") > 99:
    AUTO_ATTACCO = False

# lettura incrementale del giornale con chiave dedicata: Read(key) consuma SOLO le
# righe nuove (l'offset per-chiave e' quello che Clear sposta — GetEntireBuffer lo ignora).
# Cosi': niente target vecchi all'avvio, e una RI-chiamata dello stesso serial ri-fira
# (il dedupe per serial non la vedrebbe mai).
BUFFER_KEY = "focus_receiver"
Engine.Journal.Clear(BUFFER_KEY)   # salta tutto lo storico: da qui in poi solo righe nuove

while True:
    # consuma tutte le righe arrivate dall'ultima scansione
    # HeadMsg('SCRIPT AGGIORNATO', 'self', 35)
    while True:
        ok, voce = Engine.Journal.Read(BUFFER_KEY)   # IronPython: out param -> tupla
        if not ok or voce is None:
            break
        # grido d'aiuto: rehue ROSA chi lo manda (per tutti quelli che girano il receiver)
        testo_v = voce.Text or ""
        if HELP_HUE and HELP_MARKER in testo_v:
            try:
                hs = trova_caller_seriale(voce, testo_v, HELP_MARKER)
                if hs:
                    if help_seriale and help_seriale != hs:
                        Rehue(help_seriale, 0)
                    Rehue(hs, HELP_HUE)
                    help_seriale = hs
                    help_ticks = max(1, HELP_DURATA_MS // SCANSIONE_MS)
                    SysMessage(">>> HELP <<<", HELP_HUE)
            except:
                pass
            continue

        seriale, nome = parse_target(voce)
        if not seriale:
            continue

        # nuova chiamata (anche stesso serial: ri-punta cursore e last target)
        # evidenzia il nuovo target col rehue e ripulisce il precedente
        if EVIDENZIA_HUE:
            try:
                if ultimo_seriale and ultimo_seriale != seriale:
                    Rehue(ultimo_seriale, 0)
                Rehue(seriale, EVIDENZIA_HUE)
            except:
                pass
        # evidenzia anche il caller (se in vista), ripulendo l'eventuale caller precedente
        if CALLER_HUE:
            try:
                cs = trova_caller_seriale(voce, voce.Text)
                if cs and cs != caller_seriale:
                    if caller_seriale:
                        Rehue(caller_seriale, 0)
                    Rehue(cs, CALLER_HUE)
                    caller_seriale = cs
            except:
                pass
        ultimo_seriale = seriale
        ultimo_nome = nome or "?"
        annunciato = True
        # imposta direttamente il last target: funziona anche se il bersaglio e' fuori vista /
        # non caricato nel client. SetLastTarget() invece richiede la mobile gia' nota
        # (Engine.Mobiles.GetMobile) e fallisce per i maghi che chiamano target lontani.
        Engine.Player.LastTargetSerial = seriale
        # se la mobile e' caricata, SetLastTarget sincronizza anche il CLIENT
        # (ChangeCombatant): serve alle macro last-target/cast del client, non solo a CA
        try:
            if FindObject(seriale):
                SetLastTarget(seriale)
        except:
            pass
        # se c'e' gia' un cursore da spell aperto, riempilo col target ricevuto (utile ai maghi)
        try:
            if TargetExists():
                Pause(50)
                Target(seriale)
        except:
            pass
        SysMessage(">>> TARGET: %s <<<" % ultimo_nome)   # SEMPRE visibile (anche off-screen)
        mostra_banner(seriale, ultimo_nome)              # overhead solo se il target e' in vista
        contatore = 0
        if AUTO_ATTACCO and a_portata(seriale):
            Attack(seriale)

    # HP bassi? grida aiuto in alliance (percentuale: vale per qualsiasi build)
    if HELP_INVIA:
        if help_cd > 0:
            help_cd -= 1
        else:
            try:
                if not Dead("self") and MaxHits("self") > 0 and \
                        Hits("self") * 100 < MaxHits("self") * HELP_PCT:
                    AllyMsg(HELP_MARKER)
                    help_cd = max(1, HELP_COOLDOWN_MS // SCANSIONE_MS)
            except:
                pass

    # togli il rosa quando gli hp risalgono oltre HELP_FINE_PCT, o comunque a durata scaduta
    if help_seriale:
        help_ticks -= 1
        guarito = False
        try:
            # Hits/MaxHits funzionano anche sugli altri (fuori party sono scalati 0-25,
            # ma il rapporto percentuale resta valido); serve la mobile in vista
            if FindObject(help_seriale) and MaxHits(help_seriale) > 0 and \
                    Hits(help_seriale) * 100 > MaxHits(help_seriale) * HELP_FINE_PCT:
                guarito = True
        except:
            pass
        if guarito or help_ticks <= 0:
            try:
                Rehue(help_seriale, 0)
            except:
                pass
            help_seriale = 0

    # rinfresca il banner sopra la testa (solo dopo un annuncio reale, solo se in vista)
    if annunciato:
        contatore += 1
        if contatore >= banner_ogni:
            contatore = 0
            if FindObject(ultimo_seriale):
                mostra_banner(ultimo_seriale, ultimo_nome)

    Pause(SCANSIONE_MS)

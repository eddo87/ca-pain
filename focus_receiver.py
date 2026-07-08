# Ricevitore target: legge dalla chat "TARGET <nome> 0x<seriale>" (inviato da
# share_target.py), imposta l'ultimo target, lo annuncia nel giornale (sempre
# visibile) e mostra un banner sopra la testa (se il target e' in vista).
# Avviare come macro normale con Loop OFF: si autoregola.

from Assistant import Engine

MARCATORE     = "TARGET"               # deve combaciare con il mittente
AUTO_ATTACCO  = True                   # mischia: attacca da solo (entro distanza). Maghi: False.
DISTANZA_MAX  = 0                      # 0 = nessun limite; >0 = attacca solo entro N caselle
BANNER_FMT    = ">>> TARGET (%s) <<<"  # %s = nome del target
BANNER_COLORE = 33                     # colore del banner / annuncio
BANNER_MS     = 2800                  # ogni quanto rinfrescare il banner
SCANSIONE_MS  = 150                   # ogni quanto leggere il giornale

# solo questi nomi possono chiamare il target (lista vuota = accetta tutti)
CALLER_AMMESSI = ["PASO ADELANTE", "uno"]

ultimo_seriale = 0
ultimo_nome = "?"


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


def estrai_caller(testo):
    # chi parla, da testo tipo "<Alliance> PASO ADELANTE: TARGET ..." (name=System)
    i = testo.find(MARCATORE)
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


def ultimo_target():
    # (seriale, nome) dell'ultimo TARGET valido da un caller autorizzato
    seriale = 0
    nome = ""
    for voce in Engine.Journal.GetEntireBuffer():
        if voce is None:
            continue
        testo = voce.Text
        if testo and MARCATORE in testo and caller_ammesso(voce, testo):
            s = estrai_seriale(testo)
            if s:
                seriale = s
                nome = estrai_nome(testo)
    return seriale, nome


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

# baseline all'avvio: segna l'ultimo TARGET gia' presente come "gia' visto" e NON agire.
# ClearJournal() NON serve qui: sposta solo un offset di lettura che GetEntireBuffer ignora
# (CircularBuffer.Clear "does not actually clear it"), quindi non nasconde i vecchi TARGET.
ultimo_seriale = ultimo_target()[0]

while True:
    seriale, nome = ultimo_target()

    # nuovo target condiviso
    if seriale and seriale != ultimo_seriale:
        ultimo_seriale = seriale
        ultimo_nome = nome or "?"
        annunciato = True
        # imposta direttamente il last target: funziona anche se il bersaglio e' fuori vista /
        # non caricato nel client. SetLastTarget() invece richiede la mobile gia' nota
        # (Engine.Mobiles.GetMobile) e fallisce per i maghi che chiamano target lontani.
        Engine.Player.LastTargetSerial = seriale
        # se c'e' gia' un cursore da spell aperto, riempilo col target ricevuto (utile ai maghi)
        try:
            if TargetExists():
                Target(seriale)
        except:
            pass
        SysMessage(">>> TARGET: %s <<<" % ultimo_nome)   # SEMPRE visibile (anche off-screen)
        mostra_banner(seriale, ultimo_nome)              # overhead solo se il target e' in vista
        contatore = 0
        if AUTO_ATTACCO and a_portata(seriale):
            Attack(seriale)

    # rinfresca il banner sopra la testa (solo dopo un annuncio reale, solo se in vista)
    if annunciato:
        contatore += 1
        if contatore >= banner_ogni:
            contatore = 0
            if FindObject(ultimo_seriale):
                mostra_banner(ultimo_seriale, ultimo_nome)

    Pause(SCANSIONE_MS)

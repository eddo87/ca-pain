# Ricevitore target: legge dalla chat "TARGET ... 0x<seriale>" (inviato da
# share_target.py), imposta l'ultimo target e mostra un banner sopra la testa.
# Avviare come macro normale con Loop OFF: si autoregola.

from Assistant import Engine

MARCATORE     = "TARGET"               # deve combaciare con il mittente
AUTO_ATTACCO  = True                   # mischia: attacca da solo (entro distanza). Maghi: False.
DISTANZA_MAX  = 0                      # 0 = nessun limite; >0 = attacca solo entro N caselle
BANNER_FMT    = ">>> TARGET (%s) <<<"  # %s = nome del target
BANNER_COLORE = 33                     # colore del banner
BANNER_MS     = 2000                  # ogni quanto rinfrescare il banner
SCANSIONE_MS  = 150                   # ogni quanto leggere il giornale

# solo questi nomi possono chiamare il target (lista vuota = accetta tutti)
CALLER_AMMESSI = ["PASO ADELANTE", "uno"]

ultimo_seriale = 0


def estrai_seriale(testo):
    # formato: "TARGET nome 0xID"  (o con apici 'nome' 'id'); ID esadecimale o decimale
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


def caller_ammesso(voce):
    # True se l'autore della voce e' tra i caller autorizzati (lista vuota = tutti)
    if not CALLER_AMMESSI:
        return True
    nome = voce.Name
    if not nome:
        return False
    nome = nome.strip().lower()
    for c in CALLER_AMMESSI:
        if nome == c.strip().lower():
            return True
    return False


def target_piu_recente():
    # CircularBuffer non e' iterabile, ma GetEntireBuffer() restituisce un array
    seriale = 0
    for voce in Engine.Journal.GetEntireBuffer():
        if voce is None:
            continue
        testo = voce.Text
        if testo and MARCATORE in testo and caller_ammesso(voce):
            seriale = estrai_seriale(testo)
    return seriale


def a_portata(seriale):
    # filtro distanza per l'attacco automatico (il tasto Ultimo Target rispetta gia' il range)
    if DISTANZA_MAX <= 0:
        return True
    try:
        if not FindObject(seriale):
            return False
        d = Distance(seriale)
        return 0 <= d <= DISTANZA_MAX
    except:
        return False


def mostra_banner(seriale):
    nome = Name(seriale)
    if not nome:
        nome = "?"
    HeadMsg(BANNER_FMT % nome, seriale, BANNER_COLORE)


banner_ogni = max(1, BANNER_MS // SCANSIONE_MS)   # ogni quanti giri rinfrescare il banner
contatore = 0

while True:
    seriale = target_piu_recente()

    # nuovo target condiviso
    if seriale and seriale != ultimo_seriale:
        ultimo_seriale = seriale
        SetLastTarget(seriale)         # ognuno preme il PROPRIO tasto "Ultimo Target"
        mostra_banner(seriale)         # banner subito sul nuovo target
        contatore = 0
        if AUTO_ATTACCO and a_portata(seriale):
            Attack(seriale)

    # rinfresca il banner sopra la testa (solo se il target e' in vista)
    if ultimo_seriale:
        contatore += 1
        if contatore >= banner_ogni:
            contatore = 0
            if FindObject(ultimo_seriale):
                mostra_banner(ultimo_seriale)

    Pause(SCANSIONE_MS)

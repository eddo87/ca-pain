# LOADER: scarica ed esegue l'ultima versione di focus_receiver.py da GitHub.
# I giocatori incollano SOLO questo: ad ogni avvio prende lo script aggiornato,
# cosi' non devono piu' aggiornarlo a mano.

from System import DateTime
from System.Net import WebClient, ServicePointManager, SecurityProtocolType

URL = "https://raw.githubusercontent.com/eddo87/ca-pain/refs/heads/main/focus_receiver.py"

code = None
try:
    # GitHub richiede TLS 1.2
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12
    wc = WebClient()
    wc.Headers.Add("Cache-Control", "no-cache")
    # ?cb=... per provare a saltare la cache della CDN
    code = wc.DownloadString(URL + "?cb=" + str(DateTime.Now.Ticks))
except Exception as ex:
    SysMessage("Loader: download fallito - " + str(ex))

if code:
    SysMessage("focus_receiver caricato da GitHub")
    # esegue lo script scaricato nello scope della macro (comandi CA disponibili)
    exec(compile(code, "focus_receiver.py", "exec"))

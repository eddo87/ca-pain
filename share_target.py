# SHARE the currently selected enemy with the party (once per press).
# Select first with target_enemy.py; receivers run focus_receiver.py.

MARKER         = "TARGET"  # must match focus_receiver.py
SHARE_PARTY    = True      # party chat (use while debugging)
SHARE_GUILD    = False     # guild chat
SHARE_ALLIANCE = False     # alliance chat

serial = GetAlias("enemy")

if not serial:
    SysMessage("Nessun bersaglio selezionato")
else:
    name = Name("enemy")
    if not name:
        name = "sconosciuto"

    msg = "%s %s 0x%X" % (MARKER, name, serial)
    SysMessage(msg)                    # local debug
    if SHARE_PARTY:
        PartyMsg(msg)
    if SHARE_GUILD:
        GuildMsg(msg)
    if SHARE_ALLIANCE:
        AllyMsg(msg)

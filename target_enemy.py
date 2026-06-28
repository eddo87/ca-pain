# SELECT a hostile (Murderer/Enemy): cycle to it, name it overhead, set last target.
# Does NOT broadcast - press the share_target hotkey when you've picked the one you want.

NOTORIETY = ['Murderer', 'Enemy']
BODY      = 'Any'        # 'Humanoid' to skip animal pets (may miss gargoyles - test first)
MODE      = 'Next'       # 'Closest' / 'Next' / 'Previous'
NAME_HUE  = 33           # overhead color for the enemy name

got = GetEnemy(NOTORIETY, BODY, MODE)

if not got:
    SysMessage("Nessun bersaglio")
else:
    SetLastTarget("enemy")
    name = Name("enemy")
    if not name:
        name = "sconosciuto"
    HeadMsg(name, "enemy", NAME_HUE)   # name floats over the target's head

from datetime import datetime, timedelta

HeadMsg("Survival Avviato", "self", 68)

# ---------------- CONFIG ----------------
_ProPot = True         # auto-potions

_Str   = 135
_Dex   = 70
_Stam  = 20
_MinHP = 40            # heal pot when MISSING more than this much HP

# ---------------- IDS ------------------
strpot     = 0xf09
dexpot     = 0xf08
healpot    = 0xf0c
curepot    = 0xf07
refreshpot = 0xf0b
eapple     = 0x2fd8

# ------------- COOLDOWNS ---------------
action_delay = timedelta(milliseconds=650)
_BuffPotCD   = timedelta(seconds=150)   # str/dex: ~120s buff + ~30s grace before re-quaff
CD = {
    healpot:    timedelta(seconds=11),
    curepot:    timedelta(seconds=11),
    refreshpot: timedelta(seconds=11),
    strpot:     _BuffPotCD,
    dexpot:     _BuffPotCD,
    eapple:     timedelta(seconds=120),
}

# ---------------- STATE ----------------
last_action = datetime.now() - action_delay
last_use    = {}

# ---------------- HELPERS --------------
def CanAct():
    return datetime.now() >= last_action + action_delay

def PotReady(pid):
    last = last_use.get(pid)
    return last is None or datetime.now() >= last + CD.get(pid, action_delay)

def Have(pid):
    # silent existence check (CountType returns 0 quietly) so we never search
    # for a potion we aren't carrying -> avoids "cannot find object type" spam
    return CountType(pid, "backpack") > 0

def UsePot(pid):
    # find the item anywhere in the pack and use it by serial. UseType only
    # reaches the top level of the backpack and spams "cannot find object type"
    # for potions nested in a sub-pouch; FindType is recursive and silent.
    global last_action
    if not FindType(pid, -1, "backpack"):
        return False
    UseObject("found")
    last_use[pid] = datetime.now()
    last_action   = datetime.now()
    return True

# --------------- POTIONS ---------------
def UsePotions():
    if not CanAct():
        return

    # 1) Mortal (yellow bar) -> enchanted apple
    if YellowHits("self") and Have(eapple) and PotReady(eapple):
        if UsePot(eapple): return

    # 2) cure poison
    if Poisoned("self") and Have(curepot) and PotReady(curepot):
        if UsePot(curepot): return

    # 3) heal (heal pots don't work while yellow-barred / mortal)
    if DiffHits("self") > _MinHP and not YellowHits("self") and Have(healpot) and PotReady(healpot):
        if UsePot(healpot): return

    # 4) refresh stamina
    if Stam("self") < MaxStam("self") - _Stam and Have(refreshpot) and PotReady(refreshpot):
        if UsePot(refreshpot): return

    # 5) stat buffs (cooldown-gated; _BuffPotCD adds the delay after the buff wears off)
    if Str() < _Str and Have(strpot) and PotReady(strpot):
        if UsePot(strpot): return
    if Dex() < _Dex and Have(dexpot) and PotReady(dexpot):
        if UsePot(dexpot): return

# ----------------- LOOP ----------------
while True:
    if _ProPot:
        UsePotions()
    Pause(50)

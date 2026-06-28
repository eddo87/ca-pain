# panic_heal.py - Chivalry warrior panic survival. Single pass: at most one action per run.
# Bind to a hotkey, enable "do not interrupt", and HOLD the key while in trouble.
# Each press does ONE thing (heal / cure / clear debuff / stamina) then exits.
# Cooldowns use CA Timers (persist across runs) because module vars reset every press.

# ---------------- CONFIG ----------------
_MortalHP = 93         # clear Mortal (apple / Remove Curse) only if life below this AND yellow-barred
_HealHP   = 81         # heal pot / Close Wounds if life below this (and not yellow-barred)
_StamMin  = 23         # refresh pot if stamina below this

# ---------------- IDS ------------------
healpot    = 0xf0c
curepot    = 0xf07
refreshpot = 0xf0b
eapple     = 0x2fd8

# spell fallback costs as (min mana, min tithing) - conservative; a spell is only
# attempted if we can pay for it, so we never fire one that just fails.
_CleanseCost     = (10, 10)   # Cleanse by Fire
_CloseWoundsCost = (11, 10)   # Close Wounds
_RemoveCurseCost = (20, 20)   # Remove Curse

# cooldowns (ms) - potion timers only avoid "you must wait" spam; the server still gates.
_CD_heal    = 10000
_CD_cure    = 10000
_CD_refresh = 10000
_CD_apple   = 120000           # enchanted apple has a long real cooldown
_CD_gcd     = 1500             # global spell GCD so one press can't queue a second cast

# curse-type buffs cleared by Remove Curse - exact names from ../Data/BuffIcons.json
_curseBuffs = ["Curse", "Mass Curse", "Clumsy", "Weaken", "FeebleMind", "Strangle", "Corpse Skin"]

# ---------------- TIMER HELPERS --------------
def ready(name, cd):
    return (not TimerExists(name)) or Timer(name) >= cd

def mark(name):
    SetTimer(name, 0)

# ---------------- ITEM HELPERS ---------------
def Have(pid):
    # silent existence check (CountType returns 0 quietly) so we never search for a
    # potion we lack -> avoids "cannot find object type" spam.
    return CountType(pid, "backpack") > 0

def UsePot(pid):
    # FindType is recursive + silent; UseType only reaches the top of the pack and spams.
    if not FindType(pid, -1, "backpack"):
        return False
    UseObject("found")
    return True

# ---------------- SPELL HELPER ---------------
def CastSelf(name, cost):
    mana, tithe = cost
    if not ready("ph_gcd", _CD_gcd):
        return False
    if Mana("self") < mana or TithingPoints() < tithe:
        return False
    Cast(name, "self")
    mark("ph_gcd")
    return True

def Cursed():
    for b in _curseBuffs:
        if BuffExists(b):
            return True
    return False

# --------------- PANIC (one action, most lethal first) ----------------
yellow = YellowHits("self")
hp     = Hits("self")

# 1) Mortal / yellow bar -> enchanted apple; if apple missing or on cooldown, Remove Curse.
#    Nothing else can heal while yellow-barred, so clearing this comes first.
if yellow and hp < _MortalHP:
    if Have(eapple) and ready("ph_apple", _CD_apple):
        if UsePot(eapple):
            mark("ph_apple")
    else:
        CastSelf("Remove Curse", _RemoveCurseCost)

# 2) poison -> cure potion; fallback Cleanse by Fire.
elif Poisoned("self"):
    if Have(curepot) and ready("ph_cure", _CD_cure):
        if UsePot(curepot):
            mark("ph_cure")
    else:
        CastSelf("Cleanse by Fire", _CleanseCost)

# 3) heal -> heal potion; fallback Close Wounds. (Both blocked while yellow-barred,
#    which branch 1 already handles, so this requires not-yellow.)
elif hp < _HealHP and not yellow:
    if Have(healpot) and ready("ph_heal", _CD_heal):
        if UsePot(healpot):
            mark("ph_heal")
    else:
        CastSelf("Close Wounds", _CloseWoundsCost)

# 4) curse-type debuff -> Remove Curse.
elif Cursed():
    CastSelf("Remove Curse", _RemoveCurseCost)

# 5) stamina -> refresh potion (Divine Fury excluded: it lowers defense).
elif Stam("self") < _StamMin:
    if Have(refreshpot) and ready("ph_refresh", _CD_refresh):
        if UsePot(refreshpot):
            mark("ph_refresh")

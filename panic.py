# Panic check - single pass, at most one action per run.
# Bind to a hotkey (tap when in trouble) or enable "Loop" on the macro.

# ---------------- CONFIG ----------------
_MortalHP = 93         # apple (clear Mortal) only if life is below this AND yellow-barred
_HealHP   = 81         # heal potion if life is below this
_StamMin  = 23         # refresh potion if stamina is below this

# ---------------- IDS ------------------
healpot    = 0xf0c
curepot    = 0xf07
refreshpot = 0xf0b
eapple     = 0x2fd8

# ---------------- HELPERS --------------
def Have(pid):
    # silent existence check so we never search for a potion we aren't carrying
    return CountType(pid, "backpack") > 0

def UsePot(pid):
    # find by graphic (recursive, silent) and use by serial
    if not FindType(pid, -1, "backpack"):
        return False
    UseObject("found")
    return True

# --------------- PANIC -----------------
# priority: Mortal -> cure -> heal -> refresh
if YellowHits("self") and Hits("self") < _MortalHP and Have(eapple):
    UsePot(eapple)
elif Poisoned("self") and Have(curepot):
    UsePot(curepot)
elif Hits("self") < _HealHP and not YellowHits("self") and Have(healpot):
    UsePot(healpot)
elif Stam("self") < _StamMin and Have(refreshpot):
    UsePot(refreshpot)

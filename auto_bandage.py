# auto_bandage.py - self bandage with dex-timed poison cure. Continuous loop.
# Press once to start; runs until stopped. One action per tick.
#
# RunUO raises NO "Healing" buff icon for bandaging, so we can't ask "am I bandaging?".
# Instead we time it: after applying, block reapply until the bandage's full duration
# (RunUO AOS formula) has elapsed, plus a small finish buffer. This is what stops the
# "you are already applying a bandage" spam.
#
# Idea reused from B_Healer PRO: a finished bandage also CURES poison, and its duration
# scales with Dex. So we time a cure potion to fire ~250ms BEFORE the bandage lands ->
# poison is gone the instant it completes, so the bandage heals HP instead of curing.

HeadMsg("Auto-Bandage Avviato", "self", 68)

# ---------------- CONFIG ----------------
_CureLead     = 250           # fire cure this many ms before the bandage lands
_CureCD       = 1000          # debounce so we don't double-quaff cure during latency
_FinishBuffer = 500           # wait this long PAST the computed duration before reapplying
_MortalDelay  = 1000          # resume bandaging this long after going yellow-barred
_Tick         = 100           # loop pause (ms)

# ---------------- IDS ------------------
bandage  = 0xe21
curepot  = 0xf07
_BandHues = [255, 0]          # preferred hue order: colored (255) first, plain (0) fallback

# ---------------- HELPERS --------------
def BandMs():
    # RunUO AOS self-heal: seconds = 5.0 + 0.5 * ((120 - dex) / 10)
    # (dex120=5000, dex140=4000, dex150=3500). Read live so dex pots / Divine Fury
    # shorten it. 10.0 forces float division (IronPython 2.7).
    return int((5.0 + 0.5 * ((120 - Dex()) / 10.0)) * 1000)

def ready(name, cd):
    return (not TimerExists(name)) or Timer(name) >= cd

def Have(pid):
    return CountType(pid, "backpack") > 0

def UsePot(pid):
    # recursive + silent; UseType only reaches the top of the pack and spams.
    if not FindType(pid, -1, "backpack"):
        return False
    UseObject("found")
    return True

def HaveBand():
    # only count the hues we actually use (255 preferred, 0 fallback)
    for h in _BandHues:
        if CountType(bandage, "backpack", h) > 0:
            return True
    return False

def Bandage():
    # prefer colored (255) bandages, fall back to plain (0). FindType's 4th arg is hue;
    # UseTargetedItem applies the found bandage to self (no manual cursor).
    for h in _BandHues:
        if CountType(bandage, "backpack", h) > 0 and FindType(bandage, -1, "backpack", h):
            UseTargetedItem("found", "self")
            SetTimer("ab_band", 0)
            return True
    return False

# ----------------- LOOP ----------------
while True:
    band_ms  = BandMs()
    yellow   = YellowHits("self")
    poisoned = Poisoned("self")
    hurt     = DiffHits("self") > 0
    need     = hurt or poisoned               # bandage cures poison too, so poison alone counts

    # bandage state from the timer (RunUO has no Healing buff to read)
    elapsed     = Timer("ab_band") if TimerExists("ab_band") else None
    in_progress = elapsed is not None and elapsed < band_ms
    can_band    = elapsed is None or elapsed >= band_ms + _FinishBuffer

    # track Mortal onset for the post-Mortal resume delay
    if yellow:
        if not TimerExists("ab_mortal"):
            SetTimer("ab_mortal", 0)
    elif TimerExists("ab_mortal"):
        RemoveTimer("ab_mortal")

    # warn (throttled) when out of bandages
    if not HaveBand() and ready("ab_warn", 10000):
        HeadMsg("No bandages", "self", 33)
        SetTimer("ab_warn", 0)

    # --- one action per tick (most time-critical first) ---

    # 1) CURE timed ~250ms before the bandage lands -> bandage heals HP, not poison.
    #    Only worth it while hurt (else let the bandage cure for free on completion).
    if poisoned and in_progress and hurt and Have(curepot) \
            and elapsed >= (band_ms - _CureLead) and ready("ab_cure", _CureCD):
        if UsePot(curepot):
            SetTimer("ab_cure", 0)

    # 2) bandage while yellow-barred (Mortal): wait out the short post-Mortal delay.
    elif need and can_band and yellow and HaveBand() \
            and TimerExists("ab_mortal") and Timer("ab_mortal") > _MortalDelay:
        Bandage()

    # 3) bandage normally - only once the previous one has fully finished.
    elif need and can_band and not yellow and HaveBand():
        Bandage()

    Pause(_Tick)

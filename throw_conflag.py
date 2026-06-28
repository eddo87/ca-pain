# throw_conflag.py - drop a conflagration potion on your OWN tile (fire field at your feet).
# Single pass (tap). Conflag has no fuse, so it lands immediately - no throw timing needed.

# ---------------- CONFIG ----------------
_ConflagHue = 1161     # conflag hue (1161 / 0x489 = standard conflag). Use -1 for any hue.
_OffX = 0              # tile offset from self; 0,0 = the tile you're standing on
_OffY = 0
_OffZ = 0

# ---------------- IDS ------------------
CONFLAG_ID = 0xf06

def throw_conflag():
    if CountType(CONFLAG_ID, "backpack", _ConflagHue) <= 0:
        SysMessage("No conflag", 33)
        return

    if not FindType(CONFLAG_ID, -1, "backpack", _ConflagHue):
        return
    UseObject("found")

    if not WaitForTarget(5000):
        SysMessage("No throw cursor", 33)
        return

    TargetTileOffset(_OffX, _OffY, _OffZ)   # your own ground tile

throw_conflag()

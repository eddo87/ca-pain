# throw_explosion.py - timed explosion-potion toss at Last Target. Single pass (tap).
# >>> Run with "do not interrupt" <<< so the fuse Pause can't be broken mid-throw.
#
# Technique: arm the explosion potion (UseObject opens the throw cursor), wait out most
# of the ~3s fuse, THEN target -> it detonates on impact, no time to cure/run. If the
# target ran out of range while the fuse burned, lob the LIVE potion ABORT_RANGE tiles
# behind you so it doesn't blow up in your hand.

# ---------------- CONFIG ----------------
THROW_DELAY = 2850     # ms from arming to throw; tune to your shard's explosion fuse (~3s)
EXPLO_RANGE = 10       # max tiles to target; beyond this we abort
ABORT_RANGE = 3        # tiles behind self to dump a live potion when target is out of range
_ExploHue   = 0        # explosion potion hue (0 = plain)

# ---------------- IDS ------------------
EXPLO_ID = 0xf0d

# ---------------- FACING OFFSETS -------
direction_offsets = {
    'North':     (0, -1),
    'Northeast': (1, -1),
    'East':      (1,  0),
    'Southeast': (1,  1),
    'South':     (0,  1),
    'Southwest': (-1, 1),
    'West':      (-1, 0),
    'Northwest': (-1, -1),
}

# ---------------- HELPERS --------------
def throw_behind():
    # dump the armed potion behind us so it doesn't detonate in hand
    facing = Direction()
    dx, dy = direction_offsets.get(facing, (0, -1))
    TargetTileOffset(-dx * ABORT_RANGE, -dy * ABORT_RANGE, 0)

# ---------------- THROW ----------------
def throw_explosion():
    if not FindAlias("last"):
        SysMessage("No target", 33)
        return
    if CountType(EXPLO_ID, "backpack", _ExploHue) <= 0:
        SysMessage("No explo", 33)
        return

    # arm the potion and start timing the fuse from this instant
    if not FindType(EXPLO_ID, -1, "backpack", _ExploHue):
        return
    UseObject("found")
    SetTimer("Explo", 0)

    if not WaitForTarget(5000):
        SysMessage("No throw cursor", 33)
        return

    # wait out the rest of the fuse (WaitForTarget already ate some of it)
    throw_delay = THROW_DELAY - Timer("Explo")
    if throw_delay > 0:
        Pause(throw_delay)

    # drop any queued weapon special so it can't eat the potion target
    if ActiveAbility():
        SetAbility("primary", "off")

    if InRange("last", EXPLO_RANGE):
        Target("last")
    else:
        HeadMsg("Target not in range, aborting", "self", 33)
        throw_behind()

throw_explosion()

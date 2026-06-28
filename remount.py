# Auto-remount: when dismounted, double-click the best available mount.
# Priority: not-poisoned first, then closest. Single pass (hotkey or Loop macro).

MOUNT_IDS = [
    0x77294,
    0x5ccc2,
    0x1c4bc,
    0x7bacc,
]

MOUNT_RANGE = 2        # mount must be at most this many tiles away to ride it
IDLE_PAUSE  = 1000     # ms between checks while already mounted (keeps CPU low)

MIN_MAGERY   = 40      # min Magery to cure a poisoned mount with "Cure"
MIN_CHIVALRY = 40      # min Chivalry to cure with "Cleanse by Fire"


def mount_info(serial):
    # (distance, poisoned) for a reachable mount, or None if not found / no distance
    if not FindObject(serial):
        return None
    d = Distance(serial)
    if d < 0:
        return None
    return (d, Poisoned(serial))


def try_mount(serial):
    UseObject(serial)                  # single double-click; a second click would dismount
    for _ in range(20):                # wait up to 1s for the mount to register
        Pause(50)
        if Mounted("self"):
            return True
    return False


def cure_pet(serial):
    # cure a poisoned mount so we can ride it: Magery Cure, else Chivalry Cleanse by Fire
    if WaitingForTarget():
        return False

    if Skill("Magery") >= MIN_MAGERY:
        SysMessage("Pet avvelenato: Cure")
        Cast("Cure")
    elif Skill("Chivalry") >= MIN_CHIVALRY:
        SysMessage("Pet avvelenato: Cleanse by Fire")
        Cast("Cleanse by Fire")
    else:
        return False                   # no skill to cure with

    if WaitForTargetOrFizzle(2000):
        Target(serial)
        Pause(600)                     # let the cure resolve
        return not Poisoned(serial)
    return False


def remount_once():
    # scan reachable mounts, ride the best (non-poisoned + closest first)
    candidates = []
    for s in MOUNT_IDS:
        info = mount_info(s)
        if info is not None and info[0] <= MOUNT_RANGE:
            candidates.append((info[1], info[0], s))   # (poisoned, distance, serial)

    candidates.sort()   # non-poisoned (False) first, then nearest

    for poisoned, dist, s in candidates:
        if poisoned:
            if not cure_pet(s):        # healthy ones (sorted first) failed -> cure this one
                continue               # couldn't cure -> try the next candidate
        HeadMsg("SALI", s, 68)         # healthy (or just cured) -> ride it
        if try_mount(s):
            return True
    return False


# ----------------- LOOP ----------------
# Self-paced: while mounted it just sleeps (cheap, no spam);
# the heavy scan only runs when actually dismounted.
while True:
    if Mounted("self"):
        Pause(IDLE_PAUSE)              # already mounted -> idle, check again later
    elif not remount_once():
        Pause(200)                     # nothing rideable nearby -> wait before retry

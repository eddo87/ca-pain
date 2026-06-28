# ClassicAssist
# Versione mago
# Pause massima: 50 ms, salvo dopo cast

PET_SERIALS = [
    0x0006C9C4,
    0x00055CE6,
    0x0005FF57,
    0x0005558C,
    0x00049C84,
    0x00059B4F
]

PET_BALL_SERIALS = [
    0x40636580,
    0x402DBCC0,
    0x402DB7B0,
    0x40242466,
    0x40535fdb
]

MAX_PET_RANGE = 10
MOUNT_RANGE = 1


def pet_distance(serial):
    if not FindObject(serial):
        return -1

    d = Distance(serial)

    if d < 0:
        return -1

    return d


def nearest_pet_within(max_range):
    nearest = 0
    nearest_dist = 9999

    for pet in PET_SERIALS:
        d = pet_distance(pet)

        if d >= 0 and d <= max_range and d < nearest_dist:
            nearest = pet
            nearest_dist = d

    return nearest


def use_pet_balls():
    SysMessage("Pet non vicino: uso pet ball")

    for ball in PET_BALL_SERIALS:
        if nearest_pet_within(MAX_PET_RANGE):   # a previous ball already brought one
            return
        UseObject(ball)
        Pause(1000)                             # pet balls have a server cooldown


def wait_for_pet_within(max_range, cycles):
    for _ in range(cycles):
        pet = nearest_pet_within(max_range)

        if pet:
            return pet

        Pause(50)

    return 0


def wait_pet_at_mount_range(pet, cycles):
    Msg("All follow me")

    for i in range(cycles):
        d = pet_distance(pet)

        if d >= 0 and d <= MOUNT_RANGE:
            return True

        if i and i % 20 == 0:       # re-say ~every 1s (20 * 50ms), not every tick
            Msg("All follow me")

        Pause(50)

    return False


def cure_if_needed(pet):
    if not Poisoned(pet):
        return True

    SysMessage("Pet avvelenato: cast Cure")

    if TargetExists("Beneficial"):
        Target(pet)
        Pause(100)
        return True

    if WaitingForTarget():
        return False

    Cast("Cure")

    if WaitForTargetOrFizzle(1200):
        d = pet_distance(pet)
        if d >= 0 and d <= MAX_PET_RANGE:
            Target(pet)
            Pause(250)
            return True

    return False


def mount_pet(pet):
    if not pet:
        return False

    d = pet_distance(pet)

    if d < 0 or d > MOUNT_RANGE:
        return False

    cure_if_needed(pet)

    Pause(50)

    for _ in range(2):              # mount, then one retry if it didn't take
        UseObject(pet)             # single double-click; a second click would dismount

        for _ in range(20):        # wait up to 1s for the mount to register
            Pause(50)

            if Mounted("self"):
                return True

    return False


def ensure_mounted():
    if Mounted("self"):
        SysMessage("Sei gia montato")
        return

    if WaitingForTarget():
        return

    pet = nearest_pet_within(MAX_PET_RANGE)

    if not pet:
        use_pet_balls()
        pet = wait_for_pet_within(MAX_PET_RANGE, 80)

    if not pet:
        SysMessage("Nessun pet trovato dopo pet ball")
        return

    if wait_pet_at_mount_range(pet, 120):
        if mount_pet(pet):
            SysMessage("Pet montato")
        else:
            SysMessage("Mount fallito")
    else:
        SysMessage("Pet non arrivato a 1 tile")


ensure_mounted()
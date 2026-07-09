# rapid_explo.py - rapid-fire explosion potions at the LAST TARGET's feet (ground tile).
# Loops by itself: keeps throwing until no potions / target dead or gone. Tap to start.
# No fuse hold (unlike throw_explosion.py): each potion is thrown immediately at the
# tile under the target and detonates there ~1.8s later - spam pressure, not a timed hit.

# ---------------- CONFIG ----------------
THROW_MS    = 1800     # ritmo tra i lanci (dal macro shard-tested: Pause(1801))
CURSOR_MS   = 500      # attesa cursore prima di assumere "cooldown"
RETRY_MS    = 250      # pausa prima di riprovare dopo un rifiuto per cooldown
DEBUG       = False    # stampa i ms tra i lanci riusciti, per ritarare THROW_MS
EXPLO_RANGE = 10       # oltre questa distanza non lancia
ABORT_RANGE = 3        # a quante caselle scaricare una pozione armata se il target sparisce
_ExploHue   = 0        # explosion potion hue (0 = plain)

# ---------------- IDS ------------------
EXPLO_ID = 0xf0d

def bersaglio_valido():
    return FindAlias("last") and FindObject("last") and not Dead("last")

# ---------------- LOOP ------------------
SetTimer("ExploRate", 0)   # misura il tempo tra un lancio riuscito e l'altro

while True:
    if not FindType(EXPLO_ID, -1, "backpack", _ExploHue):
        HeadMsg("| NON HO EXPLO |", "self", 35)
        break
    if not bersaglio_valido():
        SysMessage("No target", 33)
        break
    if not InRange("last", EXPLO_RANGE):
        Pause(THROW_MS)          # aspetta che torni a tiro, senza armare niente
        continue

    UseObject("found")

    # niente cursore = quasi sempre cooldown pozioni del server: riprova, non morire
    if not WaitForTarget(CURSOR_MS):
        if DEBUG:
            SysMessage("cooldown, retry (+%dms)" % Timer("ExploRate"), 53)
        Pause(RETRY_MS)
        continue

    # drop any queued weapon special so it can't eat the potion target
    if ActiveAbility():
        SetAbility("primary", "off")

    # coordinate lette ADESSO: la pozione insegue il target che corre
    if bersaglio_valido() and InRange("last", EXPLO_RANGE):
        TargetXYZ(X("last"), Y("last"), Z("last"))
        HeadMsg("BoOoOoM", "last", 35)
        if DEBUG:
            SysMessage("explo +%dms" % Timer("ExploRate"), 88)
        SetTimer("ExploRate", 0)
    else:
        HeadMsg("Scorregginiii", "self", 35)
        TargetTileRelative("self", ABORT_RANGE, True)   # scarica la pozione viva dietro di te
        break

    Pause(THROW_MS)

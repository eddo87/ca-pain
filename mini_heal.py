# mini_heal.py - lightweight self cure/heal. Single pass (hotkey tap, or enable "Loop").
# One spell per press. Spells only (no potions, no cooldown timers) - the light sibling
# of panic_heal.py. Picks a school by skill: Chivalry preferred, Magery fallback.
#
#   Chivalry (>40): Cleanse by Fire | Remove Curse | Close Wounds
#   Magery   (>40): Cure | Heal     (no curse removal in this school)

# ---------------- CONFIG ----------------
_SkillMin = 40         # a school is usable only above this skill value

# curse-type buffs cleared by Remove Curse - exact names from ../Data/BuffIcons.json
_curseBuffs = ["Curse", "Mass Curse", "Clumsy", "Weaken", "FeebleMind", "Strangle", "Corpse Skin"]

# ---------------- HELPERS ----------------
def Cursed():
    for b in _curseBuffs:
        if BuffExists(b):
            return True
    return False

# ---------------- DETECT SCHOOL ----------------
_chiv = Skill("Chivalry") > _SkillMin
_mage = Skill("Magery")   > _SkillMin

yellow = YellowHits("self")
hurt   = DiffHits("self") > 0          # any HP missing

# ---------------- SELF CURE / HEAL (one action) ----------------
# Chivalry preferred when both schools qualify.
if _chiv:
    # 1) poison -> Cleanse by Fire
    if Poisoned("self"):
        Cast("Cleanse by Fire", "self")
    # 2) Mortal/yellow bar or a curse -> Remove Curse (clears yellow on this shard so
    #    healing works again; nothing heals while yellow-barred)
    elif yellow or Cursed():
        Cast("Remove Curse", "self")
    # 3) heal
    elif hurt:
        Cast("Close Wounds", "self")

elif _mage:
    # 1) poison -> Cure (works even while yellow-barred)
    if Poisoned("self"):
        Cast("Cure", "self")
    # 2) heal - Heal is blocked while yellow-barred, and Magery has no Mortal clear,
    #    so only attempt when not yellow.
    elif hurt and not yellow:
        Cast("Heal", "self")

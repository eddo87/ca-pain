# change_weapon.py - swap to a specific weapon. Single pass (tap).
# Ported from a RazorEnhanced macro. Casting a junk spell (Create Food) right before
# equipping bypasses the weapon-swap delay so you can arm instantly.
#
# CA vs RazorEnhanced notes:
#   RE Player.CheckLayer/GetItemOnLayer  -> CA FindLayer(layer) (sets the "found" alias)
#   RE Player.EquipItem(serial)          -> CA EquipItem(serial, layer)   <-- layer required
#   RE Spells.CastMagery(name)           -> CA Cast(name)

# ---------------- CONFIG ----------------
bow    = 0x4049A1AC        # serial of the weapon to equip
_Layer = "TwoHanded"       # bow is two-handed; use "OneHanded" for a 1H weapon

# ---------------- SWAP ------------------
if FindLayer(_Layer):                       # something is already in that hand
    if GetAlias("found") == bow:
        SysMessage("Arma gia equipaggiata!", 65)
    else:
        Cast("Create Food")                 # junk cast to beat the weapon-swap delay
        EquipItem(bow, _Layer)
        Pause(100)
else:                                        # that hand is empty -> just equip
    EquipItem(bow, _Layer)
    Pause(100)

HeadMsg("Compo", "self", 65)

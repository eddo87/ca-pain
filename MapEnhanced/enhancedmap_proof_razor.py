# RazorEnhanced - PHASE 1 PROOF
# Pushes HP/Stam/Mana to a running EnhancedMap via Win32 window messages.
# Purpose: prove bars light up WITHOUT the UDP listener patch. For the real
# solution use enhancedmap_feeder_razor.py instead.
#
# NOTE: Win32 PostMessage from RazorEnhanced's IronPython relies on `ctypes`.
# This is the ONE unverified piece (see razor-scripting skill rule). If you see
# "DEBUG FAIL: ctypes..." in the RE message area, ctypes is unavailable in your
# RE build -- skip this proof and go straight to the UDP feeder (Phase 2),
# whose receiving end is already built and unit-tested.
#
# Message ids are WM_USER (0x400) + offset, fixed by PlayerObject.PreFilterMessage:
#   MANA_MAXMANA = 0x400 + 305 ; HP_MAXHP = 0x400 + 309 ; STAM_MAXSTAM = 0x400 + 310
# Packing (from the handlers): wParam = MAX value, lParam = CURRENT value.

from System import IntPtr
from System.Diagnostics import Process

WM_MANA = 0x400 + 305
WM_HP   = 0x400 + 309
WM_STAM = 0x400 + 310

_ctypes_ok = False
try:
    import ctypes
    _PostMessage = ctypes.windll.user32.PostMessageW
    _ctypes_ok = True
    Misc.SendMessage("EM proof: ctypes OK", 68)
except Exception as e:
    Misc.SendMessage("DEBUG FAIL: ctypes unavailable - " + str(e), 33)


def enhancedmap_hwnd():
    for p in Process.GetProcessesByName("EnhancedMap"):
        if p.MainWindowHandle != IntPtr.Zero:
            return p.MainWindowHandle.ToInt64()
    return 0


def post(hwnd, msg, wparam, lparam):
    # PostMessageW(HWND, UINT, WPARAM, LPARAM)
    _PostMessage(int(hwnd), int(msg), int(wparam), int(lparam))


if _ctypes_ok:
    while True:
        h = enhancedmap_hwnd()
        if h != 0:
            post(h, WM_HP,   Player.HitsMax, Player.Hits)
            post(h, WM_STAM, Player.StamMax, Player.Stam)
            post(h, WM_MANA, Player.ManaMax, Player.Mana)
        Misc.Pause(500)

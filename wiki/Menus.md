# Menus

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Menus) · 4 commands

- **InMenu(gumpid, text) -> bool**
  Returns True if the menu title or entry titles contains the given text.
  `gumpid`: ItemID / Graphic such as  0x3db.

- **MenuExists() -> bool**
  Return true if the given menu id exists.
  `if MenuExists(0x1d1):`

- **ReplyMenu(gumpid, buttonid, [itemid], [hue])**
  Sends a button reply to server menu
  `gumpid`: ItemID / Graphic such as  0x3db. · `buttonid`: Gump button ID. · `itemid`: ItemID / Graphic such as  0x3db. · `hue`: Item Hue or -1 for any.
  `ReplyMenu(0x1d0, 3, 0x2106, 0)`

- **WaitForMenu([gumpid], [timeout]) -> bool**
  Pauses until incoming menu packet is received, optional paramters of gump ID and timeout
  `gumpid`: ItemID / Graphic such as  0x3db. · `timeout`: Timeout specified in milliseconds.

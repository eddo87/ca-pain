# Gumps

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Gumps) · 13 commands

- **CloseGump(serial)**
  Close a specified gump serial
  `serial`: An entity serial such as 0xf00ff00f.
  `CloseGump(0x454ddef)`

- **ConfirmPrompt() -> bool**
  Displays an ingame prompt with the specified message, returns True if Okay was pressed, False if not.

- **GumpExists() -> bool**
  Checks if a gump id exists or not.
  `if GumpExists(0xff):`

- **InGump(gumpid, text) -> bool**
  Check for a text in gump.
  `gumpid`: An entity serial in integer or hex format, or an alias string such as "self".
  `if InGump(0xf00f, "lethal darts"):`

- **ItemArrayGump() -> int[]**
  Displays a gump with the selected serials / aliases in a grid, similar to the UOSteam loot grid, returns array of serials selected

- **MessagePrompt(message, [initialtext], [closable]) -> tuple**
  Displays an ingame gump prompting for a message
  `closable`: True/False value, see description for usage.

- **OpenGuildGump()**
  Opens the Guild gump
  `OpenGuildGump()`

- **OpenHelpGump()**
  Opens the Help gump
  `OpenHelpGump()`

- **OpenQuestsGump()**
  Opens the Quests gump
  `OpenQuestsGump()`

- **OpenVirtueGump([obj])**
  Opens the Virtue gump of the given serial/alias (defaults to current player)
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `OpenVirtueGump("enemy")`

- **ReplyGump(gumpid, buttonid, [switches], [textentries])**
  Sends a button reply to server gump, parameters are gumpID and buttonID.
  `gumpid`: ItemID / Graphic such as  0x3db. · `buttonid`: Gump button ID. · `textentries`: Not specified - See description for usage.
  `ReplyGump(0xff, 0)`

- **SelectionPrompt(options, [message], [closable]) -> tuple**
  Produces an in-game gump to choose from a list of options
  `options`: An array of strings. · `closable`: True/False value, see description for usage.

- **WaitForGump([gumpid], [timeout]) -> bool**
  Pauses until incoming gump packet is received, optional paramters of gump ID and timeout
  `gumpid`: ItemID / Graphic such as  0x3db. · `timeout`: Timeout specified in milliseconds.
  `WaitForGump(0xff, 5000)`

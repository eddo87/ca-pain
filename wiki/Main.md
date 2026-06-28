# Main

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Main) · 21 commands

- **BringClientWindowToFront()**
  Bring client window to front
  `BringClientWindowToFront()`

- **DisplayQuestPointer(x, y, [enabled])**
  Display quest arrow pointer to specified coordinates
  `x`: X Coordinate. · `y`: Y Coordinate. · `enabled`: True/False value, see description for usage.

- **HideEntity(obj)**
  Remove an item/mobile from the screen
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".

- **Hotkeys([onoff])**
  Enable and disable hotkeys.
  `onoff`: "on" or "off".
  `Hotkeys()`

- **Info([obj])**
  Show object inspector for supplied serial / alias, will prompt for target if no parameter given.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Info("self")`

- **InvokeVirtue(virtue)**
  Use a virtue by name.
  `virtue`: String value - See description for usage. See Also: [Virtues](#Virtues)
  `InvokeVirtue("Honor")`

- **Logout()**
  Disconnects from the server and returns to the login screen
  `Logout()`

- **MessageBox(title, body)**
  Show a simple message box with a custom title and body.
  `MessageBox("title", "message")`

- **OpenECV(obj)**
  Open entity collection viewer for specified container serial/alias
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `OpenECV('backpack')`

- **Pause(milliseconds)**
  Pauses execution for the given amount in milliseconds.
  `milliseconds`: Timeout specified in milliseconds.
  `Pause(1000)`

- **Playing() -> bool**
  Returns true if there is a macro, use in background macros.
  `if Playing():`

- **Playing(macroname) -> bool**
  Returns true if there is a macro, use in background macros.
  `macroname`: Macro name.
  `if Playing():`

- **PlaySound()**
  Play sound by id or system .wav file.
  `PlaySound("Bike Horn.wav")`

- **Quit()**
  Closes the client
  `Quit()`

- **Resync()**
  Sends Resync request to server.
  `Resync()`

- **SetAutologin()**
  Configures autologin settings
  `SetAutologin(False)`

- **SetQuietMode(onoff)**
  Set quiet mode True/False, True reduces the number of messages macro commands emit.
  `onoff`: "on" or "off".
  `SetQuietMode(True)`

- **Snapshot([delay], [fullscreen], [filename]) -> tuple**
  Take a screenshot of the window
  `fullscreen`: True/False value, see description for usage.

- **SysMessage(text, [hue])**
  Send a text message.
  `hue`: Item Hue or -1 for any.

- **WarMode([onoff])**
  Sets war mode status, parameter on, off, or toggle, defaults to toggle if no parameter given.
  `onoff`: "on" or "off".
  `WarMode("on")`

- **Virtues()**

# Aliases

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Aliases) · 11 commands

- **FindAlias(aliasname) -> bool**
  Returns true if alias serial can be found on screen, false if not.
  `aliasname`: Alias name.
  `if FindAlias("mount"):`

- **GetAlias(aliasname) -> int**
  Gets the value of the given alias name.
  `aliasname`: Alias name.
  `GetAlias("mount")`

- **GetPlayerAlias(aliasname) -> int**
  Gets the value of the given alias name, for the current player.
  `aliasname`: Alias name.
  `GetPlayerAlias("mount")`

- **PromptAlias(aliasname) -> int**
  Prompt with an in-game target cursor to supply value for given alias name.
  `aliasname`: Alias name.
  `PromptAlias("mount")`

- **PromptMacroAlias(aliasname) -> int**
  Prompt with an in-game target cursor to supply value for given alias name, alias is valid only in the current macro.
  `aliasname`: Alias name.
  `PromptMacroAlias("mount")`

- **PromptPlayerAlias(aliasname) -> int**
  Prompt with an in-game target cursor to supply value for given alias name, for the current player.
  `aliasname`: Alias name.
  `PromptPlayerAlias("mount")`

- **SetAlias(aliasname, obj)**
  Sets the value of the given alias name.
  `aliasname`: Alias name. · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetAlias("mount", 0x40000001)`

- **SetMacroAlias(aliasname, obj)**
  Sets the value of the given alias name, alias is valid only in the current macro.
  `aliasname`: Alias name. · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetMacroAlias("mount", 0x40000001)`

- **SetPlayerAlias(aliasname, obj)**
  Sets the value of the given alias name, for the current player.
  `aliasname`: Alias name. · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetPlayerAlias("mount", 0x40000001)`

- **UnsetAlias(aliasname)**
  Removes the alias name given.
  `aliasname`: Alias name.
  `UnsetAlias("mount")`

- **UnsetPlayerAlias(aliasname)**
  Removes the alias name given, for the current player.
  `aliasname`: Alias name.
  `UnsetPlayerAlias("mount")`

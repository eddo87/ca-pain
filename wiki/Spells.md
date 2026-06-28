# Spells

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Spells) · 3 commands

- **Cast(name)**
  Cast the given named spell and automatically target given object.
  `name`: Spell name.
  `Cast("Recall", "runebook")`

- **Cast(name, obj) -> bool**
  Cast the given named spell and automatically target given object.
  `name`: Spell name. · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Cast("Recall", "runebook")`

- **InterruptSpell()**
  Attempts to interrupt spell by lifting an item briefly.
  `InterruptSpell()`

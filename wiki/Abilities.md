# Abilities

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Abilities) · 6 commands

- **ActiveAbility() -> bool**
  Returns True if either the primary or secondary ability is set

- **ClearAbility()**
  Clear weapon ability.
  `ClearAbility()`

- **Fly()**
  (Garoyle) Start flying if not already flying.
  `Fly()`

- **Flying(obj) -> bool**
  Returns true if mobile is currently flying.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Flying("self"):`

- **Land()**
  (Garoyle) Stop flying if currently flying.
  `Land()`

- **SetAbility(ability, [onoff])**
  Set weapon ability, parameter "primary" / "secondary".
  `ability`: The name of the ability, "primary", "secondary", "stun" or "disarm". · `onoff`: "on" or "off".
  `SetAbility("primary")`

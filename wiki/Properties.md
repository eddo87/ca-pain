# Properties

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Properties) · 3 commands

- **Property(obj, value) -> bool**
  Returns true if the given text appears in the items item properties.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Property("item", "Defense Chance Increase"):`

- **PropertyValue(obj, property, [argument]) -> T**
  Returns the argument value of the given property name. Optional argument index.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `val = PropertyValue[int]("backpack", "Contents")`

- **WaitForProperties(obj, timeout) -> bool**
  Wait for item properties to be received for specified item.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `timeout`: Timeout specified in milliseconds.
  `WaitForProperties("backpack", 5000)`

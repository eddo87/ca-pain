# Agents

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Agents) · 19 commands

- **Autoloot(obj)**
  Causes autoloot to check a particular container, even when not enabled, and bypassing the corpse type check
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Autoloot("found")`

- **Autolooting() -> bool**
  Returns True if currently checking corpse / autolooting items.
  `if Autolooting():`

- **ClearTrapPouch()**
  Clears the items in the trap pouch agent...
  `ClearTrapPouch()`

- **Counter(name) -> int**
  Returns the count of the given counter agent.
  `name`: Agent entry name.
  `Counter("bm")`

- **Dress([name])**
  Dress all items in the specified dress agent.
  `name`: Agent entry name.
  `Dress("Dress-1")`

- **DressConfig()**
  Adds all equipped items to a temporary list that isn't persisted on client close.
  `DressConfig()`

- **Dressing() -> bool**
  Returns true if the Dress agent is currently dressing or undressing.
  `if Dressing():`

- **Organizer(name, [sourcecontainer], [destinationcontainer])**
  Executes the named Organizer agent.
  `name`: Agent entry name. · `sourcecontainer`: An entity serial in integer or hex format, or an alias string such as "self". · `destinationcontainer`: An entity serial in integer or hex format, or an alias string such as "self".
  `Organizer("Organizer-1")`

- **Organizing() -> bool**
  Returns true if currently running an organizer agent, or false if not.
  `if Organizing():`

- **SetAutoloot([onoff])**
  Enable/Disable/Toggle the Autoloot agent
  `onoff`: "on" or "off".
  `SetAutoloot("off")`

- **SetAutolootContainer(obj)**
  Sets the container for the Autoloot agent to put items into...
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetAutolootContainer("backpack")`

- **SetOrganizerContainers(entryname, [sourcecontainer], [destinationcontainer])**
  Set the source and destination for the specified Organizer name
  `entryname`: Agent entry name. · `sourcecontainer`: An entity serial in integer or hex format, or an alias string such as "self". · `destinationcontainer`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetOrganizerContainers("Organizer-1", "backpack", "bank")`

- **SetScavenger([onoff])**
  Enable/Disable/Toggle the Scavenger agent
  `onoff`: "on" or "off".
  `SetScavenger("off")`

- **SetTrapPouch(obj)**
  Adds the specified item to the trap pouch agent item list...
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".

- **SetVendorBuyAutoBuy(listname, [onoff])**
  Enables or disables autobuying of the specified vendor buy list name...
  `listname`: List name. · `onoff`: "on" or "off".

- **StopDress()**
  Stops the dress agent is it is currently running
  `StopDress()`

- **StopOrganizer()**
  Stops the organizer agent if currently running
  `StopOrganizer()`

- **Undress(name)**
  Undress all items in the specified dress agent.
  `name`: Agent entry name.
  `Undress("Dress-1")`

- **UseTrapPouch()**
  Uses the first item in the Trap Pouch agent list...
  `UseTrapPouch()`

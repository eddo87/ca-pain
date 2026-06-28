# Entity

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Entity) · 75 commands

- **AddFriend([obj]) -> int**
  Adds a mobile to friends list, will display target cursor if no serial/alias supplied.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `AddFriend()`

- **Ally(obj) -> bool**
  Returns true if the mobile's notoriety is Ally
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **AutoColorPick(hue)**
  Setup an automated reply to the incoming dye color gump, allowing you to define dye tubs color.
  `hue`: Item Hue or -1 for any.

- **BuffExists(name) -> bool**
  Check for a specific buff
  `name`: Buff name.
  `if BuffExists("Blood Oath"):`

- **BuffTime(name) -> float**
  Returns milliseconds remaining for given buff name, or 0 if expired/not enabled.
  `name`: Buff name.

- **ClearIgnoreList()**
  Clears the ignore list.
  `ClearIgnoreList()`

- **ClearObjectQueue()**
  Clears all actions in action packet queue
  `ClearObjectQueue()`

- **CountType(graphic, [source], [hue]) -> int**
  Amount comparison of item type inside a container.
  `graphic`: ItemID / Graphic such as  0x3db. · `source`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any.
  `CountType(0xff, "backpack")`

- **CountTypeGround(graphic, [hue], [range]) -> int**
  Amount comparison of item or mobile type on the ground.
  `graphic`: ItemID / Graphic such as  0x3db. · `hue`: Item Hue or -1 for any. · `range`: Range, ie 10.
  `if CountGround(0xff, 0, 10) < 1:`

- **Criminal(obj) -> bool**
  Returns true if the mobile's notoriety is Criminal
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **Dead([obj]) -> bool**
  Returns true if given mobile is dead, false if not, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Dead("self"):`

- **Dex() -> int**
  Returns the dexterity of the player
  `if Str() < 100:`

- **DiffHits([obj]) -> int**
  Returns the given mobiles difference between max and current hits, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if DiffHits("self") > 50:`

- **DiffHitsPercent([obj]) -> float**
  Returns the given mobiles different between max and currents hits as a percentage, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if DiffHitsPercent("self") > 30: # 70% health`

- **DiffWeight() -> int**
  Returns the difference between max weight and weight.
  `if DiffWeight() > 50:`

- **Direction([obj]) -> str**
  Returns the Direction the given alias/serial is facing
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Direction('enemy') == 'West':`

- **DirectionTo(obj) -> str**
  Returns the Direction the entity is in relative to the player.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Run(DirectionTo("enemy"))`

- **Distance(x, y) -> int**
  Returns the distance to the given coordinates.
  `x`: X Coordinate. · `y`: Y Coordinate.

- **Distance([obj]) -> int**
  Returns the distance to the given entity.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Distance("mount") < 4:`

- **Enemy(obj) -> bool**
  Returns true if the mobile's notoriety is Enemy
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **EquipWand(wandname, [minimumcharges]) -> bool**
  Search for a wand inside your backpack and equip it
  `wandname`: Wand name. See Also: [WandTypes](#WandTypes)

- **FasterCasting() -> float**
  Return faster casting value.
  `fc = FasterCasting()`

- **FasterCastRecovery() -> float**
  Return faster cast recovery value.
  `fcr = FasterCastRecovery()`

- **FindObject(obj, [range], [findlocation]) -> bool**
  Searches for entity by serial and sets found alias, defaults to ground if no source given.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `range`: Range, ie 10. · `findlocation`: An entity serial in integer or hex format, or an alias string such as "self".

- **FindType(graphic, [range], [findlocation], [hue], [minimumstackamount]) -> bool**
  Searches for entity by graphic ID and sets found alias, defaults to ground if no source given.
  `graphic`: ItemID / Graphic such as  0x3db. · `range`: Range, ie 10. · `findlocation`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any. · `minimumstackamount`: Integer representing an amount, ie 10.

- **FindWand(wandname, [containersource], [minimumcharges]) -> bool**
  Search for a wand and set alias "found".
  `wandname`: Wand name. See Also: [WandTypes](#WandTypes) · `containersource`: An entity serial in integer or hex format, or an alias string such as "self".
  `FindWand("fireball", "backpack", 10)`

- **Followers() -> int**
  Returns the number of current followers as per status bar data.
  `if Followers() < 1:`

- **Gold() -> int**
  Returns the gold value as per status bar data.
  `if Gold() < 2000:`

- **Graphic([obj]) -> int**
  Returns Item ID of given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Graphic("mount")`

- **Gray(obj) -> bool**
  Returns true if the mobile's notoriety is Attackable
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **Hidden([obj]) -> bool**
  Returns true if given mobile is hidden, false if not, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Hidden("self"):`

- **Hits([obj]) -> int**
  Returns the given mobiles hitpoints, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `hits = Hits("self")`

- **Hue([obj]) -> int**
  Returns Hue of given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Hue("mount") == 0:`

- **IgnoreObject(obj)**
  Ignores the given object from find commands
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `IgnoreObject("self")`

- **InFriendList(obj) -> bool**
  Returns true if supplied mobile exists in the friends list.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if InFriendList("last"):`

- **InIgnoreList(obj) -> bool**
  Check whether the given serial / alias exists in the ignore list.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if InIgnoreList("mount"):`

- **Innocent(obj) -> bool**
  Returns true if the mobile's notoriety is Innocent
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **InParty(obj) -> bool**
  Return the true if the given serial/alias is in party with you.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if InParty("friend"):`

- **InRange(obj, distance) -> bool**
  Check for range between your character and another mobile or an item
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `distance`: Distance.
  `if InRange("enemy", 10):`

- **Int() -> int**
  Returns the intelligence of the player
  `if Str() < 100:`

- **Invulnerable(obj) -> bool**
  Returns true if the mobile's notoriety is Invulnerable
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **Luck() -> int**
  Returns the luck value as per status bar data.
  `if Luck() < 800:`

- **Mana([obj]) -> int**
  Returns the given mobiles mana, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Mana("self") < 25:`

- **Map() -> int**
  Returns the current map of the Player
  `Map()`

- **MaxFollowers() -> int**
  Returns the number of max followers as per status bar data.
  `if Followers() == MaxFollowers():`

- **MaxHits([obj]) -> int**
  Returns the given mobiles max hitpoints, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `hits = MaxHits("self")`

- **MaxMana([obj]) -> int**
  Returns the given mobiles max mana, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `mana = MaxMana("self")`

- **MaxStam([obj]) -> int**
  Returns the given mobiles max stamina, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `stam = MaxStam("self")`

- **MaxWeight() -> int**
  Returns the max weight as per status bar data.
  `if MaxWeight() < 300:`

- **Mounted(obj) -> bool**
  Returns true if the specified mobile is mounted.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Mounted("self"):`

- **MoveItem(item, destination, [amount], [x], [y])**
  Move item to container (parameters can be serials or aliases).
  `item`: An entity serial in integer or hex format, or an alias string such as "self". · `destination`: An entity serial in integer or hex format, or an alias string such as "self". · `amount`: Integer representing an amount, ie 10. · `x`: X Coordinate. · `y`: Y Coordinate.
  `MoveItem("source", "destination")`

- **MoveItemOffset(obj, xoffset, yoffset, zoffset, [amount])**
  Move the given serial/alias to the specified x,y,z offset of the player, no amount specified or -1 will move the full stack.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `xoffset`: X Coordinate offset. · `yoffset`: Y Coordinate offset. · `zoffset`: Z Coordinate offset. · `amount`: Integer representing an amount, ie 10.
  `MoveItemOffset("trashitem", 0, 1, 0, -1)`

- **MoveItemXYZ(item, x, y, z, [amount])**
  Moves the specified serial/alias to the given coordinates
  `item`: An entity serial in integer or hex format, or an alias string such as "self". · `x`: X Coordinate. · `y`: Y Coordinate. · `z`: Z Coordinate. · `amount`: Integer representing an amount, ie 10.
  `MoveItemXYZ('found', 0, 0, 0)`

- **MoveType(id, sourcecontainer, destinationcontainer, [x], [y], [z], [hue], [amount])**
  Move a type from source to destintion.
  `id`: ItemID / Graphic such as  0x3db. · `sourcecontainer`: An entity serial in integer or hex format, or an alias string such as "self". · `destinationcontainer`: An entity serial in integer or hex format, or an alias string such as "self". · `x`: X Coordinate. · `y`: Y Coordinate. · `z`: Z Coordinate. · `hue`: Item Hue or -1 for any. · `amount`: Integer representing an amount, ie 10.

- **MoveTypeOffset(id, findlocation, xoffset, yoffset, zoffset, [amount], [hue], [range]) -> bool**
  Move the given type from the specified source container to the specified x,y,z offset of the player, no amount specified or -1 will move the full stack.
  `id`: ItemID / Graphic such as  0x3db. · `findlocation`: An entity serial in integer or hex format, or an alias string such as "self". · `xoffset`: X Coordinate offset. · `yoffset`: Y Coordinate offset. · `zoffset`: Z Coordinate offset. · `amount`: Integer representing an amount, ie 10. · `hue`: Item Hue or -1 for any. · `range`: Distance.
  `MoveTypeOffset(0xf0e, "backpack", 0, 1, 0, -1)`

- **MoveTypeXYZ(id, findlocation, x, y, z, [amount], [hue], [range]) -> bool**
  Move the given type from the specified source container to the specified X, Y, Z, no amount specified or -1 will move the full stack.
  `id`: ItemID / Graphic such as  0x3db. · `findlocation`: An entity serial in integer or hex format, or an alias string such as "self". · `x`: X Coordinate. · `y`: Y Coordinate. · `z`: Z Coordinate. · `amount`: Integer representing an amount, ie 10. · `hue`: Item Hue or -1 for any. · `range`: Distance.
  `MoveTypeXYZ(0xf0e, "backpack", 0, 0, 0, -1)`

- **Murderer(obj) -> bool**
  Returns true if the mobile's notoriety is Murderer
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Criminal("mount"):`

- **Name([obj]) -> str**
  Return the name of the given mobile.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Name("self") == "Shmoo":`

- **Paralyzed(obj) -> bool**
  Returns true if the specified mobile is frozen.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Paralyzed("self"):`

- **Poisoned(obj) -> bool**
  Returns true if the specified mobile is poisoned.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Poisoned("self"):`

- **Rehue(obj, hue)**
  Rehue an item/mobile the specified hue value, set to 0 to remove. (Experimental)
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any.
  `Rehue("mount", 1176)`

- **RemoveFriend([obj])**
  Removes a mobile from the friends list, will display target cursor if no serial/alias supplied.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `RemoveFriend()`

- **SpecialMoveExists(name) -> bool**
  Check for a specific special move
  `name`: Special move name.
  `if SpecialMoveExists("Death Strike"):`

- **Stam([obj]) -> int**
  Returns the given mobiles stamina, if parameter is null, then returns the value from the player (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Stam("self") < 25:`

- **Str() -> int**
  Returns the strength of the player
  `if Str() < 100:`

- **SwingSpeedIncrease() -> int**
  Return SwingSpeed Increase value.
  `ssi = SwingSpeedIncrease()`

- **TithingPoints() -> int**
  Returns the current players' tithing points.
  `if TithingPoints() < 1000:`

- **UseLayer(layer, [obj]) -> bool**
  Uses object in the specified layer, optional parameter for mobile
  `layer`: String representing a layer, such as "OneHanded" or "Talisman" etc. · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `UseLayer("Talisman")`

- **War(obj) -> bool**
  Checks whether a mobile is in war mode.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if War("self"):`

- **Weight() -> int**
  Returns the current weight as as per status bar data.
  `if Weight() > 300:`

- **X([obj]) -> int**
  Returns X coordinate of given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `x = X("self")`

- **Y([obj]) -> int**
  Returns Y coordinate of given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `y = Y("self")`

- **YellowHits(obj) -> bool**
  Returns true if the specified mobile is yellowhits.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if YellowHits("self"):`

- **Z([obj]) -> int**
  Returns Z coordinate of given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `y = Y("self")`

- **WandTypes()**

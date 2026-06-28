# Target

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Target) · 26 commands

- **CancelTarget()**
  Cancel an existing cursor/target.
  `CancelTarget()`

- **ClearTargetQueue()**
  Clears the target queue when queue last target/target self is enabled.
  `ClearTargetQueue()`

- **GetEnemy(notorieties, [bodytype], [distance], [infliction], [maxdistance]) -> bool**
  Get mobile and set enemy alias.
  `notorieties`: . See Also: [TargetNotoriety](#TargetNotoriety) · `bodytype`: .  See Also: [TargetBodyType](#TargetBodyType) · `distance`: .  See Also: [TargetDistance](#TargetDistance) · `infliction`: .  See Also: [TargetInfliction](#TargetInfliction) · `maxdistance`: Distance.

- **GetFriend(notorieties, [bodytype], [distance], [infliction], [maxdistance]) -> bool**
  Get mobile and set friend alias.
  `notorieties`: . See Also: [TargetNotoriety](#TargetNotoriety) · `bodytype`: .  See Also: [TargetBodyType](#TargetBodyType) · `distance`: .  See Also: [TargetDistance](#TargetDistance) · `infliction`: .  See Also: [TargetInfliction](#TargetInfliction) · `maxdistance`: Distance.
  `GetFriend(["Murderer"])`

- **GetFriendListOnly([distance], [targetinfliction], [bodytype], [maxdistance]) -> bool**
  Get friend that only exists in the friends list, parameter distance 'Closest'/'Nearest'/'Next'
  `distance`: .  See Also: [TargetDistance](#TargetDistance) · `targetinfliction`: .  See Also: [TargetInfliction](#TargetInfliction) · `bodytype`: .  See Also: [TargetBodyType](#TargetBodyType) · `maxdistance`: Distance.
  `GetFriendListOnly("Closest")`

- **SetEnemy(obj)**
  Sets the enemy to the given serial/alias.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetEnemy("mount")`

- **SetFriend(obj)**
  Sets the friend to the given serial/alias.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetFriend("mount")`

- **SetLastTarget(obj)**
  Sets the last target to the given serial/alias.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetLastTarget("mount")`

- **Target(obj, [checkrange], [usequeue], [senderserial])**
  Targets the given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `checkrange`: Not specified - See description for usage. · `usequeue`: Not specified - See description for usage. · `senderserial`: Not specified - See description for usage.
  `Target("self")`

- **TargetByResource(toolobj, resourcetype)**
  Uses tool and targets specified resource type (Requires server support (OSI / ServUO))
  `toolobj`: An entity serial in integer or hex format, or an alias string such as "self". · `resourcetype`: String value - See description for usage. See Also: [TargetResourceType](#TargetResourceType)
  `TargetByResource('pickaxe', 'Ore')`

- **TargetExists([targetexiststype]) -> bool**
  Returns true if a target cursor is displayed and the notoriety matches the supplied value, defaults to 'Any', options are 'Any', 'Beneficial', 'Harmful' or 'Neutral'
  `targetexiststype`: Target type - "harmful", "beneficial", or "neutral".  See Also: [TargetExistsType](#TargetExistsType)
  `if TargetExists("Harmful"):`

- **TargetGround(obj, [hue], [range])**
  Target the specified type on the ground, optional parameters for hue and distance.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any. · `range`: Range, ie 10.
  `TargetGround(0x190, -1, 10)`

- **TargetTileOffset(xoffset, yoffset, zoffset, [itemid])**
  Targets the tile at the given offsets relative to the player
  `xoffset`: X Coordinate offset. · `yoffset`: Y Coordinate offset. · `zoffset`: Y Coordinate offset. · `itemid`: ItemID / Graphic such as  0x3db.

- **TargetTileOffsetResource(xoffset, yoffset, zoffset, [itemid])**
  Targets the tile at the given offsets relative to the player (automatically targeting trees/cave tiles/water if present)
  `xoffset`: X Coordinate offset. · `yoffset`: Y Coordinate offset. · `zoffset`: Y Coordinate offset. · `itemid`: ItemID / Graphic such as  0x3db.
  `TargetTileOffsetResource(0, -1, 0)`

- **TargetTileRelative(obj, distance, [reverse], [itemid])**
  Target tile the given distance relative to the specified alias/serial, optional boolean for reverse mode.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `reverse`: True/False value, see description for usage. · `itemid`: ItemID / Graphic such as  0x3db.
  `TargetTileRelative("self", 1, False)`

- **TargetType(obj, [hue], [range])**
  Target specified type in player backpack, optional parameters for hue and search level.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any. · `range`: Range, ie 10.
  `TargetType(0xff, 0, 3)`

- **TargetXYZ(x, y, z, [itemid])**
  Targets the ground at the given coordinates.
  `x`: X Coordinate. · `y`: Y Coordinate. · `z`: Z Coordinate. · `itemid`: ItemID / Graphic such as  0x3db.
  `TargetXYZ(1000, 1000, 0)`

- **WaitForTarget([timeout]) -> bool**
  Wait for target packet from server, optional timeout parameter (default 5000 milliseconds).
  `timeout`: Timeout specified in milliseconds.
  `WaitForTarget(5000)`

- **WaitForTargetOrFizzle(timeout) -> bool**
  Waits the specified timeout for target cursor whilst returning false if the spell is fizzled / uncastable beforehand.
  `timeout`: Timeout specified in milliseconds.
  `WaitForTargetOrFizzle(5000)`

- **WaitingForTarget() -> bool**
  Returns true whenever the core is internally waiting for a server target
  `if WaitingForTarget():`

- **TargetBodyType()**

- **TargetDistance()**

- **TargetExistsType()**

- **TargetInfliction()**

- **TargetNotoriety()**

- **TargetResourceType()**

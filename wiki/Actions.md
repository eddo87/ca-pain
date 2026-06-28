# Actions

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Actions) · 27 commands

- **Attack(obj)**
  Attack mobile (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `Attack("last")`

- **BandageSelf() -> bool**
  Applies a bandage to the player.
  `BandageSelf()`

- **ClearHands([hand])**
  Clear hands, "left", "right", or "both"
  `hand`: Hand - "left", "right", or "both".
  `ClearHands("both")`

- **ClearUseOnce()**
  Clear UseOnce list.
  `ClearUseOnce()`

- **ClickObject(obj)**
  Single click object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `ClickObject("last")`

- **Contents(obj) -> int**
  Returns the item count for given container.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if Contents("backpack") > 120:`

- **ContextMenu(obj, entry)**
  Request a context menu option.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `entry`: Context menu entry index number.
  `ContextMenu(0x00aabbcc, 1)`

- **EquipItem(obj, layer)**
  Equip a specific item into a given layer. Use object inspector to determine layer value.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `layer`: String representing a layer, such as "OneHanded" or "Talisman" etc. See Also: [Layer](#Layer)
  `EquipItem("axe", "TwoHanded")`

- **EquipLastWeapon()**
  Send quick switch weapon packet (probably not supported on pre-AoS servers.
  `EquipLastWeapon()`

- **EquipType(id, layer)**
  Equip a specific type into a given layer. Use object inspector to determine layer value.
  `id`: ItemID / Graphic such as  0x3db. · `layer`: String representing a layer, such as "OneHanded" or "Talisman" etc. See Also: [Layer](#Layer)
  `EquipType(0xff, "TwoHanded")`

- **Feed(obj, graphic, [amount], [hue])**
  Feed a given alias or serial with graphic.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `graphic`: ItemID / Graphic such as  0x3db. · `amount`: Integer representing an amount, ie 10. · `hue`: Item Hue or -1 for any.
  `Feed("mount", 0xff)`

- **FindLayer(layer, [obj]) -> bool**
  Returns true and updates found alias if an item exists in the specified layer, option serial/alias for mobile to check.
  `layer`: String representing a layer, such as "OneHanded" or "Talisman" etc. See Also: [Layer](#Layer) · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if FindLayer("OneHanded"):`

- **InRegion(attribute, obj) -> bool**
  Returns true if the region of the target has the specified attribute.
  `attribute`: String value - See description for usage. See Also: [RegionAttributes](#RegionAttributes) · `obj`: An entity serial in integer or hex format, or an alias string such as "self".
  `if InRegion("Guarded", "self")`

- **Ping() -> long**
  Retrieve an approximated ping with server. -1 on failure.
  `Ping()`

- **Rename(obj, name)**
  Sends rename request.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `name`: String representing a name, ie "Snoopy".
  `Rename("mount", "Snoopy")`

- **ShowNames(showtype)**
  Display corpses and/or mobiles names (parameter "mobiles" or "corpses".
  `showtype`: Show type - "mobiles" or "corpses". See Also: [ShowNamesType](#ShowNamesType)
  `ShowNames("corpses")`

- **ToggleMounted()**
  Unmounts if mounted, or mounts if unmounted, will prompt for mount if no "mount" alias.
  `ToggleMounted()`

- **UseObject(obj, [skipqueue])**
  Sends use (doubleclick) request for given object (parameter can be serial or alias).
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `skipqueue`: Not specified - See description for usage.
  `UseObject("mount")`

- **UseOnce(graphic, [hue]) -> bool**
  Use a specific item type (graphic) from your backpack, only once
  `graphic`: ItemID / Graphic such as  0x3db. · `hue`: Item Hue or -1 for any.
  `UseOnce(0xff)`

- **UseTargetedItem(item, target)**
  Uses specified item and targets target in one action. Requires server support (OSI / ServUO)
  `item`: An entity serial in integer or hex format, or an alias string such as "self". · `target`: An entity serial in integer or hex format, or an alias string such as "self".
  `UseTargetedItem('bandage', 'pet')`

- **UseType(type, [hue], [container], [skipqueue])**
  Sends use (doubleclick) request for given type, optional parameters of hue and container object (defaults to player backpack) (parameters can be serial or alias).
  `type`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any. · `container`: An entity serial in integer or hex format, or an alias string such as "self". · `skipqueue`: Not specified - See description for usage.
  `UseType(0xff)`

- **WaitForContents(obj, [timeout]) -> bool**
  Wait for container contents for given container.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `timeout`: Timeout specified in milliseconds.
  `WaitForContents("backpack", 5000)`

- **WaitForContext(obj, entry, timeout) -> bool**
  Request or wait for a context menu option.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `entry`: Context menu entry index number. · `timeout`: Timeout specified in milliseconds.

- **WaitForContext(obj, entryname, timeout) -> bool**
  Request or wait for a context menu option.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `timeout`: Timeout specified in milliseconds.

- **Layer()**

- **RegionAttributes()**

- **ShowNamesType()**

# Movement

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Movement) · 11 commands

- **Follow([obj])**
  Instructs ClassicUO to follow the specified alias/serial, supply no parameter to cancel
  `obj`: An entity serial in integer or hex format, or an alias string such as "self".

- **Following() -> bool**
  Returns True if currently following a target

- **Pathfind(obj, [checkdistance], [desireddistance]) -> bool**
  Requests client to pathfind to given coordinates / entity
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `checkdistance`: Not specified - See description for usage. · `desireddistance`: Not specified - See description for usage.

- **Pathfind(x, y, z, [checkdistance], [desireddistance]) -> bool**
  Requests client to pathfind to given coordinates / entity
  `x`: X Coordinate. · `y`: Y Coordinate. · `z`: Z Coordinate. · `checkdistance`: Not specified - See description for usage. · `desireddistance`: Not specified - See description for usage.

- **Pathfinding() -> bool**
  Returns True if ClassicUO is currently pathfinding

- **Run(direction) -> bool**
  Run in the given direction.
  `direction`: Direction, ie "West". See Also: [Direction](#Direction)
  `Run("east")`

- **SetForceWalk()**
  Set force walk, True or False
  `SetForceWalk(True)`

- **ToggleForceWalk()**
  Toggle Force Walk
  `ToggleForceWalk()`

- **Turn(direction)**
  Turn in the given direction.
  `direction`: Direction, ie "West". See Also: [Direction](#Direction)
  `Turn("east")`

- **Walk(direction) -> bool**
  Walk in the given direction.
  `direction`: Direction, ie "West".
  `Walk("east")`

- **Direction()**

# Timers

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Timers) · 6 commands

- **CreateTimer(name)**
  Create a new named timer.
  `name`: Timer name.
  `CreateTimer("shmoo")`

- **RemoveTimer(name)**
  Removes the named timer.
  `name`: Timer name.
  `RemoveTimer("shmoo")`

- **SetTimer(name, [milliseconds])**
  Set a timer value and create in case it does not exist.
  `name`: An entity serial in integer or hex format, or an alias string such as "self".
  `SetTimer("shmoo", 0)`

- **Timer(name) -> long**
  Check for a named timer value.
  `name`: Timer name.
  `if Timer("shmoo") > 10000:`

- **TimerExists(name) -> bool**
  Returns true if the timer exists.
  `name`: Timer name.
  `if TimerExists("shmoo"):`

- **TimerMsg(name)**
  Outputs the elapsed timer value as a SystemMessage
  `name`: Timer name.
  `TimerMsg("shmoo")`

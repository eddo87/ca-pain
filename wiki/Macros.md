# Macros

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Macros) · 6 commands

- **IsRunning(name) -> bool**
  Returns True if the specified macro name is currently running
  `name`: Macro name.
  `if IsRunning('macro'):`

- **PlayCUOMacro(name)**
  Plays the specified CUO macro name
  `name`: Macro name.
  `PlayCUOMacro('Paperdoll')`

- **PlayMacro(name, args)**
  Plays the given macro name.
  `name`: Macro name. · `args`: Comma seperated list of parameters.

- **Replay(args)**
  Replay the current macro
  `args`: Comma seperated list of parameters.
  `Replay()`

- **Stop([name])**
  Stops the current macro.
  `name`: Macro name.

- **StopAll()**
  Stops all running macros including background macros.
  `StopAll()`

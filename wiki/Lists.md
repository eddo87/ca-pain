# Lists

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Lists) · 9 commands

- **ClearList(listname)**
  Clear a list by name.
  `listname`: List name.
  `ClearList("list")`

- **CreateList(listname)**
  Create list with given name, if list already exists, it is overwritten.
  `listname`: List name.
  `CreateList("list")`

- **GetList(listname) -> object[]**
  Returns array of all entries in the list, for use with for loop etc.
  `listname`: List name.
  `GetList("list")`

- **InList(listname, value) -> bool**
  Checks whether a list contains a given element.
  `listname`: List name.
  `if InList("shmoo", 1):`

- **List(listname) -> int**
  Returns the number of entries in the list.
  `listname`: List name.
  `if List("list") < 5:`

- **ListExists(listname) -> bool**
  Returns true if list exist, or false if not.
  `listname`: List name.
  `if ListExists("list"):`

- **PopList(listname, [elementvalue]) -> int**
  Remove elements from a list, returns the number of elements removed
  `listname`: List name. · `elementvalue`: Element value to remove from list, or 'front' to remove the first item, or 'back' to remove last entry, default 'back'.

- **PushList(listname, value)**
  Pushes a value to the end of the list, will create list if it doesn't exist.
  `listname`: List name.
  `PushList("list", 1)`

- **RemoveList(listname)**
  Removes the list with the given name.
  `listname`: List name.
  `RemoveList("list")`

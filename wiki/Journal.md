# Journal

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Journal) · 4 commands

- **ClearJournal([buffer])**
  Clear all journal texts.
  `ClearJournal()`

- **InJournal(text, [author], [hue], [timeout], [buffer]) -> bool**
  Check for a text in journal, optional source name.
  `hue`: Item Hue or -1 for any. · `timeout`: Timeout specified in milliseconds.
  `if InJournal("town guards", "system"):`

- **WaitForJournal(text, timeout, [author], [hue]) -> bool**
  Wait the given timeout for the journal text to appear.
  `timeout`: Timeout specified in milliseconds. · `hue`: Item Hue or -1 for any.
  `if WaitForJournal("town guards", 5000, "system"):`

- **WaitForJournal(entries, timeout, [author]) -> tuple**
  Wait up the given timeout for one of any of provided array of string to appear in journal
  `entries`: An array of strings. · `timeout`: Timeout specified in milliseconds.

# Trade

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Trade) · 5 commands

- **TradeAccept()**
  Accepts the current trade window
  `TradeAccept()`

- **TradeClose()**
  Closes the current trade window
  `TradeClose()`

- **TradeCurrency()**
  Sets the gold and platinum in the trade window (for shards that support it)
  `TradeCurrency(60000, 1)`

- **TradeReject()**
  Rejects (unticks) the current trade window
  `TradeReject()`

- **WaitForTradeWindow([timeout]) -> bool**
  Waits the specified number of milliseconds for trade window action, -1 for infinite
  `timeout`: Timeout specified in milliseconds.
  `WaitForTradeWindow(5000)`

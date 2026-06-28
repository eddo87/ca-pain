# Messages

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Messages) · 13 commands

- **AllyMsg(message)**
  Sends given message to alliance chat.
  `AllyMsg("alert")`

- **CancelPrompt()**
  Cancels the current prompt.
  `CancelPrompt()`

- **ChatMsg(message)**
  Sends a chat message.
  `ChatMsg("Mary had a little lamb")`

- **EmoteMsg(message)**
  Emotes the given message
  `EmoteMsg("hi")`

- **GetText(prompt, [timeout]) -> tuple**
  Sends an internal prompt request and returns the text entered
  `timeout`: Timeout specified in milliseconds.

- **GuildMsg(message)**
  Sends given message to guild chat.
  `GuildMsg("alert")`

- **HeadMsg(message, [obj], [hue])**
  Displays overhead message above given mobile / item.
  `obj`: An entity serial in integer or hex format, or an alias string such as "self". · `hue`: Item Hue or -1 for any.
  `HeadMsg("hi", "backpack")`

- **Msg(message, [hue])**
  Speaks the given message, Optional hue
  `hue`: Item Hue or -1 for any.
  `Msg("hi")`

- **PartyMsg(message)**
  Sends given message to party chat.
  `PartyMsg("alert")`

- **PromptMsg(message)**
  Sends the specified message as a prompt response
  `PromptMsg("hello")`

- **WaitForPrompt(timeout) -> bool**
  Wait the specified timeout for a prompt packet to be received
  `timeout`: Timeout specified in milliseconds.
  `WaitForPrompt(5000)`

- **WhisperMsg(message)**
  Whispers the given message
  `WhisperMsg("hi")`

- **YellMsg(message)**
  Yells the given message
  `YellMsg("hi")`

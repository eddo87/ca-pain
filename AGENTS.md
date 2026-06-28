# ClassicAssist scripts — agent notes

UO automation scripts for **ClassicAssist** (CA), the ClassicUO assistant. Repo: `eddo87/ca-pain`.

## Runtime
- Scripts run in CA's **IronPython 2.7** (Python 2 syntax: `except Exception, e` style works, `print` is useless — use `SysMessage`).
- .NET is reachable: `from Assistant import Engine`, `from System.Net import WebClient`, etc.
- API reference: the **CA wiki** (`github.com/Reetus/ClassicAssist/wiki`) — pages: Macro-Commands, Entity, Targeting, Spells, Journal, Actions, Aliases. Data files in `../Data/` (BuffIcons.json, Spells.json, Properties.json) define valid names.

## How scripts are stored / run (important)
- CA macros live **inline in `../Profiles/settings.json`** as escaped JSON strings. CA **rewrites that file from memory on save/exit** — if you hand-edit settings.json while CA is open, it gets clobbered. Close CA first.
- Preferred: keep code in a `.py` here and use a one-line macro stub `execfile(r"C:\...\Scripts\name.py")`. `execfile`/`exec(compile(...))` re-read the file **every run**, so edits need no CA reload.
- Remote auto-update: `focus_loader.py` fetches `focus_receiver.py` from GitHub raw and `exec`s it (`WebClient` + `ServicePointManager.SecurityProtocol = Tls12`). Raw CDN caches ~5 min.

## Gotchas (learned the hard way)
- **Pause() blocks the whole macro.** For multiple concurrent cooldowns use `datetime` timestamps (non-blocking checks) or CA **Timers** (`SetTimer`/`Timer`, persist across runs — needed for hotkey-triggered single-pass scripts since module vars reset each run).
- **Item use:** `UseType(graphic)` only reaches the **top level** of the backpack and spams *"cannot find object type"* for nested items. Use `FindType(g,-1,"backpack")` + `UseObject("found")` to use at any depth. Gate with `CountType(g,"backpack")>0` (silent) so you never search for items you lack.
- **Buff names** (`BuffExists`, `BuffTime`) must match `../Data/BuffIcons.json` **exactly** (case/space sensitive) or you get *"Nome buff sconosciuto"*. e.g. `"Mortal Strike"` ✓, `"Mortal Wound"` ✗; `"Strength"`/`"Agility"` ✓. There is **no** "am I casting" check.
- **Spells:** `Cast(name)` → void (opens cursor); `Cast(name, target)` → bool (auto-targets, e.g. `Cast("Cure","self")`). Names from `../Data/Spells.json` (`"Heal"`, `"Greater Heal"`, `"Cure"`, `"Cleanse by Fire"`). `Skill("Magery")` reads skill value.
- **Stat/status args:** `Hits/MaxHits/DiffHits/Stam/MaxStam/Poisoned/YellowHits/Paralyzed/Mounted` take an entity (`"self"`). `Str()/Dex()/Int()` take **no** arg. `YellowHits("self")` = can't-be-healed (Mortal).
- **Targeting:** `GetEnemy(notorietyList, body, mode)` sets the `enemy` alias and returns a **flag, not the serial** — read the serial with `GetAlias("enemy")`. Notoriety: Innocent/Criminal/Enemy/Murderer/Gray/Ally/Invulnerable. Body: Any/Humanoid/Transformation — **`Humanoid` may exclude gargoyle players**, test before trusting. `SetLastTarget(obj)` has no harmful/beneficial variant. `TargetExists("Harmful"|"Beneficial"|"Neutral"|"Any")`; `Target(obj)` fills an already-open cursor.
- **Aliases** (`SetAlias`/`GetAlias`/`FindAlias`) are **global** scope and persist within a session; script-set ones are not reliably written to disk.
- **Reading chat/journal:** macro `InJournal`/`WaitForJournal` only return bool / the matched search string — they **cannot** give you the line text. Use `Engine.Journal` (a `CircularBuffer<JournalEntry>`): it is **not iterable and has no indexer** — call **`GetEntireBuffer()`** → `JournalEntry[]` (iterable). Each entry: `.Text`, `.Name` (author), `.SpeechType`. (`FindAny` exists but isn't callable from IronPython.)
- **Channel chat format varies by server:** sometimes the author is the real player (`.Name="uno"`, text=`"TARGET ..."`); sometimes it's relayed as `.Name="System"` with the speaker inside the text (`"<Alliance> PASO ADELANTE: TARGET ..."`). Match **both** author and text-parsed speaker; use **exact** name compare (substring matches "uno" inside "Bruno").
- **Overhead vs system text:** `HeadMsg(text, serial, hue)` is transient floating text that only renders if the target is **on the player's screen**. For an always-visible message (off-screen targets), use `SysMessage`.
- **Range:** targeting/`HeadMsg`/`Name()` need the mobile within client view (~18 tiles). CA's own Last Target action already respects the range option.

## Files
| File | Role |
|---|---|
| `autoheal.py` | survival: auto potions (cure/heal/refresh/str/dex + apple on Mortal), datetime cooldowns, loop |
| `panic.py` | single-pass panic potions (apple if life<X & yellow, cure, heal, refresh) |
| `petBall.py` | recall pets via pet balls, walk to range, cure, mount |
| `remount.py` | self-paced auto-remount nearest non-poisoned mount; cures poisoned mount (Cure/Cleanse by Fire) |
| `target_enemy.py` | SELECT nearest Murderer/Enemy (cycle), name overhead, set last target — no broadcast |
| `share_target.py` | broadcast current selection once: `TARGET <name> 0x<serial>` to party/guild/alliance |
| `focus_receiver.py` | read broadcasts (caller allow-list), set last target, announce + banner, optional melee auto-attack |
| `focus_loader.py` | bootstrap that fetches+runs latest `focus_receiver.py` from GitHub |
| `_diag_journal.py` | temp diagnostic: dump journal entries containing a marker (author + speech type) |

## Focus-fire flow
`target_enemy` (cycle) → `share_target` (broadcast once) → teammates run `focus_receiver`/`focus_loader` → everyone's Last Target = the call. Mages cast then press their own Last Target key (receiver only **sets** it; it does not hijack spell cursors).

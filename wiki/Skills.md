# Skills

[Wiki page](https://github.com/Reetus/ClassicAssist/wiki/Skills) · 10 commands

- **SetSkill(skill, status)**
  Sets the lock state of the given skill, up, down or locked.
  `skill`: Skill name. · `status`: Lock Status - "up", "down", or "locked". See Also: [LockStatus](#LockStatus)
  `SetSkill("hiding", "locked")`

- **SetStatus(stat, lockstatus)**
  Sets the lock state of the given stat, up, down or locked.
  `stat`: String value - See description for usage. See Also: [StatType](#StatType) · `lockstatus`: Lock Status - "up", "down", or "locked". See Also: [LockStatus](#LockStatus)
  `SetStatus('str', 'locked')`

- **Skill(name, [baseskill]) -> float**
  Returns the value of the given skill name.
  `name`: Skill name. · `baseskill`: Not specified - See description for usage.
  `if Skill("hiding") < 100:`

- **SkillCap(name) -> float**
  Returns the skill cap for the specified skill
  `name`: Skill name.
  `if SkillCap("Blacksmithy") == 120:`

- **SkillDelta(name) -> float**
  Returns the skill value delta since last reset
  `name`: Skill name.

- **SkillState(name) -> str**
  Returns the lock status of the given skill, up, down, or locked.
  `name`: Skill name.
  `if SkillState("hiding') == "locked":`

- **UseLastSkill()**
  Uses the last invoked skill
  `UseLastSkill()`

- **UseSkill(skill)**
  Invokes the given skill name.
  `skill`: Skill name.
  `UseSkill("Hiding")`

- **LockStatus()**

- **StatType()**

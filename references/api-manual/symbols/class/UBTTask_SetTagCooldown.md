# UBTTask_SetTagCooldown

- Symbol Type: class
- Symbol Path: Others / UBTTask_SetTagCooldown
- Source JSON Path: class/detail/Others/UBTTask_SetTagCooldown.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_SetTagCooldown.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Cooldown task node.
  Sets a cooldown tag value.  Use with cooldown tag decorators to prevent behavior tree execution.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CooldownTag | FGameplayTag | Gameplay tag that will be used for the cooldown. |  |
| bAddToExistingDuration | bool | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |  |
| CooldownDuration | float | Value we will add or set to the Cooldown tag when this task runs. |  |

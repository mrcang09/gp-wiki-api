# UBTDecorator_SetTagCooldown

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_SetTagCooldown
- Source JSON Path: class/detail/Others/UBTDecorator_SetTagCooldown.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_SetTagCooldown.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Set tag cooldown decorator node.
  A decorator node that sets a gameplay tag cooldown.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CooldownTag | FGameplayTag | Gameplay tag that will be used for the cooldown. |  |
| CooldownDuration | float | Value we will add or set to the Cooldown tag when this task runs. |  |
| bAddToExistingDuration | bool | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |  |

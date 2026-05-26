# UBTDecorator_TagCooldown

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_TagCooldown
- Source JSON Path: class/detail/Others/UBTDecorator_TagCooldown.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_TagCooldown.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Cooldown decorator node.
  A decorator node that bases its condition on whether a cooldown timer based on a gameplay tag has expired.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CooldownTag | FGameplayTag | Gameplay tag that will be used for the cooldown. |  |
| CooldownDuration | float | Value we will add or set to the Cooldown tag when this node is deactivated. |  |
| bAddToExistingDuration | bool | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |  |
| bActivatesCooldown | bool | Whether or not we are addingsetting to the cooldown tag's value when the decorator deactivates. |  |

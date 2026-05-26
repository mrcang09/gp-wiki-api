# UBTDecorator_ConeCheck

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_ConeCheck
- Source JSON Path: class/detail/Others/UBTDecorator_ConeCheck.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_ConeCheck.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Cone check decorator node.
  A decorator node that bases its condition on a cone check, using Blackboard entries to form the parameters of the check.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeHalfAngle | float | Angle between cone direction and code cone edge, or a half of the total cone angle |  |
| ConeOrigin | FBlackboardKeySelector | blackboard key selector |  |
| ConeDirection | FBlackboardKeySelector | "None" means "use ConeOrigin's direction" |  |
| Observed | FBlackboardKeySelector | blackboard key selector |  |

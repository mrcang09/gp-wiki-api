# UBTDecorator_KeepInCone

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_KeepInCone
- Source JSON Path: class/detail/Others/UBTDecorator_KeepInCone.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_KeepInCone.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Cooldown decorator node.
  A decorator node that bases its condition on whether the observed position is still inside a cone. The cone's direction is calculated when the node first becomes relevant.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeHalfAngle | float | max allowed time for execution of underlying node |  |
| ConeOrigin | FBlackboardKeySelector | blackboard key selector |  |
| Observed | FBlackboardKeySelector | blackboard key selector |  |
| bUseSelfAsOrigin | uint32 |  |  |
| bUseSelfAsObserved | uint32 |  |  |

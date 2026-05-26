# UBTDecorator_DoesPathExist

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_DoesPathExist
- Source JSON Path: class/detail/Others/UBTDecorator_DoesPathExist.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_DoesPathExist.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Cooldown decorator node.
  A decorator node that bases its condition on whether a path exists between two points from the Blackboard.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlackboardKeyA | FBlackboardKeySelector | blackboard key selector |  |
| BlackboardKeyB | FBlackboardKeySelector | blackboard key selector |  |
| bUseSelf | uint32 |  |  |
| PathQueryType | TEnumAsByte < EPathExistanceQueryType :: Type > |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > | "None" will result in default filter being used |  |

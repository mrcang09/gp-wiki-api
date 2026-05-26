# UKismetAnimationLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetAnimationLibrary
- Source JSON Path: class/detail/Others/UKismetAnimationLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetAnimationLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### K2_TwoBoneIK

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RootPos | FVector &  |  |  |
| JointPos | FVector &  |  |  |
| EndPos | FVector &  |  |  |
| JointTarget | FVector &  |  |  |
| Effector | FVector &  |  |  |
| OutJointPos | FVector &  |  |  |
| OutEndPos | FVector &  |  |  |
| bAllowStretching | bool  |  |  |
| StartStretchRatio | float  |  |  |
| MaxStretchScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_LookAt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurrentTransform | FTransform &  |  |  |
| TargetPosition | FVector &  |  |  |
| LookAtVector | FVector  |  |  |
| bUseUpVector | bool  |  |  |
| UpVector | FVector  |  |  |
| ClampConeInDegree | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

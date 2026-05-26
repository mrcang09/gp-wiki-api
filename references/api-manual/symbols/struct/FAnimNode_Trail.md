# FAnimNode_Trail

- Symbol Type: struct
- Symbol Path: FAnimNode_Trail
- Source JSON Path: cppstruct/detail/FAnimNode_Trail.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Trail.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Trail Controller

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TrailBone | FBoneReference | Reference to the active bone in the hierarchy to modify. |  |
| ChainLength | int32 | Number of bones above the active one in the hierarchy to modify. ChainLength should be at least 2. |  |
| ChainBoneAxis | TEnumAsByte < EAxis :: Type > | Axis of the bones to point along trail. |  |
| bInvertChainBoneAxis | bool | Invert the direction specified in ChainBoneAxis. |  |
| TrailRelaxation_DEPRECATED | float | How quickly we 'relax' the bones to their animated positions. Deprecated. Replaced to TrailRelaxationCurve |  |
| TrailRelaxationSpeed | FRuntimeFloatCurve | How quickly we 'relax' the bones to their animated positions. Time 0 will map to top root joint, time 1 will map to the bottom joint. |  |
| bLimitStretch | bool | Limit the amount that a bone can stretch from its ref-pose length. |  |
| StretchLimit | float | If bLimitStretch is true, this indicates how long a bone can stretch beyond its length in the ref-pose. |  |
| FakeVelocity | FVector | 'Fake' velocity applied to bones. |  |
| bActorSpaceFakeVel | bool | Whether 'fake' velocity should be applied in actor or world space. |  |
| BaseJoint | FBoneReference | Base Joint to calculate velocity from. If none, it will use Component's World Transform. . |  |

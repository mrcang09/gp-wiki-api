# FAnimNode_RotationMultiplier

- Symbol Type: struct
- Symbol Path: FAnimNode_RotationMultiplier
- Source JSON Path: cppstruct/detail/FAnimNode_RotationMultiplier.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotationMultiplier.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Simple controller that multiplies scalar value to the translationrotationscale of a single bone.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetBone | FBoneReference | Name of bone to control. This is the main bone chain to modify from. |  |
| SourceBone | FBoneReference | Source to get transform from |  |
| Multiplier | float |  |  |
| RotationAxisToRefer | TEnumAsByte < EBoneAxis > |  |  |
| bIsAdditive | bool |  |  |

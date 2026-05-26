# FAnimNode_Constraint

- Symbol Type: struct
- Symbol Path: FAnimNode_Constraint
- Source JSON Path: cppstruct/detail/FAnimNode_Constraint.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Constraint.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Constraint node to parent or world transform for rotationtranslation

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneToModify | FBoneReference | Name of bone to control. This is the main bone chain to modify from. |  |
| ConstraintSetup | TArray < FConstraint > | List of constraints |  |
| ConstraintWeights | TArray < float > | Weight data - post edit syncs up to ConstraintSetups |  |

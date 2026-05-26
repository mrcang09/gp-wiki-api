# FAnimNode_CCDIK

- Symbol Type: struct
- Symbol Path: FAnimNode_CCDIK
- Source JSON Path: cppstruct/detail/FAnimNode_CCDIK.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CCDIK.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Controller which implements the CCDIK IK approximation algorithm

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EffectorLocation | FVector | Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location |  |
| EffectorLocationSpace | TEnumAsByte < enum EBoneControlSpace > | Reference frame of Effector Transform. |  |
| EffectorTarget | FBoneSocketTarget | If EffectorTransformSpace is a bone, this is the bone to use. |  |
| TipBone | FBoneReference | Name of tip bone |  |
| RootBone | FBoneReference | Name of the root bone |  |
| Precision | float | Tolerance for final tip location delta from EffectorLocation |  |
| MaxIterations | int32 | Maximum number of iterations allowed, to control performance. |  |
| bStartFromTail | bool | Toggle drawing of axes to debug joint rotation |  |
| bEnableRotationLimit | bool | Tolerance for final tip location delta from EffectorLocation |  |
| RotationLimitPerJoints | TArray < float > | symmetry rotation limit per joint. Index 0 matches with root bone and last index matches with tip bone. |  |

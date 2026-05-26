# FAnimNode_Fabrik

- Symbol Type: struct
- Symbol Path: FAnimNode_Fabrik
- Source JSON Path: cppstruct/detail/FAnimNode_Fabrik.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Fabrik.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EffectorTransform | FTransform | Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location |  |
| EffectorTransformSpace | TEnumAsByte < enum EBoneControlSpace > | Reference frame of Effector Transform. |  |
| EffectorTransformBone_DEPRECATED | FBoneReference | If EffectorTransformSpace is a bone, this is the bone to use. |  |
| EffectorTarget | FBoneSocketTarget | If EffectorTransformSpace is a bone, this is the bone to use. |  |
| EffectorRotationSource | TEnumAsByte < enum EBoneRotationSource > |  |  |
| TipBone | FBoneReference | Name of tip bone |  |
| RootBone | FBoneReference | Name of the root bone |  |
| Precision | float | Tolerance for final tip location delta from EffectorLocation |  |
| MaxIterations | int32 | Maximum number of iterations allowed, to control performance. |  |
| bEnableDebugDraw | bool | Toggle drawing of axes to debug joint rotation |  |

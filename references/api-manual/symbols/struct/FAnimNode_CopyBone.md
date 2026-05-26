# FAnimNode_CopyBone

- Symbol Type: struct
- Symbol Path: FAnimNode_CopyBone
- Source JSON Path: cppstruct/detail/FAnimNode_CopyBone.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBone.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceBone | FBoneReference | Source Bone Name to get transform from |  |
| TargetBone | FBoneReference | Name of bone to control. This is the main bone chain to modify from. |  |
| bCopyTranslation | bool | If Translation should be copied |  |
| bCopyRotation | bool | If Rotation should be copied |  |
| bCopyScale | bool | If Scale should be copied |  |
| ControlSpace | TEnumAsByte < EBoneControlSpace > | Space to convert transforms into prior to copying components |  |

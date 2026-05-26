# FBoneNode

- Symbol Type: struct
- Symbol Path: FBoneNode
- Source JSON Path: cppstruct/detail/FBoneNode.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FBoneNode.json
- Mirrored At (UTC): 2026-05-19 08:24:36Z

---

## Description

Each Bone node in BoneTree

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name_DEPRECATED | FName | Name of bone, this is the search criteria to match with mesh bone. This will be NAME_None if deleted. |  |
| ParentIndex_DEPRECATED | int32 | Parent Index. -1 if not used. The root has 0 as its parent. Do not delete the element but set this to -1. If it is revived by other reason, fix up this link. |  |
| TranslationRetargetingMode | TEnumAsByte < EBoneTranslationRetargetingMode :: Type > | Retargeting Mode for Translation Component. |  |
| PerBoneOverrideRetargetingModeConfig | TMap < FName , TEnumAsByte < EBoneTranslationRetargetingMode :: Type > > |  |  |

# FAnimNode_CopyBoneDelta

- Symbol Type: struct
- Symbol Path: FAnimNode_CopyBoneDelta
- Source JSON Path: cppstruct/detail/FAnimNode_CopyBoneDelta.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBoneDelta.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Simple controller to copy a transform relative to the ref pose to the target bone,
 	instead of the copy bone node which copies the absolute transform

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceBone | FBoneReference |  |  |
| TargetBone | FBoneReference |  |  |
| bCopyTranslation | bool |  |  |
| bCopyRotation | bool |  |  |
| bCopyScale | bool |  |  |
| CopyMode | CopyBoneDeltaMode |  |  |
| TranslationMultiplier | float |  |  |
| RotationMultiplier | float |  |  |
| ScaleMultiplier | float |  |  |

# FAnimNode_BlendBoneByChannel

- Symbol Type: struct
- Symbol Path: FAnimNode_BlendBoneByChannel
- Source JSON Path: cppstruct/detail/FAnimNode_BlendBoneByChannel.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendBoneByChannel.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FPoseLink |  |  |
| B | FPoseLink |  |  |
| Alpha | float |  |  |
| AlphaScaleBias | FInputScaleBias |  |  |
| BoneDefinitions | TArray < FBlendBoneByChannelEntry > |  |  |
| TransformsSpace | TEnumAsByte < EBoneControlSpace > | Space to convert transforms into prior to copying channels |  |
| InternalBlendAlpha | float |  |  |
| bBIsRelevant | bool |  |  |
| ValidBoneEntries | TArray < FBlendBoneByChannelEntry > |  |  |

# FAnimNode_BlendListBase

- Symbol Type: struct
- Symbol Path: FAnimNode_BlendListBase
- Source JSON Path: cppstruct/detail/FAnimNode_BlendListBase.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendListBase.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlendPose | TArray < FPoseLink > |  |  |
| BlendTime | TArray < float > |  |  |
| TransitionType | EBlendListTransitionType |  |  |
| BlendType | EAlphaBlendOption |  |  |
| CustomBlendCurve | UCurveFloat * |  |  |
| BlendProfile | UBlendProfile * |  |  |
| ResetFrameCountSubValue | int32 |  |  |
| LastFrameCount | uint64 |  |  |
| Blends | TArray < struct FAlphaBlend > |  |  |
| BlendWeights | TArray < float > |  |  |
| RemainingBlendTimes | TArray < float > |  |  |
| LastActiveChildIndex | int32 |  |  |
| PerBoneSampleData | TArray < FBlendSampleData > |  |  |
| bResetChildOnActivation | bool | This reinitializes child pose when re-activated. For example, when active child changes |  |
| bResetChildOnBlendListChange | bool |  |  |

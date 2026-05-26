# FAnimMontageInstance

- Symbol Type: struct
- Symbol Path: FAnimMontageInstance
- Source JSON Path: cppstruct/detail/FAnimMontageInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimMontageInstance.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |
| MontageNoGCID | int64 |  |  |
| bPlaying | bool |  |  |
| DefaultBlendTimeMultiplier | float |  |  |
| IgnoreNotifyType | TArray < FString > |  |  |
| CustomSectionsPlayInfo | TArray < FMontageSectionsPlayInfo > |  |  |
| NextSections | TArray < int32 > |  |  |
| PrevSections | TArray < int32 > |  |  |
| ActiveStateBranchingPoints | TArray < FAnimNotifyEvent > | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |  |
| Position | float |  |  |
| PlayRate | float |  |  |
| Blend | FAlphaBlend |  |  |
| DisableRootMotionCount | int32 |  |  |
| RandomJumpTimes | int32 |  |  |

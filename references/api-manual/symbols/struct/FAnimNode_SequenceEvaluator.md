# FAnimNode_SequenceEvaluator

- Symbol Type: struct
- Symbol Path: FAnimNode_SequenceEvaluator
- Source JSON Path: cppstruct/detail/FAnimNode_SequenceEvaluator.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SequenceEvaluator.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sequence | UAnimSequenceBase * |  |  |
| ExplicitTime | float |  |  |
| ExplicitTimeType | TEnumAsByte < ESequenceEvalTimeType :: Type > | 输入时间类型： |  |
| bShouldLoop | bool | This only works if bTeleportToTargetTime is false OR this node is set to use SyncGroup |  |
| bTeleportToExplicitTime | bool | If true, teleport to explicit time, does NOT advance time (does not trigger notifies, does not extract Root Motion, etc.)<br>	Note: using a sync group forces advancing time regardless of what this option is set to. |  |
| StartPosition | float |  |  |
| ReinitializationBehavior | TEnumAsByte < ESequenceEvalReinit :: Type > | What to do when SequenceEvaluator is reinitialized |  |
| bReinitialized | bool |  |  |
| CheckReTickFrameCounterSubValue | int32 |  |  |
| bEnableTriggerNotify | bool |  |  |

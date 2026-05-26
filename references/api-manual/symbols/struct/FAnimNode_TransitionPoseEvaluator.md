# FAnimNode_TransitionPoseEvaluator

- Symbol Type: struct
- Symbol Path: FAnimNode_TransitionPoseEvaluator
- Source JSON Path: cppstruct/detail/FAnimNode_TransitionPoseEvaluator.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TransitionPoseEvaluator.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Animation data node for state machine transitions.
  Can be set to supply either the animation data from the transition source (From State) or the transition destination (To State).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DataSource | TEnumAsByte < EEvaluatorDataSource :: Type > |  |  |
| EvaluatorMode | TEnumAsByte < EEvaluatorMode :: Mode > |  |  |
| FramesToCachePose | int32 |  |  |
| CacheFramesRemaining | int32 |  |  |

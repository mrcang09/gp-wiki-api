# FAnimNode_SubInstance

- Symbol Type: struct
- Symbol Path: FAnimNode_SubInstance
- Source JSON Path: cppstruct/detail/FAnimNode_SubInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SubInstance.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPose | FPoseLink | Input pose for the node, intentionally not accessible because if there's no input<br>	   Node in the target class we don't want to show this as a pin |  |
| InPoses | TArray < FPoseLink > | Each layer's blended pose |  |
| SubInstanceSlotName | FName |  |  |
| InstanceClass | TSubclassOf < UAnimInstance > |  |  |
| bNeedCacheSubInstance | bool |  |  |
| MaxCacheSubInstanceCount | int32 |  |  |
| bResetToAdditivePose | bool |  |  |
| InstanceToRun | UAnimInstance * | This is the actual instance allocated at runtime that will run |  |
| InstancePendingToRun | UAnimInstance * |  |  |
| MultiInstancesToRunDatas | TArray < FMultiSubInstanceData > |  |  |
| BlendOutInstanceDatas | TArray < FSubInstanceBlendData > |  |  |
| InstanceProperties | TArray < UProperty * > | List of properties on the calling instance to push from |  |
| SubInstanceProperties | TArray < UProperty * > | List of properties on the sub instance to push to, built from name list when initialised |  |
| SourcePropertyNames | TArray < FName > | List of source properties to use, 1-1 with Dest names below, built by the compiler |  |
| DestPropertyNames | TArray < FName > | List of destination properties to use, 1-1 with Source names above, built by the compiler |  |
| PosInertialization | FAnimNode_SubAnimInertialization |  |  |
| bBlendSubAnim | bool |  |  |
| NewAnimBlendTime | float |  |  |
| bKeepUpdateOldSubInstanes | bool |  |  |
| bUpdateWhenNotRelevant | bool |  |  |
| NotRelevantUpdateConditions | TArray < UAnimInstanceUpdateCondition * > |  |  |
| bAlwaysUpdateInputNode | bool |  |  |
| bResetInertializationWhenReactive | bool |  |  |
| bUpdateAllInputNodeWhenNoInstanceRun | bool |  |  |
| bResetPendingBlendDurationWhenReactive | bool |  |  |

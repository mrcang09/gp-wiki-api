# UAnimInstance

- Symbol Type: class
- Symbol Path: Others / UAnimInstance
- Source JSON Path: class/detail/Others/UAnimInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimInstance.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurrentSkeleton | USkeleton * | This is used to extract animation. If Mesh exists, this will be overwritten by Mesh->Skeleton |  |
| RootMotionMode | TEnumAsByte < ERootMotionMode :: Type > |  |  |
| bRunUpdatesInWorkerThreads_DEPRECATED | bool | DEPRECATED: No longer used.<br>	  Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. this requires certain conditions to be met:<br>	  - All access of variables in the blend tree should be a direct access of a member variable<br>	  - No BlueprintUpdateAnimation event should be used (i.e. the event graph should be empty). Only native update is permitted. |  |
| bCanUseParallelUpdateAnimation_DEPRECATED | bool | DEPRECATED: No longer used.<br>	  Whether we can use parallel updates for our animations.<br>	  Conditions affecting this include:<br>	  - Use of BlueprintUpdateAnimation<br>	  - Use of non 'fast-path' EvaluateGraphExposedInputs in the node graph |  |
| bUseMultiThreadedAnimationUpdate | bool | Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. This flag is propagated from the UAnimBlueprint to this instance by the compiler.<br>	  The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded<br>	  Animation Update" should be set. |  |
| bWarnAboutBlueprintUsage_DEPRECATED | bool | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |  |
| bBlueprintSkipUpdate | bool |  |  |
| bUseBlueprintUpdateAnimation | uint8 |  |  |
| bUseBlueprintPostEvaluateAnimation | uint8 |  |  |
| AnimAssets_NoGCRef | TMap < int64 , UAnimationAsset * > |  |  |
| bQueueMontageEvents | bool | True when Montages are being ticked, and Montage Events should be queued.<br>	  When Montage are being ticked, we queue AnimNotifies and Events. We trigger notifies first, then Montage events. |  |
| ForbiddenPlayMontageSlot | TArray < FString > |  |  |
| ActiveAnimNotifyState | TArray < FAnimNotifyEvent > | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |  |
| bNeedUpdateNotAttributeCurve | bool | 此动画蓝图是否需要更新非Attribute的Curve数据 |  |
| RefCachedSubAnimInstances | TArray < UAnimInstance * > |  |  |
| bIsOnlyMasterTriggerNotify | bool |  |  |
| bIsMaster | bool |  |  |
| bDynamicDisableBoneRetarget | bool |  |  |
| CopyPoseFromSkelComp | USkeletalMeshComponent * |  |  |
| BoneRetargetSource | FName |  |  |
| bUseBoneStateDirtyFeature | bool |  |  |
| bBoneStateDirty | bool |  |  |
| C_InverseRetargetIgnoreBoneList | TArray < int32 > |  |  |
| FollowedAnimInstance | UAnimInstance * | 记录被跟随者的动画实例   当该指针为nullptr时，代表启用了自身 Proxy 的 Follow 轨道(即FollowGroupArrays开始记录) |  |
| FollowerAnimInstances | TArray < TWeakObjectPtr < UAnimInstance > > |  |  |
| ParentAnimInstance | TWeakObjectPtr < UAnimInstance > |  |  |
| SubAnimInstances | TArray < TWeakObjectPtr < UAnimInstance > > |  |  |
| SubAnimInstancesTempRef | TArray < UAnimInstance * > |  |  |
| CachedSwitchNotifySequence | TArray < UAnimSequenceBase * > |  |  |
| CachedBoneTransformInfoIndex | int64 |  |  |
| CachedBoneTransformMapAsync | TMap < FName , FCachedBoneTransformInfo > |  |  |
| CachedBoneTransformMapInGame | TMap < FName , FCachedBoneTransformInfo > |  |  |
| bIsInPoseUpdate | bool |  |  |
| bEnableBoneCacheInGameThread | bool |  |  |
| bEnableFastPathExposedNodeTree | bool |  |  |
| UpdateConditions | TArray < UAnimInstanceUpdateCondition * > |  |  |
| bCheckUpdateConditionResult | bool |  |  |
| bEnableAnimBlueprintSkeletonDifferFromMeshSkeleton | bool |  |  |
| bEnableFilterForceTriggerNotifyWhenMontageJumpTick | bool |  |  |
| MultiSubInstanceTransferDefaultPoseIndex | int32 |  |  |
| bEnableTriggerAnimNotify | bool |  |  |
| InitNodeSourcePropertyLookupTable | TMap < FName , UProperty * > |  |  |
| bParentPoseOverride | bool |  |  |
| bAutoCopyPose | bool |  |  |
| bHasAvatarSlotEvent | bool |  |  |
| bRestoreSlotVar | bool |  |  |
| bSkipSlotRelevanceCheckForNotifies | bool |  |  |
| bEnableAsyncAnimInstance | bool |  |  |
| bCanCopyRequiredBones | bool |  |  |
| PostCompileValidationClassName | FSoftClassPath | Name of Class to do Post Compile Validation.<br>	 See Class UAnimBlueprintPostCompileValidation. |  |
| BoneRetargetBaseRefMesh | USkeletalMesh * |  |  |

## Functions

### TryGetPawnOwner

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn * |  |  |

### SavePoseSnapshot

Takes a snapshot of the current skeletal mesh component pose & saves it internally.
	  This snapshot can then be retrieved by name in the animation blueprint for blending.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SnapshotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SnapshotPose

Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Snapshot | FPoseSnapshot & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOwningActor

Returns the owning actor of this AnimInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### GetOwningComponent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USkeletalMeshComponent * |  |  |

### BlueprintShouldSkipUpdateAnimation

Executed before the Animation is updated, Check custom condition, whether to skip update

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTimeX | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BlueprintInitializeAnimation

Executed when the Animation is initialized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BlueprintUnInitializeAnimation

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BlueprintUpdateAnimation

Executed when the Animation is updated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTimeX | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BlueprintPostEvaluateAnimation

Executed after the Animation is evaluated

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BlueprintBeginPlay

Executed when begin play is called on the owning component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PlaySlotAnimation

SlotAnimation
	 
	 DEPRECATED. Use PlaySlotAnimationAsDynamicMontage instead, it returns the UAnimMontage created instead of time, allowing more control 
	 Play normal animation asset on the slot node. You can only play one asset (whether montage or animsequence) at a time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Asset | UAnimSequenceBase *  |  |  |
| SlotNodeName | FName  |  |  |
| BlendInTime | float  |  |  |
| BlendOutTime | float  |  |  |
| InPlayRate | float  |  |  |
| LoopCount | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### PlaySlotAnimationAsDynamicMontage

Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Asset | UAnimSequenceBase *  |  |  |
| SlotNodeName | FName  |  |  |
| BlendInTime | float  |  |  |
| BlendOutTime | float  |  |  |
| InPlayRate | float  |  |  |
| LoopCount | int32  |  |  |
| BlendOutTriggerTime | float  |  |  |
| InTimeToStartMontageAt | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimMontage *  |  |  |

### PlaySlotAnimationAsDynamicMontageCustom

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Asset | UAnimSequenceBase *  |  |  |
| SlotNodeName | FName  |  |  |
| Extra | FCustomMontageAnimInfo  |  |  |
| BlendInTime | float  |  |  |
| BlendOutTime | float  |  |  |
| InPlayRate | float  |  |  |
| LoopCount | int32  |  |  |
| BlendOutTriggerTime | float  |  |  |
| InTimeToStartMontageAt | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimMontage *  |  |  |

### SetMatineeAnimPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetMontage | UAnimMontage *  |  |  |
| InPosition | float  |  |  |
| Extra | FCustomMontageAnimInfo  |  |  |
| Weight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopSlotAnimation

Stops currently playing slot animation slot or all

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendOutTime | float  |  |  |
| SlotNodeName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsPlayingSlotAnimation

Return true if it's playing the slot animation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Asset | UAnimSequenceBase *  |  |  |
| SlotNodeName | FName  |  |  |
| bcheckTransientPackage | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ForceTriggerAnimEndedEvent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMontageCustomSectionsPlayInfo

AnimMontage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| InPlayInfo | TArray < FMontageSectionsPlayInfo > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMontageCustomSectionsPlayInfo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_Play

Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MontageToPlay | UAnimMontage *  |  |  |
| InPlayRate | float  |  |  |
| ReturnValueType | EMontagePlayReturnType  |  |  |
| InTimeToStartMontageAt | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Montage_CustomPlay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MontageToPlay | UAnimMontage *  |  |  |
| Extra | FCustomMontageAnimInfo  |  |  |
| InPlayRate | float  |  |  |
| ReturnValueType | EMontagePlayReturnType  |  |  |
| InTimeToStartMontageAt | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Montage_Stop

Stops the animation montage. If reference is NULL, it will stop ALL active montages.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendOutTime | float  |  |  |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_StopBySlot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendOutTime | float  |  |  |
| SlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_CustomStop

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendOutTime | float  |  |  |
| Extra | FCustomMontageAnimInfo  |  |  |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_Pause

Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_Resume

Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_JumpToSection

Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SectionName | FName  |  |  |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_JumpToSectionsEnd

Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SectionName | FName  |  |  |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_SetNextSection

Relink new next section AFTER SectionNameToChange in run-time
	 	You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
	 	use this function to relink the next section
	 	For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
	 	next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SectionNameToChange | FName  | : This should be the name of the Montage Section after which you want to insert a new next section |  |
| NextSection | FName  | : new next section |  |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_SetPlayRate

Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| NewPlayRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_ReversePlayByAbsRateAndSlot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FName  |  |  |
| AbsPlayRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_SetDelayFrame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| DelayFrame | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_IsActive

Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Montage_IsPlaying

Returns true if the animation montage is currently active and playing.
	If reference is NULL, it will return true is ANY montage is currently active and playing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Montage_IsExisting

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### MontageGroup_IsPlaying

判断有无某个组下的蒙太奇正在播放

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GroupName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Montage_GetCurrentSection

Returns the name of the current animation montage section.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### Montage_GetPosition

Get Current Montage Position

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Montage_SetPosition

Set position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| NewPosition | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Montage_GetIsStopped

return true if Montage is not currently active. (not valid or blending out)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Montage_GetBlendTime

Get the current blend time of the Montage.
	If Montage reference is NULL, it will return the current blend time on the first active Montage found.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Montage_GetPlayRate

Get PlayRate for Montage.
	If Montage is not playing, 0 is returned.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### IsAnyMontagePlaying

Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetCurrentActiveMontage

Get a current Active Montage in this AnimInstance.
		Note that there might be multiple Active at the same time. This will only return the first active one it finds.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimMontage * |  |  |

### GetCurrentActiveMontages

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FAnimMontageInstance > |  |  |

### GetCurMontageBySlot

Get the UAnimMontage currently running that matches this SlotName.  Will return NULL if no instance is found.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimMontage *  |  |  |

### Montage_GetNextSection

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| SectionName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### AddAnimAssetNoGCRef

添加动画资源到非GC引用列表，返回全局唯一ID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimAsset | UAnimationAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### RemoveAnimAssetNoGCRef

从非GC引用列表移除动画资源（通过ID）

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimAssetNoGCID | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveAllAnimAssetNoGCRef

从非GC引用列表移除所有动画资源（通过资源指针）

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimAsset | UAnimationAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAnimAssetsNoGCReferences

清空非GC引用列表

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopAllMontages

Stop all montages that are active

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlendOut | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAllMontages

Stop all montages that are active

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlendOut | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearStoppedMontageInstances

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bClearSubAnim | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetForbiddenPlayMontageSlot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FString > |  |  |

### SetForbiddenPlayMontageSlot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsAdd | bool  |  |  |
| SlotName | FString | should be GroupName + SlotName |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRootMotionMode

Set RootMotionMode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | TEnumAsByte < ERootMotionMode :: Type > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInstanceAssetPlayerLength

NOTE: Derived anim getters
	 
	  Anim getter functions can be defined for any instance deriving UAnimInstance.
	  To do this the function must be marked BlueprintPure, and have the AnimGetter metadata entry set to
	  "true". Following the instructions below, getters should appear correctly in the blueprint node context
	  menu for the derived classes
	 
	  A context string can be provided in the GetterContext metadata and can contain any (or none) of the
	  following entries separated by a pipe (|)
	  Transition  - Only available in a transition rule
	  AnimGraph   - Only available in an animgraph (also covers state anim graphs)
	  CustomBlend - Only available in a custom blend graph
	 
	  Anim getters support a number of automatic parameters that will be baked at compile time to be passed
	  to the functions. They will not appear as pins on the graph node. They are as follows:
	  AssetPlayerIndex - Index of an asset player node to operate on, one getter will be added to the blueprint action list per asset node available
	  MachineIndex     - Index of a state machine in the animation blueprint, one getter will be added to the blueprint action list per state machine
	  StateIndex       - Index of a state inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per state
	  TransitionIndex  - Index of a transition inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per transition
	 
	  Gets the length in seconds of the asset referenced in an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceAssetPlayerTime

Get the current accumulated time in seconds for an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SetInstanceAssetPlayerTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32  |  |  |
| time | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNodeIndexWithTag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NodeTag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetInstanceAssetPlayerTime_BP

Get the current accumulated time in seconds for an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SetInstanceAssetPlayerTime_BP

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32  |  |  |
| time | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInstanceAssetPlayerTimeFraction

Get the current accumulated time as a fraction for an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceAssetPlayerTimeFromEnd

Get the time in seconds from the end of an animation in an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceAssetPlayerTimeFromEndFraction

Get the time as a fraction of the asset length of an animation in an asset player node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetPlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceMachineWeight

Get the blend weight of a specified state machine

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceStateWeight

Get the blend weight of a specified state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceCurrentStateElapsedTime

Get the current elapsed time of a state within the specified state machine

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceTransitionCrossfadeDuration

Get the crossfade duration of a specified transition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| TransitionIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceTransitionTimeElapsed

Get the elapsed time in seconds of a specified transition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| TransitionIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInstanceTransitionTimeElapsedFraction

Get the elapsed time as a fraction of the crossfade duration of a specified transition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| TransitionIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRelevantAnimTimeRemaining

Get the time remaining in seconds for the most relevant animation in the source state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32  |  |  |
| NullAnimDefaultValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRelevantAnimTimeRemainingFraction

Get the time remaining as a fraction of the duration for the most relevant animation in the source state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32  |  |  |
| NullAnimDefaultValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRelevantAnimLength

Get the length in seconds of the most relevant animation in the source state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32  |  |  |
| NullAnimDefaultValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRelevantAnimTime

Get the current accumulated time in seconds for the most relevant animation in the source state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32  |  |  |
| NullAnimDefaultValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRelevantAnimTimeFraction

Get the current accumulated time as a fraction of the length of the most relevant animation in the source state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32  |  |  |
| StateIndex | int32  |  |  |
| NullAnimDefaultValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetCurveValue

Returns the value of a named curve.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurveName | FName  |  |  |
| Immediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetCurrentStateName

Returns the name of a currently active state in a state machine.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MachineIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### SetMorphTarget

Sets a morph target to a certain weight.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MorphTargetName | FName  |  |  |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMorphTargets

Clears the current morph targets.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CalculateDirection

Returns degree of the angle betwee velocity and Rotation forward vector
	  The range of return will be from [-180, 180], and this can be used to feed blendspace directional value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Velocity | FVector &  |  |  |
| BaseRotation | FRotator & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### LockAIResources

locks indicated AI resources of animated pawn
	 	DEPRECATED. Use LockAIResourcesWithAnimation instead

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bLockMovement | bool  |  |  |
| LockAILogic | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnlockAIResources

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources.
	 	DEPRECATED. Use UnlockAIResourcesWithAnimation instead

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUnlockMovement | bool  |  |  |
| UnlockAILogic | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTimeToClosestMarker

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SyncGroup | FName  |  |  |
| MarkerName | FName  |  |  |
| OutMarkerTime | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### HasMarkerBeenHitThisFrame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SyncGroup | FName  |  |  |
| MarkerName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsSyncGroupBetweenMarkers

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSyncGroupName | FName  |  |  |
| PreviousMarker | FName  |  |  |
| NextMarker | FName  |  |  |
| bRespectMarkerOrder | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetSyncGroupPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSyncGroupName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FMarkerSyncAnimPosition  |  |  |

### TriggerAllSequenceSwitchNotify

Trigger AnimNotifies

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CheckCanTriggerNotify_AnimIsolation_Outer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimNotifyEvent | FAnimNotifyEvent &  |  |  |
| InNotify | UAnimNotify * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CheckCanTriggerNotifyState_AnimIsolation_Outer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimNotifyEvent | FAnimNotifyEvent &  |  |  |
| InNotifyState | UAnimNotifyState * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimNotifyEvent | FAnimNotifyEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ReplaceSubAnimNodeAnimClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| NewAnimClass | TSubclassOf < UAnimInstance >  |  |  |
| BlendTime | float  |  |  |
| bEnableNoWaitParallelEvalTask | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance *  |  |  |

### ReplaceSubAnimNodeAnimClass_EmptyClassDefaut

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| NewAnimClass | TSubclassOf < UAnimInstance >  |  |  |
| BlendTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance *  |  |  |

### ResetSubAnimNodeAnimClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| FilterAnimClass | TSubclassOf < UAnimInstance >  |  |  |
| BlendTime | float  |  |  |
| bEnableNoWaitParallelEvalTask | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetSubAnimNodeAnimClass_EmptyClassDefaut

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| FilterAnimClass | TSubclassOf < UAnimInstance >  |  |  |
| BlendTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetAllSubAnimNode

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClearAllSubAnimBlendTime

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetAllSubAnimNodePosInertialization

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetSubAnimInstanceBySlot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance *  |  |  |

### IsUseSubAnimInstanceBySlot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetSubAnimNodeEnableBlend

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| bEnable | bool  |  |  |
| NewSubAnimBlendTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSubAnimNodeAnimClass

同槽多子动画实例

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| NewAnimClass | TSubclassOf < UAnimInstance >  |  |  |
| Priority | int32  |  |  |
| BlendTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance *  |  |  |

### RemoveSubAnimNodeAnimClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName  |  |  |
| FilterClass | TSubclassOf < UAnimInstance >  |  |  |
| BlendTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetSubAnimNode_MultiInstanceClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubInstanceSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetAllSubAnimNode_MultiInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddStopTickSubAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Instance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveCachedStopTickSubAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Instance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAllStopTickSubAnimInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRecycleCachedSubAnimInstances

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bToPersistentPool | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MarkBoneStateDirty

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsDirty | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBoneStateDirty

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsUseBoneStateDirtyFeature

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### HasSlotNode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UpdateAnimSlotRetargetInfo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMontage | UAnimMontage *  |  |  |
| InSlotNameRetargetInfo | TMap < FName , FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInverseRetargetIgnoreBoneList

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const TArray < int32 > & |  |  |

### SetFollowedAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputFollowedInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetFollowedAnimInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsFollowing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetFollowedInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetDelayPlay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsDelay | bool  |  |  |
| InputDelayFrames | int |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetParentAnimInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance * |  |  |

### SetParentAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InParentAnimInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### GetAllSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### SwapCachedBoneTransformMap

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCachedBoneTransform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName  |  |  |
| OutTransform | FTransform &  |  |  |
| forceSync | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetCachedBoneTransformByFlag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName  |  |  |
| InCacheFlag | FName  |  |  |
| OutTransform | FTransform &  |  |  |
| NeedLastFrameCount | int32  |  |  |
| forceSync | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CompareCachedBoneTransformByFlag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName0 | FName  |  |  |
| InCacheFlag0 | FName  |  |  |
| InBoneName1 | FName  |  |  |
| InCacheFlag1 | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### SetTriggerAnimNotify

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NeedTrigger | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FilterForceTriggerNotifyWhenMontageJumpTick

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMontage | UAnimMontage *  |  |  |
| bPlayingBackwards | bool  |  |  |
| CurrentTrackPos | float  |  |  |
| CurrentDeltaSeconds | float  |  |  |
| InAnimNotifies | TArray < FAnimNotifyEvent > &  |  |  |
| OutForceTriggerAnimNotifies | TArray < FAnimNotifyEvent > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLobbySeqIgnoreNotifyList

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FString > |  |  |

### ResetNotifyQueue

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

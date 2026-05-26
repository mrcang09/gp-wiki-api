# USkeletalMeshComponent

- Symbol Type: class
- Symbol Path: Others / USkeletalMeshComponent
- Source JSON Path: class/detail/Others/USkeletalMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

SkeletalMeshComponent is used to create an instance of an animated SkeletalMesh asset.
 
  @see USkeletalMesh

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimationMode | TEnumAsByte < EAnimationMode :: Type > | Animation<br>	 <br>	 @Todo anim: Matinee related data start - this needs to be replaced to new system. <br>	 @Todo anim: Matinee related data end - this needs to be replaced to new system. <br>	 Whether to use Animation Blueprint or play Single Animation Asset. |  |
| AnimBlueprintGeneratedClass | UAnimBlueprintGeneratedClass * |  |  |
| AnimClass | TSubclassOf < UAnimInstance > | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |  |
| bAutoInitAnimInstance | bool | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |  |
| AnimScriptInstance | UAnimInstance * | The active animation graph program instance. |  |
| SubInstances | TArray < UAnimInstance * > | Any running sub anim instances that need to be updates on the game thread |  |
| NewSubInstances | TArray < UAnimInstance * > |  |  |
| DirtySubInstances | TArray < UAnimInstance * > |  |  |
| StopTickSubInstances | TArray < UAnimInstance * > |  |  |
| PostProcessAnimInstance | UAnimInstance * | An instance created from the PostPhysicsBlueprint property of the skeletal mesh we're using,<br>	   Runs after physics has been blended |  |
| AnimationData | FSingleAnimationPlayData |  |  |
| CachedBoneSpaceTransforms | TArray < FTransform > | Cached BoneSpaceTransforms for Update Rate optimization. |  |
| CachedComponentSpaceTransforms | TArray < FTransform > | Cached SpaceBases for Update Rate optimization. |  |
| GlobalAnimRateScale | float | Used to scale speed of all animations on this skeletal mesh. |  |
| UseAsyncScene | EDynamicActorScene | The simulation scene to use for this instance. By default we use what's in the physics asset (which defaults to the sync scene) |  |
| bHasValidBodies | uint32 | If true, there is at least one body in the current PhysicsAsset with a valid bone in the current SkeletalMesh |  |
| KinematicBonesUpdateType | TEnumAsByte < EKinematicBonesUpdateToPhysics :: Type > | If we are running physics, should we update non-simulated bones based on the animation bone positions. |  |
| UpdateKinematicBonesRate | int32 |  |  |
| PhysicsTransformUpdateMode | TEnumAsByte < EPhysicsTransformUpdateMode :: Type > | Whether physics simulation updates component transform. |  |
| bBlendPhysics | uint32 | Enables blending in of physics bodies whether Simulate or not |  |
| bEnablePhysicsOnDedicatedServer | uint32 | If true, simulate physics for this component on a dedicated server.<br>	   This should be set if simulating physics and replicating with a dedicated server.<br>	 	Note: This property cannot be changed at runtime. |  |
| bEnableCreatePhysicsOnDedicatedServer | uint32 |  |  |
| bNeedUpdatePhysicsTickRegisteredState | bool |  |  |
| bUpdateJointsFromAnimation | uint32 | If we should pass joint position to joints each frame, so that they can be used by motorized joints to drive the<br>	 	ragdoll based on the animation. |  |
| bDisableClothSimulation | uint32 | Disable cloth simulation and play original animation without simulation |  |
| bAllowAnimCurveEvaluation | uint32 | Disable animation curves for this component. If this is set true, no curves will be processed |  |
| bDisableAnimCurves_DEPRECATED | uint32 | DEPRECATED. Use bAllowAnimCurveEvaluation instead |  |
| DisallowedAnimCurves | TArray < FName > | You can choose to disable certain curves if you prefer.<br>	  This is transient curves that will be ignored by animation system if you choose this |  |
| bCollideWithEnvironment | uint32 | can't collide with part of environment if total collision volumes exceed 16 capsules or 32 planes per convex |  |
| bCollideWithAttachedChildren | uint32 | can't collide with part of attached children if total collision volumes exceed 16 capsules or 32 planes per convex |  |
| bLocalSpaceSimulation | uint32 | It's worth trying this option when you feel that the current cloth simulation is unstable.<br>	  The scale of the actor is maintained during the simulation.<br>	  It is possible to add the inertia effects to the simulation, through the inertiaScale parameter of the clothing material.<br>	  So with an inertiaScale of 1.0 there should be no visible difference between local space and global space simulation.<br>	  Known issues: - Currently there's simulation issues when this feature is used in 3.x (DE4076) So if localSpaceSim is enabled there's no inertia effect when the global pose of the clothing actor changes. |  |
| bClothMorphTarget | uint32 | cloth morph target option<br>	  This option will be applied only before playing because should do pre-calculation to reduce computation time for run-time play<br>	  so it's impossible to change this option in run-time |  |
| bResetAfterTeleport | uint32 | reset the clothing after moving the clothing position (called teleport) |  |
| ClothBlendWeight | float | weight to blend between simulated results and key-framed positions<br>	  if weight is 1.0, shows only cloth simulation results and 0.0 will show only skinned results |  |
| RootBoneTranslation | FVector | Offset of the root bone from the reference pose. Used to offset bounding box. |  |
| bDeferMovementFromSceneQueries | uint32 | Optimization<br>	 <br>	  Whether animation and world transform updates are deferred. If this is on, the kinematic bodies (scene query data) will not update until the next time the physics simulation is run |  |
| bNoSkeletonUpdate | uint32 | Skips Ticking and Bone Refresh. |  |
| bPauseAnims | uint32 | pauses this component's animations (doesn't tick them, but still refreshes bones) |  |
| bUseRefPoseOnInitAnim | bool | On InitAnim should we set to ref pose (if false use first tick of animation data) |  |
| bEnablePerPolyCollision | uint32 | Uses skinned data for collision data. |  |
| BodySetup | UBodySetup * | Used for per poly collision. In 99% of cases you will be better off using a Physics Asset.<br>	 This BodySetup is per instance because all modification of vertices is done in place |  |
| bForceRefpose | bool | Misc<br>	 <br>	 If true, force the mesh into the reference pose - is an optimization. |  |
| bOnlyAllowAutonomousTickPose | uint32 | If true TickPose() will not be called from the Component's TickComponent function.<br>	 It will instead be called from Autonomous networking updates. See ACharacter. |  |
| bIsAutonomousTickPose | uint32 | True if calling TickPose() from Autonomous networking updates. See ACharacter. |  |
| bOldForceRefPose | uint32 | If bForceRefPose was set last tick. |  |
| bShowPrePhysBones | uint32 | Bool that enables debug drawing of the skeleton before it is passed to the physics. Useful for debugging animation-driven physics. |  |
| bRequiredBonesUpToDate | uint32 | If false, indicates that on the next call to UpdateSkelPose the RequiredBones array should be recalculated. |  |
| bAnimTreeInitialised | uint32 | If true, AnimTree has been initialised. |  |
| bIncludeComponentLocationIntoBounds | uint32 | If true, the Location of this Component will be included into its bounds calculation<br>	 (this can be useful when using SMU_OnlyTickPoseWhenRendered on a character that moves away from the root and no bones are left near the origin of the component) |  |
| bEnableLineCheckWithBounds | uint32 | If true, line checks will test against the bounding box of this skeletal mesh component and return a hit if there is a collision. |  |
| CachedAnimCurveUidVersion | uint16 | Cache AnimCurveUidVersion from Skeleton and this will be used to identify if it needs to be updated |  |
| LineCheckBoundsScale | FVector | If bEnableLineCheckWithBounds is true, scale the bounds by this value before doing line check. |  |
| OnConstraintBroken | FConstraintBrokenSignature | Notification when constraint is broken. |  |
| SaveBoneSpaceTransfroms | TArray < FTransform > |  |  |
| ClothingSimulationFactory | TSubclassOf < UClothingSimulationFactory > | Class of the object responsible for |  |
| TeleportDistanceThreshold | float | Conduct teleportation if the character's movement is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check.<br>	 You can also do force teleport manually using ForceNextUpdateTeleport()  ForceNextUpdateTeleportAndReset(). |  |
| TeleportRotationThreshold | float | Rotation threshold in degrees, ranging from 0 to 180.<br>	 Conduct teleportation if the character's rotation is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check. |  |
| bEnableUpdateOverlapsEvent | uint8 |  |  |
| SequenceToPlay_DEPRECATED | UAnimSequence * |  |  |
| AnimToPlay_DEPRECATED | UAnimationAsset * |  |  |
| bDefaultLooping_DEPRECATED | uint32 |  |  |
| bDefaultPlaying_DEPRECATED | uint32 |  |  |
| DefaultPosition_DEPRECATED | float |  |  |
| DefaultPlayRate_DEPRECATED | float |  |  |
| LastPoseTickFrame | uint32 |  |  |
| LastPoseTickTime | float | Keep track of when animation has been ticked to ensure it is ticked only once per frame. |  |
| bNeedsQueuedAnimEventsDispatched | bool |  |  |
| bIsNeedUpdate | bool |  |  |
| bSkeletalMeshDirty | bool |  |  |
| BoneRetargetSource | FName |  |  |
| MeshShiftTransform | FTransform |  |  |
| MeshShiftRefBone | FName |  |  |
| MeshShiftAnchorRefBone | FName |  |  |
| bUseMeshShiftFeature | bool |  |  |
| bOnlyPartOfShiftRefBoneAsRoot | bool |  |  |
| MeshShiftCompensationType | EMeshShiftCompensationType |  |  |
| MeshShiftCompensationBaseSkelComp | TWeakObjectPtr < USkeletalMeshComponent > |  |  |
| AnimOverrideMeshShiftParam | FMeshShiftParam |  |  |
| DynamicBoneScaleFeature_Scale3D | FVector |  |  |
| DynamicBoneScaleFeature_BoneNameList | TArray < FName > |  |  |
| bUseDynamicBoneScaleFeature | bool |  |  |
| bIsOverrideScale | bool |  |  |
| bIsEnableBatchSection | bool | For Dynamic Bone Scale Feature End |  |
| BatchSectionList | TArray < FDynamicBatchSectionInfo > |  |  |
| OriginalMaterials | TArray < UMaterialInterface * > |  |  |
| AnimationBlueprint_DEPRECATED | UAnimBlueprint * | The blueprint for creating an AnimationScript. |  |
| bUpdateAnimationInEditor | uint32 | If true, this will Tick until disabled |  |
| BoneRetargetBaseRefMesh | USkeletalMesh * | For Bone Retarget Feature Start |  |

## Functions

### SetAnimInstanceClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewClass | UClass *  |  |  |
| bTickAnimationNow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyBoneSpaceTransfroms

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputTransforms | TArray < FTransform > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoneSpaceTransfromsForCopy

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Other | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FTransform >  |  |  |

### GetAnimInstance

Returns the animation instance that is driving the class (if available). This is typically an instance of
	  the class set as AnimBlueprintGeneratedClass (generated by an animation blueprint)
	  Since this instance is transient, it is not safe to be used during construction script

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance * |  |  |

### GetSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### GetNewSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### GetAllSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### GetDirtySubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### GetStopTickSubAnimInstances

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UAnimInstance * > |  |  |

### ClearDirtySubAnimInstances

清理所有脏标记的SubAnimInstance
	  从SubInstances、NewSubInstances、StopTickSubInstances中移除，并调用UninitializeAnimation、PendingDestroy等清理逻辑

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddNewSubAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddDirtySubAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddStopTickSubAnimInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPostProcessInstance

Returns the active post process instance is one is available. This is set on the mesh that this
	  component is using, and is evaluated immediately after the main instance.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimInstance * |  |  |

### SetAnimationMode

Below are the interface to control animation when animation mode, not blueprint mode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimationMode | EAnimationMode :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAnimationMode

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EAnimationMode :: Type |  |  |

### GetAnimationPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UAnimationAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### PlayAnimation

Animation play functions
	 
	  These changes status of animation instance, which is transient data, which means it won't serialize with this component
	  Because of that reason, it is not safe to be used during construction script
	  Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAnimToPlay | UAnimationAsset *  |  |  |
| bLooping | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAnimation

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAnimToPlay | UAnimationAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Play

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bLooping | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Stop

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsPlaying

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetPosition

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPos | float  |  |  |
| bFireNotifies | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPosition

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetPlayRate

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Rate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlayRate

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### OverrideAnimationData

This overrides current AnimationData parameter in the SkeletalMeshComponent. This will serialize when the component serialize
	  so it can be used during construction script. However note that this will override current existing data
	  This can be useful if you'd like to make a blueprint with custom default animation per component
	  This sets single player mode, which means you can't use AnimBlueprint with it

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimToPlay | UAnimationAsset *  |  |  |
| bIsLooping | bool  |  |  |
| bIsPlaying | bool  |  |  |
| Position | float  |  |  |
| PlayRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMorphTarget

Set Morph Target with Name and Value(0-1)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MorphTargetName | FName  |  |  |
| Value | float  |  |  |
| bRemoveZeroWeight | bool | : Used by editor code when it should stay in the active list with zero weight |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMorphTargets

Clear all Morph Target that are set to this mesh

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetMorphTarget

Get Morph target with given name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MorphTargetName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SnapshotPose

Takes a snapshot of this skeletal mesh component's pose and saves it to the specified snapshot.
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

### GetClothMaxDistanceScale

GetSet the max distance scale of clothing mesh vertices

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetClothMaxDistanceScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Scale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ForceClothNextUpdateTeleport

Used to indicate we should force 'teleport' during the next call to UpdateClothState,
	  This will transform positions and velocities and thus keep the simulation state, just translate it to a new pose.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ForceClothNextUpdateTeleportAndReset

Used to indicate we should force 'teleport and reset' during the next call to UpdateClothState.
	  This can be used to reset it from a bad state or by a teleport where the old state is not important anymore.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SuspendClothingSimulation

Stops simulating clothing, but does not show clothing ref pose. Keeps the last known simulation state

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResumeClothingSimulation

Resumes a previously suspended clothing simulation, teleporting the clothing on the next tick

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsClothingSimulationSuspended

Gets whether or not the clothing simulation is currently suspended

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ResetClothTeleportMode

Reset the teleport mode of a next update to 'Continuous'

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BindClothToMasterPoseComponent

If this component has a valid MasterPoseComponent then this function makes cloth items on the slave component
	  take the transforms of the cloth items on the master component instead of simulating separately.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UnbindClothFromMasterPoseComponent

If this component has a valid MasterPoseComponent and has previously had its cloth bound to the
	  MCP, this function will unbind the cloth and resume simulation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bRestoreSimulationSpace | bool | if true and the master pose cloth was originally simulating in world |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUpdateAnimationInEditor

Sets whether or not to force tick component in order to update animation and refresh transform for this component
	 This is supported only in the editor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewUpdateState | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDisableAnimCurves

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInDisableAnimCurves | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDisableAnimCurves

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetAllowAnimCurveEvaluation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInAllow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllowedAnimCurveEvaluate

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### AllowAnimCurveEvaluation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NameOfCurve | FName  |  |  |
| bAllow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetAllowedAnimCurveEvaluation

By reset, it will allow all the curves to be evaluated

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetAllowedAnimCurvesEvaluation

resets, and then only allow the following list to be alloweddisallowed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| List | TArray < FName > &  |  |  |
| bAllow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTeleportRotationThreshold

Gets the teleportation rotation threshold.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | Threshold in degrees. |  |

### SetTeleportRotationThreshold

Sets the teleportation rotation threshold.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Threshold | float | Threshold in degrees. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTeleportDistanceThreshold

Gets the teleportation distance threshold.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | Threshold value. |  |

### SetTeleportDistanceThreshold

Sets the teleportation distance threshold.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Threshold | float | Threshold value. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBodyNotifyRigidBodyCollision

Changes the value of bNotifyRigidBodyCollision for a given body

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewNotifyRigidBodyCollision | bool  | The value to assign to bNotifyRigidBodyCollision |  |
| BoneName | FName |   Name of the body to turn hit notifies onoff. None implies root body |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNotifyRigidBodyCollisionBelow

Changes the value of bNotifyRigidBodyCollision on all bodies below a given bone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewNotifyRigidBodyCollision | bool  | The value to assign to bNotifyRigidBodyCollision |  |
| BoneName | FName  |   Name of the body to turn hit notifies on (and below) |  |
| bIncludeSelf | bool |   Whether to modify the given body (useful for roots with multiple children) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEnableBodyGravity

Enables or disables gravity for the given bone.
	 	NAME_None indicates the root body will be edited.
	 	If the bone name given is otherwise invalid, nothing happens.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableGravity | bool  | Whether gravity should be enabled or disabled. |  |
| BoneName | FName |  The name of the bone to modify. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBodyGravityEnabled

Checks whether or not gravity is enabled on the given bone.
	 	NAME_None indicates the root body should be queried.
	 	If the bone name given is otherwise invalid, false is returned.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName | The name of the bone to check. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if gravity is enabled on the bone. |  |

### SetEnableGravityOnAllBodiesBelow

Enables or disables gravity to all bodies below the given bone.
	   NAME_None indicates all bodies will be edited.
		In that case, consider using UPrimitiveComponent::EnableGravity.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableGravity | bool  | Whether gravity should be enabled or disabled. |  |
| BoneName | FName  |  The name of the top most bone. |  |
| bIncludeSelf | bool | Whether the bone specified should be edited. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetClosestPointOnPhysicsAsset

Given a world position, find the closest point on the physics asset. Note that this is independent of collision and welding. This is based purely on animation position

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldPosition | FVector &  |  The point we want the closest point to (i.e. for all bodies in the physics asset, find the one that has a point closest to WorldPosition) |  |
| ClosestWorldPosition | FVector &  |  |  |
| Normal | FVector &  |  |  |
| BoneName | FName &  |  |  |
| Distance | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if we found a closest point |  |

### GetBoneMass

Returns the mass (in kg) of the given bone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  | Name of the body to return. 'None' indicates root body. |  |
| bScaleMass | bool | If true, the mass is scaled by the bone's MassScale. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetSkeletalCenterOfMass

Returns the center of mass of the skeletal mesh, instead of the root body's location

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### AddForceToAllBodiesBelow

Add a force to all rigid bodies below.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  |  Force vector to apply. Magnitude indicates strength of force. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |
| bAccelChange | bool  | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |  |
| bIncludeSelf | bool | If false, Force is only applied to bodies below but not given bone name. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddImpulseToAllBodiesBelow

Add impulse to all single rigid bodies below. Good for one time instant burst.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  | Magnitude and direction of impulse to apply. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |  |
| bVelChange | bool  | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |  |
| bIncludeSelf | bool | If false, Force is only applied to bodies below but not given bone name. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsEnableAnimBoneStateDirtyFeature

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetAllBodiesSimulatePhysics

Set bSimulatePhysics to true for all bone bodies. Does not change the component bSimulatePhysics flag.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewSimulate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsBlendWeight

This is global set up for setting physics blend weight
	  This does multiple things automatically
	  If PhysicsBlendWeight == 1.f, it will enable Simulation, and if PhysicsBlendWeight == 0.f, it will disable Simulation.
	  Also it will respect each body's setup, so if the body is fixed, it won't simulate. Vice versa
	  So if you'd like all bodies to change manually, do not use this function, but SetAllBodiesPhysicsBlendWeight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PhysicsBlendWeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEnablePhysicsBlending

Disable physics blending of bones

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewBlendPhysics | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllBodiesBelowSimulatePhysics

Set all of the bones below passed in bone to be simulated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName &  |  |  |
| bNewSimulate | bool  |  |  |
| bIncludeSelf | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetAllBodiesSimulatePhysics

Allows you to reset bodies Simulate state based on where bUsePhysics is set to true in the BodySetup.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetAllBodiesPhysicsBlendWeight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PhysicsBlendWeight | float  |  |  |
| bSkipCustomPhysicsType | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllBodiesBelowPhysicsBlendWeight

Set all of the bones below passed in bone to be simulated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName &  |  |  |
| PhysicsBlendWeight | float  |  |  |
| bSkipCustomPhysicsType | bool  |  |  |
| bIncludeSelf | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AccumulateAllBodiesBelowPhysicsBlendWeight

Accumulate AddPhysicsBlendWeight to physics blendweight for all of the bones below passed in bone to be simulated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName &  |  |  |
| AddPhysicsBlendWeight | float  |  |  |
| bSkipCustomPhysicsType | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllMotorsAngularPositionDrive

Enable or Disable AngularPositionDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSwingDrive | bool  |  |  |
| bEnableTwistDrive | bool  |  |  |
| bSkipCustomPhysicsType | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllMotorsAngularVelocityDrive

Enable or Disable AngularVelocityDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSwingDrive | bool  |  |  |
| bEnableTwistDrive | bool  |  |  |
| bSkipCustomPhysicsType | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllMotorsAngularDriveParams

Set Angular Drive motors params for all constraint instances

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSpring | float  |  |  |
| InDamping | float  |  |  |
| InForceLimit | float  |  |  |
| bSkipCustomPhysicsType | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintProfile

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset. If profile name is not found the joint is set to use the default constraint profile.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| JointName | FName  |  |  |
| ProfileName | FName  |  |  |
| bDefaultIfNotFound | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintProfileForAll

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset for all constraints. If profile name is not found the joint is set to use the default constraint profile.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProfileName | FName  |  |  |
| bDefaultIfNotFound | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FindConstraintBoneName

Find Constraint Name from index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintIndex | int32 | Index of constraint to look for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | Constraint Joint Name |  |

### BreakConstraint

Break a constraint off a Gore mesh.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  | vector of impulse |  |
| HitLocation | FVector  | location of the hit |  |
| InBoneName | FName | Name of bone to break constraint for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularLimits

Sets the Angular Motion Ranges for a named bone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName  | Name of bone to adjust constraint ranges for |  |
| Swing1LimitAngle | float  | Size of limit in degrees, 0 means locked, 180 means free |  |
| TwistLimitAngle | float  | Size of limit in degrees, 0 means locked, 180 means free |  |
| Swing2LimitAngle | float | Size of limit in degrees, 0 means locked, 180 means free |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentJointAngles

Gets the current Angular state for a named bone constraint

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoneName | FName  | Name of bone to get constraint ranges for |  |
| Swing1Angle | float &  | current angular state of the constraint |  |
| TwistAngle | float &  | current angular state of the constraint |  |
| Swing2Angle | float & | current angular state of the constraint |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HandleExistingParallelEvaluationTask

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bBlockOnTask | bool  |  |  |
| bPerformPostAnimEvaluation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### HandleExistingParallelIMPhysicsEvaluationTask

ImmediatePhysics Evaluation Start

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bBlockOnTask | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetLastPoseTickFrame_BP

Checked whether we have already ticked the pose this frame

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64 |  |  |

### SetNeedUpdateChildTransformsOnFinalizeAnimationUpdate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUpdate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PauseIMSimulation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPauseFrameCount | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MarkMeshShiftFeature

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsUseShiftFeature | bool  |  |  |
| InIsOnlyPartOfShiftRefBoneAsRoot | bool  |  |  |
| InShiftTransform | FTransform &  |  |  |
| InShiftRefBone | FName  |  |  |
| InAnchorRefBone | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MarkMeshShiftCompensation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMeshShiftCompensationType | EMeshShiftCompensationType  |  |  |
| InCompensationBaseSkelComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AnimOverrideMeshShiftParam_Start

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimMeshShiftParam | FMeshShiftParam & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AnimOverrideMeshShiftParam_Stop

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimMeshShiftParam | FMeshShiftParam & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetRawCurveValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCurveName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetRetargetBoneRelativeTMInBaseRefPose

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetBoneName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### SingleNodeInstance_ActiveBoneRetargetFeature

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsActive | bool  |  |  |
| InTargetSkelComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SingleNodeInstance_OverrideBoneRetargetParam

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsUseRetargetFeature | bool  |  |  |
| InIsConsiderMasterPoseRetarget | bool  |  |  |
| InIsForeceUseBaseSkeletonAsRetargetSource | bool  |  |  |
| InTargetSkelComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsInitAnimTickDelay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsInitRefreshPoseDelay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### DelayInitAnimTick

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInitAnimTickParam | FDelayInitAnimTickParam & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DelayInitRefreshPose

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PerformDelayedInitAnimTick

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PerformDelayedInitRefreshPose

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### MarkDynamicBoneScaleFeature

For Bone Retarget Feature End 
	 
	
	  For Dynamic Bone Scale Feature Start

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsUseDynamicBoneScaleFeature | bool  |  |  |
| InIsOverrideScale | bool  |  |  |
| InTargetBoneNameList | TArray < FName > &  |  |  |
| InDynamicScale3D | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsSectionBatched

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BatchSectionsWithAtlas

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIdx | int32  |  |  |
| IsBatchSection | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AutoBatchSection

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIdx | int32  |  |  |
| BatchIndices | TArray < int32 >  |  |  |
| IsBatchSection | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearInterpolateBoneCache

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DurationTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

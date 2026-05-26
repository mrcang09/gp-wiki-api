# AActor

- Symbol Type: class
- Symbol Path: Others / AActor
- Source JSON Path: class/detail/Others/AActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

Actor is the base class for an Object that can be placed or spawned in a level.
  Actors may contain a collection of ActorComponents, which can be used to control how actors move, how they are rendered, etc.
  The other main function of an Actor is the replication of properties and function calls across the network during play.
 
  @see UActorComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryActorTick | FActorTickFunction | Primary Actor tick function, which calls TickActor().<br>	  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.<br>	  @see AddTickPrerequisiteActor(), AddTickPrerequisiteComponent() |  |
| CustomTimeDilation | float | Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick. |  |
| bAllowBPReceiveTickEvent | bool | If true, bp tick will be called , otherwise skipped |  |
| TickAdapterInterval | uint8 |  |  |
| bTickAdapterRqrMainFrame | uint8 |  |  |
| bSupportSuspendTick | uint8 |  |  |
| bHidden | uint8 | Allows us to only see this Actor in the Editor, and not in the actual game.<br>	  @see SetActorHiddenInGame() |  |
| bConsideredHidden | uint8 |  |  |
| bNetTemporary | uint8 | If true, when the actor is spawned it will be sent to the client but receive no further replication updates from the server afterwards. |  |
| bNetStartup | uint8 | If true, this actor was loaded directly from the map, and for networking purposes can be addressed by its full path name |  |
| bOnlyRelevantToOwner | uint8 | If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed. |  |
| bOwningSpecificNetConsideration | uint8 | If true, this actor is considered for replication in an owning-specific semantics. |  |
| bRegionBasedNetConsideration | uint8 | If true, this actor is considered for replication in region-based semantics. |  |
| bMRegionBasedNetConsideration | uint8 | If true, this actor is considered for replication in Mregion-based semantics. |  |
| bMRegionStatic | uint8 |  |  |
| bFastDistBasedNetRelevancy | uint8 | If true, this actor is checked for relevancy by fast distance-based calculation. |  |
| bGroupBasedNetRelevancy | uint8 | If true, this actor is checked for relevancy by relevancy group first. |  |
| bLazyNetReplication | uint8 | If true, this actor is only replicated by calling ForceNetUpdate. |  |
| bClientSimulatedRelevancy | uint8 | NOTE: Mark "Client Simulated Relevancy" for ob  replay<br>	 @see SetActorSimulatedRelevancy()<br>	 @see OnActorSimulatedRelevant() |  |
| bCheckAllRelyOnAttachment | uint8 |  |  |
| bAlwaysRelevant | uint8 | Always relevant for network (overrides bOnlyRelevantToOwner). |  |
| bForceOwnedMeshAlwaysRefreshBones | uint8 |  |  |
| bTearOff | uint8 | If true, this actor is no longer replicated to new clients, and is "torn off" (becomes a ROLE_Authority) on clients to which it was being replicated.<br>	  @see TornOff() |  |
| bExchangedRoles | uint8 | Whether we have already exchanged RoleRemoteRole on the client, as when removing then re-adding a streaming level.<br>	  Causes all initialization to be performed again even though the actor may not have actually been reloaded. |  |
| bNetLoadOnClient | uint8 | This actor will be loaded on network clients during map load |  |
| bNetUseOwnerRelevancy | uint8 | If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority |  |
| bBlockInput | uint8 | If true, all input on the stack below this actor will not be considered |  |
| bCanBeBaseForCharacter | uint8 | If true, all input on the stack below this actor will not be considered |  |
| bAllowTickBeforeBeginPlay | uint8 | Whether we allow this Actor to tick before it receives the BeginPlay event.<br>	  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.<br>	  This Actor must be able to tick for this setting to be relevant. |  |
| bCustomHandlingNetworkSubobjectDeletion | uint8 |  |  |
| bReplicates | uint8 | If true, this actor will replicate to remote machines<br>	  @see SetReplicates() |  |
| RemoteRole | TEnumAsByte < enum ENetRole > | Describes how much control the remote machine has over the actor. |  |
| Owner | AActor * | Owner of this Actor, used primarily for replication (bNetUseOwnerRelevancy & bOnlyRelevantToOwner) and visibility (PrimitiveComponent bOwnerNoSee and bOnlyOwnerSee)<br>	  @see SetOwner(), GetOwner() |  |
| bReplicateMovement | uint8 | If true, replicate movementlocation related properties.<br>	  Actor must also be set to replicate.<br>	  @see SetReplicates() |  |
| bActorEnableCollision | uint8 | Enables any collision on this actor.<br>	  @see SetActorEnableCollision(), GetActorEnableCollision() |  |
| bEnableDeferredConstructComponent | uint8 |  |  |
| bUseSpawnReplicatedActorMaxFrameDelayFromConfig | uint8 |  |  |
| PendingConstructComponents | TArray < FDeferedComponentUnit > |  |  |
| PreSCSComponentsBeforeDeferContruction | TArray < UActorComponent * > |  |  |
| AsyncReplicatedActorSpawnDistA | float |  |  |
| AsyncReplicatedActorSpawnDistB | float |  |  |
| SpawnReplicatedActorMaxFrameDelayFromConfig | int32 |  |  |
| ScriptNetworkReplicatedPropertyWrapper | FScriptNetworkReplicatedPropertyWrapper |  |  |
| NetDriverName | FName | Used to specify the net driver to replicate on (NAME_None || NAME_GameNetDriver is the default net driver) |  |
| ReplicatedMovement | FRepMovement | Used for replication of our RootComponent's position and velocity |  |
| InitialLifeSpan | float | How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun. |  |
| AttachmentReplication | FRepAttachment | Used for replicating attachment of this actor's RootComponent to another actor.<br>	  This is filled in via GatherCurrentMovement() when the RootComponent has an AttachParent. |  |
| Role | TEnumAsByte < enum ENetRole > | Describes how much control the local machine has over the actor. |  |
| NetDormancy | TEnumAsByte < enum ENetDormancy > | Dormancy setting for actor to take itself off of the replication list without being destroyed on clients. |  |
| AutoReceiveInput | TEnumAsByte < EAutoReceiveInput :: Type > | Automatically registers this actor to receive input from a player. |  |
| InputPriority | int32 | The priority of this input component when pushed in to the stack. |  |
| InputComponent | UInputComponent * | Component that handles input for this actor, if input is enabled. |  |
| NetCullDistanceSquared | float | Square of the max distance from the client's viewpoint that this actor is relevant and will be replicated. |  |
| NetCullFactorSquared | float | NetCullDistanceSquared Factor for Connection |  |
| OBRelevantFactor | float |  |  |
| NetTag | int32 | Internal - used by UWorld::ServerTickClients() |  |
| NetConsiderFrequency | float | How often (per second) this actor enters consider list, should be greater than or equal to NetUpdateFrequency |  |
| NetUpdateFrequency | float | How often (per second) this actor will be checked for replication, used to determine NetUpdateTime |  |
| MinNetUpdateFrequency | float | Used to determine what rate to throttle down to when replicated properties are changing infrequently |  |
| NetUpdateJumpFrame | int32 |  |  |
| NetPriority | float | Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate |  |
| bAutoDestroyWhenFinished | uint8 | If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight. |  |
| bCanBeDamaged | uint8 | Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.<br>	  @see TakeDamage(), ReceiveDamage() |  |
| bCanNotifyDamager | uint8 | Whether this actor can Notify damager. Must be true for notify damager events (PreDamageOther) to be called.<br>	  @see TakeDamage(), PreDamageOther() |  |
| bRepParentUpdatePhx | uint8 |  |  |
| bActorIsBeingDestroyed | uint8 | Set when actor is about to be deleted. |  |
| bCollideWhenPlacing | uint8 | This actor collides with the world when placing in the editor, even if RootComponent collision is disabled. Does not affect spawning, @see SpawnCollisionHandlingMethod |  |
| bFindCameraComponentWhenViewTarget | uint8 | If true, this actor should search for an owned camera component to view through when used as a view target. |  |
| bRelevantForNetworkReplays | uint8 | If true, this actor will be replicated to network replays (default is true) |  |
| bForcedRelevancyCheckForReplay | uint8 |  |  |
| bLowUpdateRateForReplay | uint8 |  |  |
| bGenerateOverlapEventsDuringLevelStreaming | uint8 | If true, this actor will generate overlap events when spawned as part of level streaming. You might enable this is in the case where a streaming level loads around an actor and you want overlaps to trigger. |  |
| bCanCachedInWorldSpecialActorList | uint8 |  |  |
| bShouldDumpCallstackWhenMovingfast | uint8 |  |  |
| bCanBeInCluster | uint8 | If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance |  |
| bAllowReceiveTickEventOnDedicatedServer | uint8 | If false, the Blueprint ReceiveTick() event will be disabled on dedicated servers.<br>	  @see AllowReceiveTickEventOnDedicatedServer() |  |
| bActorSeamlessTraveled | uint8 | Indicates the actor was pulled through a seamless travel. |  |
| bIgnoresOriginShifting | uint8 | Whether this actor should not be affected by world origin shifting. |  |
| bEnableAutoLODGeneration | uint8 | If true, and if World setting has bEnableHierarchicalLOD equal to true, then it will generate LODActor from groups of clustered Actor |  |
| SpawnCollisionHandlingMethod | ESpawnActorCollisionHandlingMethod | Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here. |  |
| CollisionCheckMoveDisStep | float |  |  |
| CollisionCheckMoveDegreeStep | float |  |  |
| CollisionCheckCircleRadius | float |  |  |
| Instigator | APawn * | Pawn responsible for damage caused by this actor. |  |
| Children | TArray < AActor * > | Array of Actors whose Owner is this actor |  |
| RootComponent | USceneComponent * | Collision primitive that defines the transform (location, rotation, scale) of this Actor. |  |
| ControllingMatineeActors | TArray < AMatineeActor * > | The matinee actors that control this actor. |  |
| Layers | TArray < FName > | Layer's the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling. |  |
| ParentComponent | TWeakObjectPtr < UChildActorComponent > | The UChildActorComponent that owns this Actor. |  |
| Tags | TArray < FName > | Array of tags that can be used for grouping and categorizing. |  |
| DynamicTags | TArray < FName > |  |  |
| BlueprintCreatedComponents | TArray < UActorComponent * > | Array of ActorComponents that are created by blueprints and serialized per-instance. |  |
| InstanceComponents | TArray < UActorComponent * > | Array of ActorComponents that have been added by the user on a per-instance basis. |  |
| BackupRestoreIdentifier | int64 |  |  |
| NeedsBackupStates | uint8 |  |  |
| bSkipNewDuplicateOwnedComponents | uint8 | If you call CreateComponentFromTemplate on an actor which already owns a component with the same name, problem comes out<br>	  Optimized version will return the existing component, but not duplicate a new one, in this case, setting this switch to true is necessary |  |
| bCanBeNetContainer | uint8 |  |  |
| bDonotAsSubActor | uint8 |  |  |
| DeformEffectType | TEnumAsByte < enum EDeformEffectType > |  |  |
| bBlockLandscapeDeform | bool | If this actor will block any overlap deform. |  |
| bRemoveStaticChildActorComp | bool |  |  |
| InputConsumeOption_DEPRECATED | TEnumAsByte < enum EInputConsumeOptions > |  |  |
| ExportActorInLevel | bool | 在编辑器获取level里面actor的位置和朝向, 通过命令行方式导出到一个lua表格. feishen, 20210406 |  |
| PivotOffset | FVector | Local space pivot offset for the actor |  |
| ParentComponentActor_DEPRECATED | TWeakObjectPtr < AActor > | The Actor that owns the UChildActorComponent that owns this Actor. |  |
| GroupActor | AActor * | The group this actor is a part of. |  |
| SpriteScale | float | The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games). |  |
| ActorLabel | FString | The friendly name for this actor, displayed in the editor.  You should always use AActor::GetActorLabel() to access the actual label to display,<br>	  and call AActor::SetActorLabel() or FActorLabelUtilities::SetActorLabelUnique() to change the label.  Never set the label directly. |  |
| FolderPath | FName | The folder path of this actor in the world (empty=root,  separated) |  |
| bActorLabelEditable | uint8 |  |  |
| bHiddenEd | uint8 | Whether this actor is hidden within the editor viewport. |  |
| bEditable | uint8 | Whether the actor can be manipulated by editor operations. |  |
| bListedInSceneOutliner | uint8 | Whether this actor should be listed in the scene outliner. |  |
| bIsEditorPreviewActor | uint8 | True if this actor is the preview actor dragged out of the content browser |  |
| bHiddenEdLayer | uint8 | Whether this actor is hidden by the layer browser. |  |
| bHiddenEdTemporary | uint8 | Whether this actor is temporarily hidden within the editor; used for showhideetc functionality wo dirtying the actor. |  |
| bHiddenEdLevel | uint8 | Whether this actor is hidden by the level browser. |  |
| bLockLocation | uint8 | If true, prevents the actor from being moved in the editor viewport. |  |
| HiddenEditorViews | uint64 | Bitflag to represent which views this actor is hidden in, via per-view layer visibility. |  |
| bActorCoastline | uint8 |  |  |

## Functions

### GetToString

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### SetForceOwnedMeshAlwaysRefreshBones

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAlwaysRefreshBones | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRep_ReplicateMovement

Called on client when updated bReplicateMovement value is received for this actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### TearOff

Networking - Server - TearOff this actor to stop replication to clients. Will set bTearOff to true.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_Role

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_RemoteRole

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_Hidden

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_TearOff

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_CanBeDamaged

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_Owner

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### TickConstructComponentWithTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OneFrameConstructTimeMS | float  |  |  |
| bCreateImmediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### OnRep_ScriptNetworkReplicatedPropertyWrapper

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CallSubObjectLuaOnRep

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerSendScriptNetworkRemoteContent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | FScriptNetworkRemoteContent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerSendScriptNetworkRemoteContent_Unreliable

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | FScriptNetworkRemoteContent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSendScriptNetworkRemoteContent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | FScriptNetworkRemoteContent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSendScriptNetworkRemoteContent_Unreliable

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | FScriptNetworkRemoteContent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveScriptNetworkRemoteContent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | FScriptNetworkRemoteContent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReplicates

Set whether this actor replicates to network clients. When this actor is spawned on the server it will be sent to clients as well.
	  Properties flagged for replication will update on clients if they change on the server.
	  Internally changes the RemoteRole property and handles the cases where the actor needs to be added to the network actor list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInReplicates | bool | Whether this Actor replicates to network clients. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReplicateMovement

Set whether this actor's movement replicates to network clients.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInReplicateMovement | bool | Whether this Actor's movement replicates to clients. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLocalRole

Returns how much control the local machine has over this actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENetRole |  |  |

### GetRemoteRole

Returns how much control the remote machine has over this actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENetRole |  |  |

### GetRole

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENetRole |  |  |

### OnRep_AttachmentReplication

Called on client when updated AttachmentReplication value is received for this actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_Instigator

Called on clients when Instigator is replicated.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddDynamicTag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveDynamicTag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableInput

Pushes this actor on to the stack of input being handled by a PlayerController.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * | The PlayerController whose input events we want to receive. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableInput

Removes this actor from the stack of input being handled by a PlayerController.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * | The PlayerController whose input events we no longer want to receive. If null, this actor will stop receiving input from all PlayerControllers. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInputAxisValue

Gets the value of the input axis if input is enabled for this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputAxisName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInputAxisKeyValue

Gets the value of the input axis key if input is enabled for this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputAxisKey | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInputVectorAxisValue

Gets the value of the input axis key if input is enabled for this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputAxisKey | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetInstigator

Returns the instigator for this actor, or NULL if there is none.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn * |  |  |

### GetInstigatorController

Returns the instigator's controller for this actor, or NULL if there is none.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AController * |  |  |

### GetTransform

Get the actor-to-world transform.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform | The transform that transforms from actor space to world space. |  |

### K2_GetActorLocation

Returns the location of the RootComponent of this Actor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### K2_SetActorLocation

Move the Actor to the specified location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector  | The new location to move the Actor to. |  |
| bSweep | bool  | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  | The hit result from the move if swept. |  |
| bTeleport | bool | Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the location was successfully set (if not swept), or whether movement occurred at all (if swept). |  |

### K2_GetActorRotation

Returns rotation of the RootComponent of this Actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator |  |  |

### GetActorForwardVector

Get the forward (X) vector (length 1.0) from this Actor, in world space.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetActorUpVector

Get the up (Z) vector (length 1.0) from this Actor, in world space.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetActorRightVector

Get the right (Y) vector (length 1.0) from this Actor, in world space.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetActorBounds

Returns the bounding box of all components that make up this Actor (excluding ChildActorComponents).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOnlyCollidingComponents | bool  | If true, will only return the bounding box for components with collision enabled. |  |
| Origin | FVector &  |  |  |
| BoxExtent | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetRootComponent

Returns the RootComponent of this Actor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USceneComponent * |  |  |

### GetVelocity

Returns velocity (in cms (Unreal Unitssecond) of the rootcomponent if it is either using physics or has an associated MovementComponent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### K2_SetActorRotation

Set the Actor's rotation instantly to the specified rotation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRotation | FRotator  | The new rotation for the Actor. |  |
| bTeleportPhysics | bool | Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the rotation was successfully set. |  |

### K2_SetActorLocationAndRotation

Move the actor instantly to the specified location and rotation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector  | The new location to teleport the Actor to. |  |
| NewRotation | FRotator  | The new rotation for the Actor. |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  | The hit result from the move if swept. |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the rotation was successfully set. |  |

### SetActorScale3D

Set the Actor's world-space scale.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScale3D | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorScale3D

Returns the Actor's world-space scale.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetDistanceTo

Returns the distance from this Actor to OtherActor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetSquaredDistanceTo

Returns the squared distance from this Actor to OtherActor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetHorizontalDistanceTo

Returns the distance from this Actor to OtherActor, ignoring Z.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetVerticalDistanceTo

Returns the distance from this Actor to OtherActor, ignoring XY.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetDotProductTo

Returns the dot product from this Actor to OtherActor. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetHorizontalDotProductTo

Returns the dot product from this Actor to OtherActor, ignoring Z. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### K2_AddActorWorldOffset

Adds a delta to the location of this actor in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaLocation | FVector  | The change in location. |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  | The hit result from the move if swept. |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AddActorWorldRotation

Adds a delta to the rotation of this actor in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaRotation | FRotator  | The change in rotation. |  |
| bSweep | bool  |  Whether to sweep to the target rotation (not currently supported for rotation). |  |
| SweepHitResult | FHitResult &  | The hit result from the move if swept. |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AddActorWorldTransform

Adds a delta to the transform of this actor in world space. Scale is unchanged.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTransform | FTransform &  |  |  |
| bSweep | bool  |  |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetActorTransform

Set the Actors transform to the specified one.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTransform | FTransform &  | The new transform. |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### K2_AddActorLocalOffset

Adds a delta to the location of this component in its local reference frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaLocation | FVector  |  |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AddActorLocalRotation

Adds a delta to the rotation of this component in its local reference frame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaRotation | FRotator  | The change in rotation in local space. |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AddActorLocalTransform

Adds a delta to the transform of this component in its local reference frame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTransform | FTransform &  | The change in transform in local space. |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetActorRelativeLocation

Set the actor's RootComponent to the specified relative location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRelativeLocation | FVector  | New relative location of the actor's root component |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetActorRelativeRotation

Set the actor's RootComponent to the specified relative rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRelativeRotation | FRotator  | New relative rotation of the actor's root component |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetActorRelativeTransform

Set the actor's RootComponent to the specified relative transform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRelativeTransform | FTransform &  | New relative transform of the actor's root component |  |
| bSweep | bool  |  Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |  |
| SweepHitResult | FHitResult &  |  |  |
| bTeleport | bool |  Whether we teleport the physics state (if physics collision is enabled for this object). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorRelativeScale3D

Set the actor's RootComponent to the specified relative scale 3d

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRelativeScale | FVector | New scale to set the actor's RootComponent to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorRelativeScale3D

Return the actor's relative scale 3d

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetActorHiddenInGame

Sets the actor to be hidden in the game

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewHidden | bool | Whether or not to hide the actor and all its components |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorConsideredHidden

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewHidden | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorSimulatedRelevancy

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsRelevant | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnActorSimulatedRelevant

NOTE : Callback of Check Actor Relevancy in Client for ob or replay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsRelevant | bool  | : Whether or not relevant for replay view target |  |
| bConsiderHidden | bool | : Whether or not to hide the actor and all its components |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorEnableCollision

Allows enablingdisabling collision for the whole actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewActorEnableCollision | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorEnableCollision

Get current state of collision for the whole actor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### K2_DestroyActor

Destroy the actor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### HasAuthority

Returns whether this actor has network authority

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### AddComponent

Creates a new component and assigns ownership to the Actor this is
	  called for. Automatic attachment causes the first component created to
	  become the root, and all subsequent components to be attached under that
	  root. When bManualAttachment is set, automatic attachment is
	  skipped and it is up to the user to attach the resulting component (or
	  set it up as the root) themselves.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TemplateName | FName  |   The name of the Component Template to use. |  |
| bManualAttachment | bool  |  Whether manual or automatic attachment is to be used |  |
| RelativeTransform | FTransform &  |  The relative transform between the new component and its attach parent (automatic only) |  |
| ComponentTemplateContext | UObject * | Optional UBlueprintGeneratedClass reference to use to find the template in. If null (or not a BPGC), component is sought in this Actor's class |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent *  |  |  |

### K2_DestroyComponent

DEPRECATED - Use Component::DestroyComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UActorComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AttachRootComponentTo

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InParent | USceneComponent *  |  |  |
| InSocketName | FName  |  |  |
| AttachLocationType | EAttachLocation :: Type  | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |  |
| bWeldSimulatedBodies | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AttachToComponent

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Parent | USceneComponent *  |   Parent to attach to. |  |
| SocketName | FName  |  Optional socket to attach to on the parent. |  |
| LocationRule | EAttachmentRule  |  |  |
| RotationRule | EAttachmentRule  |  |  |
| ScaleRule | EAttachmentRule  |  |  |
| bWeldSimulatedBodies | bool | Whether to weld together simulated physics bodies. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AttachRootComponentToActor

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InParentActor | AActor *  |  |  |
| InSocketName | FName  |  |  |
| AttachLocationType | EAttachLocation :: Type  | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |  |
| bWeldSimulatedBodies | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_AttachToActor

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParentActor | AActor *  |  Actor to attach this actor's RootComponent to |  |
| SocketName | FName  |  Socket name to attach to, if any |  |
| LocationRule | EAttachmentRule  |  How to handle translation when attaching. |  |
| RotationRule | EAttachmentRule  |  How to handle rotation when attaching. |  |
| ScaleRule | EAttachmentRule  |   How to handle scale when attaching. |  |
| bWeldSimulatedBodies | bool | Whether to weld together simulated physics bodies. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SnapRootComponentTo

Snap the RootComponent of this Actor to the supplied Actor's root component, optionally at a named socket. It is not valid to call this on components that are not Registered.
	   If InSocketName == NAME_None, it will attach to origin of the InParentActor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InParentActor | AActor *  |  |  |
| InSocketName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DetachRootComponentFromParent

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bMaintainWorldPosition | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_DetachFromActor

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LocationRule | EDetachmentRule  |  How to handle translation when detaching. |  |
| RotationRule | EDetachmentRule  |  How to handle rotation when detaching. |  |
| ScaleRule | EDetachmentRule |  How to handle scale when detaching. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ActorHasTag

See if this actor contains the supplied tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetActorTimeDilation

Get CustomTimeDilation - this can be used for input control or speed control for slomo.
	  We don't want to scale input globally because input can be used for UI, which do not care for TimeDilation.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### AddTickPrerequisiteActor

Make this actor tick after PrerequisiteActor. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrerequisiteActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTickPrerequisiteComponent

Make this actor tick after PrerequisiteComponent. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrerequisiteComponent | UActorComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveTickPrerequisiteActor

Remove tick dependency on PrerequisiteActor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrerequisiteActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveTickPrerequisiteComponent

Remove tick dependency on PrerequisiteComponent.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrerequisiteComponent | UActorComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTickableWhenPaused

Gets whether this actor can tick when paused.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetTickableWhenPaused

Sets whether this actor can tick when paused.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bTickableWhenPaused | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeMIDForMaterial

Allocate a MID for a given parent material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Parent | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic *  |  |  |

### GetGameTimeSinceCreation

The number of seconds (in game time) since this Actor was created, relative to Get Game Time In Seconds.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### MakeNoise

Trigger a noise caused by a given Pawn, at a given location.
	  Note that the NoiseInstigator Pawn MUST have a PawnNoiseEmitterComponent for the noise to be detected by a PawnSensingComponent.
	  Senders of MakeNoise should have an Instigator if they are not pawns, or pass a NoiseInstigator.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Loudness | float  | The relative loudness of this noise. Usual range is 0 (no noise) to 1 (full volume). If MaxRange is used, this scales the max range, otherwise it affects the hearing range specified by the sensor. |  |
| NoiseInstigator | APawn *  | Pawn responsible for this noise. Uses the actor's Instigator if NoiseInstigator=NULL |  |
| NoiseLocation | FVector  | Position of noise source. If zero vector, use the actor's location. |  |
| MaxRange | float  | Max range at which the sound may be heard. A value of 0 indicates no max range (though perception may have its own range). Loudness scales the range. (Note: not supported for legacy PawnSensingComponent, only for AIPerception) |  |
| Tag | FName | Identifier for the noise. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveBeginPlay

Event when play begins for this actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveReInitForReplay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveFastForwardFinishedForReplay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveActorSimulatedRelevant

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsRelevant | bool  |  |  |
| bConsiderHidden | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsActorBeingDestroyed

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ReceiveAnyDamage

Event when this actor takes ANY damage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Damage | float  |  |  |
| DamageType | UDamageType *  |  |  |
| InstigatedBy | AController *  |  |  |
| DamageCauser | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveRadialDamage

Event when this actor takes RADIAL damage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DamageReceived | float  |  |  |
| DamageType | UDamageType *  |  |  |
| Origin | FVector  |  |  |
| HitInfo | FHitResult &  |  |  |
| InstigatedBy | AController *  |  |  |
| DamageCauser | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceivePointDamage

Event when this actor takes POINT damage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Damage | float  |  |  |
| DamageType | UDamageType *  |  |  |
| HitLocation | FVector  |  |  |
| HitNormal | FVector  |  |  |
| HitComponent | UPrimitiveComponent *  |  |  |
| BoneName | FName  |  |  |
| ShotFromDirection | FVector  |  |  |
| InstigatedBy | AController *  |  |  |
| DamageCauser | AActor *  |  |  |
| HitInfo | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveTick

Event called every frame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaSeconds | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorBeginOverlap

Event when this actor overlaps another actor, for example a player walking into a trigger.
	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorEndOverlap

Event when an actor no longer overlaps another actor, and they have separated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorBeginCursorOver

Event when this actor has the mouse moved over it with the clickable interface.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveActorEndCursorOver

Event when this actor has the mouse moved off of it with the clickable interface.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveActorOnClicked

Event when this actor is clicked by the mouse when using the clickable interface.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ButtonPressed | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorOnReleased

Event when this actor is under the mouse when left mouse button is released while using the clickable interface.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ButtonReleased | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorOnInputTouchBegin

Event when this actor is touched when click events are enabled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorOnInputTouchEnd

Event when this actor is under the finger when untouched when click events are enabled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorOnInputTouchEnter

Event when this actor has a finger moved over it with the clickable interface.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActorOnInputTouchLeave

Event when this actor has a finger moved off of it with the clickable interface.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOverlappingActors

Returns list of actors this actor is overlapping (any component overlapping any component). Does not return itself.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverlappingActors | TArray < AActor * > &  | [out] Returned list of overlapping actors |  |
| ClassFilter | TSubclassOf < AActor > |  [optional] If set, only returns actors of this class or subclasses |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOverlappingComponents

Returns list of components this actor is overlapping.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverlappingComponents | TArray < UPrimitiveComponent * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveHit

Event when this actor bumps into a blocking object, or blocks another actor that bumps into it.
	  This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
	  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyComp | UPrimitiveComponent *  |  |  |
| Other | AActor *  |  |  |
| OtherComp | UPrimitiveComponent *  |  |  |
| bSelfMoved | bool  |  |  |
| HitLocation | FVector  |  |  |
| HitNormal | FVector  |  |  |
| NormalImpulse | FVector  |  |  |
| Hit | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLifeSpan

Set the lifespan of this actor. When it expires the object will be destroyed. If requested lifespan is 0, the timer is cleared and the actor will not be destroyed.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLifespan | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLifeSpan

Get the remaining lifespan of this actor. If zero is returned the actor lives forever.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### UserConstructionScript

Construction script, the place to spawn components and do other setup.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveDestroyed

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveEndPlay

Event to notify blueprints this actor is about to be deleted.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndPlayReason | EEndPlayReason :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorTickEnabled

Set this actor's tick functions to be enabled or disabled. Only has an effect if the function is registered
	  This only modifies the tick function on actor itself

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool | Whether it should be enabled or not |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsActorTickEnabled

Returns whether this actor has tick enabled or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetActorTickInterval

Sets the tick interval of this actor's primary tick function. Will not enable a disabled tick function. Takes effect on next tick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TickInterval | float | The rate at which this actor should be ticking |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorTickInterval

Returns the tick interval of this actor's primary tick function

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### OnRep_ReplicatedMovement

ReplicatedMovement struct replication event

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetOwner

Set the owner of this Actor, used primarily for network replication.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewOwner | AActor * | The Actor whom takes over ownership of this Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOwner

Get the owner of this Actor, used primarily for network replication.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * | Actor that owns this Actor |  |

### IsOverlappingActor

Check whether any component of this Actor is overlapping any component of another Actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Other | AActor * | The other Actor to test against |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether any component of this Actor is overlapping any component of another Actor. |  |

### SetNetDormancy

Puts actor in dormant networking state

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDormancy | ENetDormancy |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushNetDormancy

Forces dormant actor to replicate but doesn't change NetDormancy state (i.e., they will go dormant again if left dormant)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsChildActor

Returns whether this Actor was spawned by a child actor component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetAllChildActors

Returns a list of all child actors, including children of children

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ChildActors | TArray < AActor * > &  |  |  |
| bIncludeDescendants | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetParentComponent

If this Actor was created by a Child Actor Component returns that Child Actor Component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UChildActorComponent * |  |  |

### GetParentActor

If this Actor was created by a Child Actor Component returns the Actor that owns that Child Actor Component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### K2_TeleportTo

Teleport this actor to a new location. If the actor doesn't fit exactly at the location specified, tries to slightly move it out of walls and such.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DestLocation | FVector  | The target destination point |  |
| DestRotation | FRotator | The target rotation at the destination |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the actor has been successfully moved, or false if it couldn't fit. |  |

### GetLevelName

Return the ULevel name that this Actor is part of.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetAttachParentActor

Walk up the attachment chain from RootComponent until we encounter a different actor, and return it. If we are not attached to a component in a different actor, returns NULL

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### GetAttachParentSocketName

Walk up the attachment chain from RootComponent until we encounter a different actor, and return the socket name in the component. If we are not attached to a component in a different actor, returns NAME_None

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName |  |  |

### GetAttachedActors

Find all Actors which are attached directly to a component in this actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTickGroup

Sets the ticking group for this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTickGroup | ETickingGroup | the new value to assign |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CanBeBaseForCharacter

Return true if the given Pawn can be "based" on this actor (ie walk on it).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pawn | APawn * | - The pawn that wants to be based on this actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetAnimNotifyStateBoneRetargetAdaptInfoObj

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimNotifyStateBoneRetargetAdaptInfoObj * |  |  |

### TryGetBoneRetargetObj

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSourceObj | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### TryGetBoneRetargetObjForNotifyState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetNotifyState | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### InitAnimNotifyStateBoneRetargetInfo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetNotifyState | UObject *  |  |  |
| InBoneRetargetObj | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAnimNotifyStateBoneRetargetAdaptState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetNotifyState | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsAnimNotifyStateBoneRetargetAdaptInitDone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetNotifyState | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### OverrideNotifyAttachMesh

For Bone Retarget Feature End

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetNotifyState | UObject *  |  |  |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| HasRetarget | bool  |  |  |
| IgnoreNewFPPState | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USkeletalMeshComponent *  |  |  |

### K2_OnBecomeViewTarget

Event called when this Actor becomes the view target for the given PlayerController.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PC | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnEndViewTarget

Event called when this Actor is no longer the view target for the given PlayerController.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PC | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnReset

Event called when this Actor is reset to its initial state - used when restarting level without reloading.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### WasRecentlyRendered

Returns true if this actor has been rendered "recently", with a tolerance in seconds to define what "recent" means.
	  e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tolerance | float | How many seconds ago the actor last render time can be and still count as having been "recently" rendered. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether this actor was recently rendered. |  |

### ForceNetRelevant

Forces this actor to be net relevant if it is not already by default

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ForceNetConsider

Force actor enter consider list

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ForceNetComponentUpdate

Force actor's component to be updated to client

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InComponent | UActorComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ForceNetUpdate

Force actor to be updated to clients

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PrestreamTextures

Calls PrestreamTextures() for all the actor's meshcomponents.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Seconds | float  | - Number of seconds to force all mip-levels to be resident |  |
| bEnableStreaming | bool  | - Whether to start (true) or stop (false) streaming |  |
| CinematicTextureGroups | int32 | - Bitfield indicating which texture groups that use extra high-resolution mips |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTextureForceResidentFlag

Calls SetTextureForceResidentFlag() for all the actor's meshcomponents.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bForceMiplevelsToBeResident | bool | Whether textures should be forced to be resident or not. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorEyesViewPoint

Returns the point of view of the actor.
	  Note that this doesn't mean the camera, but the 'eyes' of the actor.
	  For example, for a Pawn, this would define the eye height location,
	  and view rotation (which is different from the pawn rotation which has a zeroed pitch component).
	  A camera first person view will typically use this view point. Most traces (weapon, AI) will be done from this view point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutLocation | FVector &  | - location of view point |  |
| OutRotation | FRotator & | - view rotation of actor. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetComponentByClass

Script exposed version of FindComponentByClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ComponentClass | TSubclassOf < UActorComponent > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent *  |  |  |

### GetComponentsByClass

Gets all the components that inherit from the given class.
	Currently returns an array of UActorComponent which must be cast to the correct type.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ComponentClass | TSubclassOf < UActorComponent > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UActorComponent * >  |  |  |

### GetComponentsByTag

Gets all the components that inherit from the given class with a given tag.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ComponentClass | TSubclassOf < UActorComponent >  |  |  |
| Tag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UActorComponent * >  |  |  |

### SetGeneralCampID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetGeneralCampID

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetGeneralCampName

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetGeneralCampRelationWithCampID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CampID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECampRelation  |  |  |

### GetGeneralCampRelationWithActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECampRelation  |  |  |

### AllowTriggerDeformEffect

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Origin | FVector &  |  |  |
| EffectRange | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TriggerDeformEffect

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Origin | FVector &  |  |  |
| EffectRange | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableDeformEffect

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### MarkSubObjectDeleteDirty

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsHiddenEdAtStartup

Simple accessor to check if the actor is hidden upon editor startup

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the actor is hidden upon editor startup; false if it is not |  |

### IsHiddenEd

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetIsTemporarilyHiddenInEditor

Sets whether or not this actor is hidden in the editor for the duration of the current editor session

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsHidden | bool | True if the actor is hidden |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsTemporarilyHiddenInEditor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIncludeParent | bool | - Whether to recurse up child actor hierarchy or not |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether or not this actor is hidden in the editor for the duration of the current editor session |  |

### IsEditable

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | Returns true if this actor is allowed to be displayed, selected and manipulated by the editor. |  |

### IsSelectable

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | Returns true if this actor can EVER be selected in a level in the editor.  Can be overridden by specific actors to make them unselectable. |  |

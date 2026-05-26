# UActorComponent

- Symbol Type: class
- Symbol Path: Others / UActorComponent
- Source JSON Path: class/detail/Others/UActorComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UActorComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

ActorComponent is the base class for components that define reusable behavior that can be added to different types of Actors.
  ActorComponents that have a transform are known as SceneComponents and those that can be rendered are PrimitiveComponents.
 
  @see USceneComponent
  @see UPrimitiveComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryComponentTick | FActorComponentTickFunction | Main tick function for the Actor |  |
| DSTickInterval | float | The frequency in seconds at which this tick function will be executed on DS.  If less than or equal to 0 then it will tick every frame<br>	 If greater than 0 will cover PrimaryComponentTick.TickInterval<br>	 Add by zoranouyang |  |
| ComponentTags | TArray < FName > | Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting. |  |
| NetUpdateFrequency | float |  |  |
| bAllowBPReceiveTickEvent | bool | If true, bp tick will be called , otherwise skipped |  |
| TickAdapterIntvlOverride | uint8 |  |  |
| bSyncOwnerTickAdapter | uint8 |  |  |
| ScriptNetworkReplicatedPropertyWrapper | FScriptNetworkReplicatedPropertyWrapper |  |  |
| bSupportSuspendTick | uint8 |  |  |
| bDestroyIfOnClientNoLocalControl | uint8 |  |  |
| bReplicates | uint8 | Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first! |  |
| bNetAddressable | uint8 | Is this component safe to ID over the network by name? |  |
| bDeferedConstructComponent | uint8 |  |  |
| bSkipNewDuplicateComponent | uint8 |  |  |
| bNameStableForBackupRestore | uint8 |  |  |
| bNeedBackupRestoreForCustomSerialize | uint8 |  |  |
| bEnableTickWhenOutOfRegion | uint8 | If true, this component will Enale Tick when out of region. |  |
| bAutoActivate | uint8 | Whether the component is activated at creation or must be explicitly activated. |  |
| bIsActive | uint8 | Whether the component is currently active. |  |
| bEditableWhenInherited | uint8 |  |  |
| bCanEverAffectNavigation | uint8 | Whether this component can potentially influence navigation |  |
| bIsEditorOnly | uint8 | If true, the component will be excluded from non-editor builds |  |
| bNeedsLoadForClient | uint8 | If false, the component will be excluded from client builds |  |
| bNeedsLoadForServer | uint8 | If false, the component will be excluded from server builds |  |
| bAllowRenderDataUpdateLag | uint8 |  |  |
| CreationMethod | EComponentCreationMethod |  |  |
| UCSModifiedProperties | TArray < FSimpleMemberReference > |  |  |
| AssetUserData | TArray < UAssetUserData * > | Array of user data stored with the component |  |
| bCreatedByConstructionScript_DEPRECATED | uint8 | True if this component was created by a construction script, and will be destroyed by DestroyConstructedComponents |  |
| bInstanceComponent_DEPRECATED | uint8 | True if this component was created as an instance component |  |

## Functions

### GetToString

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### ForceNetUpdate

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

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

### IsBeingDestroyed

Returns whether the component is in the process of being destroyed.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### OnRep_Replicates

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_IsActive

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetOwner

Follow the Outer chain to get the  AActor  that 'Owns' this component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### ComponentHasTag

See if this component contains the supplied tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Activate

Activates the SceneComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bReset | bool | - The value to assign to HiddenGame. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Deactivate

Deactivates the SceneComponent.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetActive

Sets whether the component is active or not

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewActive | bool  | - The new active state of the component |  |
| bReset | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ToggleActive

Toggles the active state of the component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsActive

Returns whether the component is active or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | - The active state of the component. |  |

### SetAutoActivate

Sets whether the component should be auto activate or not. Only safe during construction scripts.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewAutoActivate | bool | - The new auto activate state of the component |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTickableWhenPaused

Sets whether this component can tick when paused.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bTickableWhenPaused | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIsReplicated

Enable or disable replication. This is the equivalent of RemoteRole for actors (only a bool is required for components)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShouldReplicate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveBeginPlay

Blueprint implementable event for when the component is beginning play, called before its Owner's BeginPlay on Actor BeginPlay
	  or when the component is dynamically created if the Actor has already BegunPlay.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveEndPlay

Blueprint implementable event for when the component ends play, generally via destruction or its Actor's EndPlay.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndPlayReason | EEndPlayReason :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetComponentTickEnabled

Set this component's tick functions to be enabled or disabled. Only has an effect if the function is registered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool | - Whether it should be enabled or not |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsComponentTickEnabled

Returns whether this component has tick enabled or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsComponentTickEnabledByExternal

Returns whether this component has tick enabled or not,
	  Which set by External business

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetComponentTickInterval

Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect on next tick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TickInterval | float | The duration between ticks for this component's primary tick function |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetComponentTickInterval

Returns whether this component has tick enabled or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### K2_DestroyComponent

Unregister and mark for pending kill a component.  This may not be used to destroy a component that is owned by an actor unless the owning actor is calling the function.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTickGroup

Changes the ticking group for this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTickGroup | ETickingGroup |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTickPrerequisiteActor

Make this component tick after PrerequisiteActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrerequisiteActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTickPrerequisiteComponent

Make this component tick after PrerequisiteComponent.

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

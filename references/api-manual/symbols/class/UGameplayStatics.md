# UGameplayStatics

- Symbol Type: class
- Symbol Path: 引擎 / 常用全局类 / UGameplayStatics
- Source JSON Path: class/detail/引擎/常用全局类/UGameplayStatics.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UGameplayStatics.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Functions

### SpawnObject

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectClass | TSubclassOf < UObject >  |  |  |
| Outer | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### BeginSpawningActorFromBlueprint

生成指定蓝图类的实例，但不自动执行构造函数

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| Blueprint | UBlueprint *  | 蓝图类 |  |
| SpawnTransform | FTransform &  | 生成Actor的Transform | cppstruct/detail/FTransform.json |
| bNoCollisionFail | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  | Actor实例 |  |

### BeginSpawningActorFromClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ActorClass | TSubclassOf < AActor >  |  |  |
| SpawnTransform | FTransform &  |  | cppstruct/detail/FTransform.json |
| bNoCollisionFail | bool  |  |  |
| Owner | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  |  |

### BeginDeferredActorSpawnFromClass

Spawns an instance of an actor class, but does not automatically run its construction script.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ActorClass | TSubclassOf < AActor >  |  |  |
| SpawnTransform | FTransform &  |  | cppstruct/detail/FTransform.json |
| CollisionHandlingOverride | ESpawnActorCollisionHandlingMethod  |  |  |
| Owner | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  |  |

### FinishSpawningActor

结束生成Actor，执行Actor的构造函数

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  | Actor实例 |  |
| SpawnTransform | FTransform & | 生成Actor的Transform | cppstruct/detail/FTransform.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  | Actor实例 |  |

### GetActorArrayAverageLocation

Find the average location (centroid) of an array of Actors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  | cppstruct/detail/FVector.json |

### GetActorArrayBounds

Bind the bounds of an array of Actors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actors | TArray < AActor * > &  |  |  |
| bOnlyCollidingComponents | bool  |  |  |
| Center | FVector &  |  | cppstruct/detail/FVector.json |
| BoxExtent | FVector & |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllActorsOfClass

Find all Actors in the world of the specified class.
	 	This is a slow operation, use with caution e.g. do not use every frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ActorClass | TSubclassOf < AActor >  | Class of Actor to find. Must be specified or result array will be empty. |  |
| OutActors | TArray < AActor * > & | Output array of Actors of the specified class. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFirstActorOfClass

Find one Actor in the world of the specified class.
		This is a slow operation, use with caution e.g. do not use every frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ActorClass | TSubclassOf < AActor > | Class of Actor to find. Must be specified or result array will be empty. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  |  |

### GetAllActorsWithInterface

Find all Actors in the world with the specified interface.
	 	This is a slow operation, use with caution e.g. do not use every frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Interface | TSubclassOf < UInterface >  | Interface to find. Must be specified or result array will be empty. |  |
| OutActors | TArray < AActor * > & | Output array of Actors of the specified interface. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllActorsWithTag

获取拥有指定Tag的所有Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| Tag | FName  | Tag名称 |  |
| OutActors | TArray < AActor * > & | 输出的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetGameInstance

获取GameInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameInstance *  | GameInstance |  |

### GetCurrentGameInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameInstance * |  |  |

### GetPlayerController

获取PlayerController

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| PlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController *  | PlayerController |  |

### GetPlayerPawn

获取PlayerPawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| PlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn *  | PlayerPawn |  |

### GetPlayerCharacter

获取PlayerCharacter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| PlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ACharacter *  | PlayerCharacter |  |

### GetPlayerCameraManager

获取PlayerCameraManager

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| PlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerCameraManager *  | PlayerCameraManager |  |

### CreatePlayer

Create a new player for this game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ControllerId | int32  | The ID of the controller that the should control the newly created player. A value of -1 specifies to use the next available ID |  |
| bSpawnPawn | bool | Whether a pawn should be spawned immediately. If false a pawn will not be created until transition to the next map. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController *  |  |  |

### RemovePlayer

Removes a player from this game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController *  |  The player controller of the player to be removed |  |
| bDestroyPawn | bool | Whether the controlled pawn should be deleted as well |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlayerControllerID

Gets what controller ID a Player is using

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController * | The player controller of the player to get the ID of |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | 		The ID of the passed in player. -1 if there is no controller for the passed in player |  |

### SetPlayerControllerID

Sets what controller ID a Player should be using

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController *  |  The player controller of the player to change the controller ID of |  |
| ControllerId | int32 | The controller ID to assign to this player |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### LoadStreamLevel

加载子关卡

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| LevelName | FName  | 子关卡名称 |  |
| bMakeVisibleAfterLoad | bool  | 加载后是否显示 |  |
| bShouldBlockOnLoad | bool  | 加载时是否阻塞 |  |
| LatentInfo | FLatentActionInfo | 回调信息结构 | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnloadStreamLevel

加载子关卡

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| LevelName | FName  | 子关卡名称 |  |
| LatentInfo | FLatentActionInfo | 回调信息结构 | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStreamingLevel

Returns level streaming object with specified level package name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PackageName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULevelStreaming *  |  |  |

### FlushLevelStreaming

刷新关卡流，直到所有子关卡加载完毕时返回

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushLevelStreamingBasedOnCharacterLocation

更新玩家的位置，触发LevelBounds，然后加载所有关卡

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| CharacterLocation | FVector |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushAllStreamingResource

触发TextureStreaming， 将贴图全部加载完毕

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CancelAsyncLoading

Cancels all currently queued streaming packages

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OpenLevel

Travel to another level

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LevelName | FName  |  the level to open |  |
| bAbsolute | bool  |  if true options are reset, if false options are carried over from current level |  |
| Options | FString |  a string of options to use for the travel URL |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OpenShaderLibrary

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FString &  |  |  |
| VersionNum | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CloseShaderLibrary

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableShaderGroup

Enable a new ShaderGroup for all opened ShaderCodeLibrary

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GroupName | FString &  |  |  |
| ShaderPlatform | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableShaderLevel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShaderLevelName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableShaderPak

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShaderPakName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableShaderLevel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShaderLevelName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableShaderPak

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShaderPakName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RestartShaderPrecompile

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OpenShaderCodeLibrary

OpenShaderCodeLibrary in Saved Folder

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Version | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentLevelName

获得当前关卡名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| bRemovePrefixString | bool | 是否移除prefix的字符串 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 关卡名称 |  |

### GetGameMode

获得当前GameMode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AGameModeBase *  | 当前GameMode |  |

### GetGameState

获得当前GameState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AGameStateBase *  | 当前GameState |  |

### GetGameStateByWorldContext

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AGameStateBase *  |  |  |

### GetObjectClass

获得对象的类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * | 指定对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  | 对象的类型 |  |

### GetGlobalTimeDilation

获得当前时间膨胀

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | Current time dilation. |  |

### SetGlobalTimeDilation

设置时间膨胀

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| TimeDilation | float | 世界的时间膨胀 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetGamePaused

设置游戏是否暂停

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| bPaused | bool | 是否暂停 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the game was successfully pausedunpaused |  |

### IsGamePaused

判断游戏是否暂停

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the game is currently paused or not |  |

### ApplyRadialDamage

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| BaseDamage | float  | - The base damage to apply, i.e. the damage at the origin. |  |
| Origin | FVector &  | - Epicenter of the damage area. | cppstruct/detail/FVector.json |
| DamageRadius | float  | - Radius of the damage area, from Origin |  |
| DamageTypeClass | TSubclassOf < UDamageType >  | - Class that describes the damage that was done. |  |
| IgnoreActors | TArray < AActor * > &  |  |  |
| DamageCauser | AActor *  | - Actor that actually caused the damage (e.g. the grenade that exploded). This actor will not be damaged and it will not block damage. |  |
| InstigatedByController | AController *  | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |  |
| bDoFullDamage | bool  |  |  |
| DamagePreventionChannel | ECollisionChannel  | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |  |
| DamageTag | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if damage was applied to at least one actor. |  |

### ApplyRadialDamageWithFalloff

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| BaseDamage | float  | - The base damage to apply, i.e. the damage at the origin. |  |
| MinimumDamage | float  |  |  |
| Origin | FVector &  | - Epicenter of the damage area. | cppstruct/detail/FVector.json |
| DamageInnerRadius | float  | - Radius of the full damage area, from Origin |  |
| DamageOuterRadius | float  | - Radius of the minimum damage area, from Origin |  |
| DamageFalloff | float  | - Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius |  |
| DamageTypeClass | TSubclassOf < UDamageType >  | - Class that describes the damage that was done. |  |
| IgnoreActors | TArray < AActor * > &  |  |  |
| DamageCauser | AActor *  | - Actor that actually caused the damage (e.g. the grenade that exploded) |  |
| InstigatedByController | AController *  | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |  |
| DamagePreventionChannel | ECollisionChannel  | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |  |
| DamageTag | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if damage was applied to at least one actor. |  |

### ApplyPointDamage

Hurts the specified actor with the specified impact.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DamagedActor | AActor *  | - Actor that will be damaged. |  |
| BaseDamage | float  | - The base damage to apply. |  |
| HitFromDirection | FVector &  | - Direction the hit came FROM | cppstruct/detail/FVector.json |
| HitInfo | FHitResult &  | - Collision or trace result that describes the hit | cppstruct/detail/FHitResult.json |
| EventInstigator | AController *  | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |  |
| DamageCauser | AActor *  | - Actor that actually caused the damage (e.g. the grenade that exploded) |  |
| DamageTypeClass | TSubclassOf < UDamageType >  | - Class that describes the damage that was done. |  |
| DamageTag | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | Actual damage the ended up being applied to the actor. |  |

### ApplyDamage

Hurts the specified actor with generic damage.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DamagedActor | AActor *  | - Actor that will be damaged. |  |
| BaseDamage | float  | - The base damage to apply. |  |
| EventInstigator | AController *  | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |  |
| DamageCauser | AActor *  | - Actor that actually caused the damage (e.g. the grenade that exploded) |  |
| DamageTypeClass | TSubclassOf < UDamageType >  | - Class that describes the damage that was done. |  |
| DamageTag | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | Actual damage the ended up being applied to the actor. |  |

### PlayWorldCameraShake

Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | - Object that we can obtain a world context from |  |
| Shake | TSubclassOf < UCameraShake >  | - Camera shake asset to use |  |
| Epicenter | FVector  | - location to place the effect in world space | cppstruct/detail/FVector.json |
| InnerRadius | float  | - Cameras inside this radius are ignored |  |
| OuterRadius | float  | - Cameras outside of InnerRadius and inside this are effected |  |
| Falloff | float  | - Affects falloff of effect as it nears OuterRadius |  |
| bOrientShakeTowardsEpicenter | bool | - Changes the rotation of shake to point towards epicenter instead of forward |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnEmitterAtLocation

Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | - Object that we can obtain a world context from |  |
| EmitterTemplate | UParticleSystem *  | - particle system to create |  |
| Location | FVector  | - location to place the effect in world space | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - rotation to place the effect in world space | cppstruct/detail/FRotator.json |
| Scale | FVector  | - scale to create the effect at | cppstruct/detail/FVector.json |
| bAutoDestroy | bool | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UParticleSystemComponent *  |  |  |

### SpawnEmitterAttached

Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EmitterTemplate | UParticleSystem *  | - particle system to create |  |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  | - Optional named point within the AttachComponent to spawn the emitter at |  |
| Location | FVector  | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition). | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition). | cppstruct/detail/FRotator.json |
| Scale | FVector  | - Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition). | cppstruct/detail/FVector.json |
| LocationType | EAttachLocation :: Type  | - Specifies whether Location is a relative offset or an absolute world position |  |
| bAutoDestroy | bool | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UParticleSystemComponent *  |  |  |

### SpawnEmitterAttachedToActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EmitterTemplate | UParticleSystem *  |  |  |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  |  |  |
| Location | FVector  |  | cppstruct/detail/FVector.json |
| Rotation | FRotator  |  | cppstruct/detail/FRotator.json |
| Scale | FVector  |  | cppstruct/detail/FVector.json |
| LocationType | EAttachLocation :: Type  |  |  |
| bAutoDestroy | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UParticleSystemComponent *  |  |  |

### AreAnyListenersWithinRange

Determines if any audio listeners are within range of the specified location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Location | FVector  | The location to potentially play a sound at | cppstruct/detail/FVector.json |
| MaximumRange | float | The maximum distance away from Location that a listener can be |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetGlobalPitchModulation

Sets a global pitch modulation scalar that will apply to all non-UI sounds
	
	  Fire and Forget.
	  Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PitchModulation | float  | - A pitch modulation value to globally set. |  |
| TimeSec | float | - A time value to linearly interpolate the global modulation pitch over from it's current value. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetGlobalListenerFocusParameters

Sets the global listener focus parameters which will scale focus behavior of sounds based on their focus azimuth settings in their attenuation settings.
	
	  Fire and Forget.
	  Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| FocusAzimuthScale | float  | - An angle scale value used to scale the azimuth angle that defines where sounds are in-focus. |  |
| NonFocusAzimuthScale | float  |  |  |
| FocusDistanceScale | float  | - A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |  |
| NonFocusDistanceScale | float  | - A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |  |
| FocusVolumeScale | float  |  |  |
| NonFocusVolumeScale | float  |  |  |
| FocusPriorityScale | float  | - A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds. |  |
| NonFocusPriorityScale | float | - A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of out-of-focus sounds. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlaySound2D

Plays a sound directly with no attenuation, perfect for UI sounds.
	 
	   Fire and Forget.
	   Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sound | USoundBase *  | - Sound to play. |  |
| VolumeMultiplier | float  | - Multiplied with the volume to make the sound louder or softer. |  |
| PitchMultiplier | float  | - Multiplies the pitch. |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| OwningActor | AActor * | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnSound2D

Spawns a sound with no attenuation, perfect for UI sounds.
	 
	   Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sound | USoundBase *  | - Sound to play. |  |
| VolumeMultiplier | float  | - Multiplied with the volume to make the sound louder or softer. |  |
| PitchMultiplier | float  | - Multiplies the pitch. |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| bPersistAcrossLevelTransition | bool  |  |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | An audio component to manipulate the spawned sound |  |

### CreateSound2D

Creates a sound with no attenuation, perfect for UI sounds. This does NOT play the sound
	 
	   Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sound | USoundBase *  | - Sound to create. |  |
| VolumeMultiplier | float  | - Multiplied with the volume to make the sound louder or softer. |  |
| PitchMultiplier | float  | - Multiplies the pitch. |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| bPersistAcrossLevelTransition | bool  |  |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | An audio component to manipulate the created sound |  |

### PlaySoundAtLocation

Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sound | USoundBase *  | - sound to play |  |
| Location | FVector  | - World position to play sound at | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - World rotation to play sound at | cppstruct/detail/FRotator.json |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - PitchMultiplier |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| AttenuationSettings | USoundAttenuation *  | - Override attenuation settings package to play sound with |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| OwningActor | AActor * | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnSoundAtLocation

Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sound | USoundBase *  | - sound to play |  |
| Location | FVector  | - World position to play sound at | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - World rotation to play sound at | cppstruct/detail/FRotator.json |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - PitchMultiplier |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| AttenuationSettings | USoundAttenuation *  | - Override attenuation settings package to play sound with |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | An audio component to manipulate the spawned sound |  |

### SpawnSoundAttached

Plays a sound attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sound | USoundBase *  | - sound to play |  |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  | - Optional named point within the AttachComponent to play the sound at |  |
| Location | FVector  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset | cppstruct/detail/FRotator.json |
| LocationType | EAttachLocation :: Type  | - Specifies whether Location is a relative offset or an absolute world position |  |
| bStopWhenAttachedToDestroyed | bool  | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |  |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - PitchMultiplier |  |
| StartTime | float  | - How far in to the sound to begin playback at |  |
| AttenuationSettings | USoundAttenuation *  | - Override attenuation settings package to play sound with |  |
| ConcurrencySettings | USoundConcurrency *  | - Override concurrency settings package to play sound with |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | An audio component to manipulate the spawned sound |  |

### PlayDialogue2D

Plays a dialogue directly with no attenuation, perfect for UI.
	 
	   Fire and Forget.
	   Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Dialogue | UDialogueWave *  | - dialogue to play |  |
| Context | FDialogueContext &  | - context the dialogue is to play in | cppstruct/detail/FDialogueContext.json |
| VolumeMultiplier | float  | - Multiplied with the volume to make the sound louder or softer. |  |
| PitchMultiplier | float  | - Multiplies the pitch. |  |
| StartTime | float | - How far in to the dialogue to begin playback at |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnDialogue2D

Spawns a dialogue with no attenuation, perfect for UI.
	 
	   Not Replicated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Dialogue | UDialogueWave *  | - dialogue to play |  |
| Context | FDialogueContext &  | - context the dialogue is to play in | cppstruct/detail/FDialogueContext.json |
| VolumeMultiplier | float  | - Multiplied with the volume to make the sound louder or softer. |  |
| PitchMultiplier | float  | - Multiplies the pitch. |  |
| StartTime | float  | - How far in to the dialogue to begin playback at |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | An audio component to manipulate the spawned sound |  |

### PlayDialogueAtLocation

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Dialogue | UDialogueWave *  | - dialogue to play |  |
| Context | FDialogueContext &  | - context the dialogue is to play in | cppstruct/detail/FDialogueContext.json |
| Location | FVector  | - World position to play dialogue at | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - World rotation to play dialogue at | cppstruct/detail/FRotator.json |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - Pitch multiplier |  |
| StartTime | float  | - How far in to the dialogue to begin playback at |  |
| AttenuationSettings | USoundAttenuation * | - Override attenuation settings package to play sound with |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnDialogueAtLocation

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Dialogue | UDialogueWave *  | - dialogue to play |  |
| Context | FDialogueContext &  | - context the dialogue is to play in | cppstruct/detail/FDialogueContext.json |
| Location | FVector  | - World position to play dialogue at | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - World rotation to play dialogue at | cppstruct/detail/FRotator.json |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - PitchMultiplier |  |
| StartTime | float  | - How far in to the dialogue to begin playback at |  |
| AttenuationSettings | USoundAttenuation *  | - Override attenuation settings package to play sound with |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | Audio Component to manipulate the playing dialogue with |  |

### SpawnDialogueAttached

Spawns a dialogue attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Dialogue | UDialogueWave *  | - dialogue to play |  |
| Context | FDialogueContext &  | - context the dialogue is to play in | cppstruct/detail/FDialogueContext.json |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  | - Optional named point within the AttachComponent to play the sound at |  |
| Location | FVector  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset | cppstruct/detail/FRotator.json |
| LocationType | EAttachLocation :: Type  | - Specifies whether Location is a relative offset or an absolute world position |  |
| bStopWhenAttachedToDestroyed | bool  | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |  |
| VolumeMultiplier | float  | - Volume multiplier |  |
| PitchMultiplier | float  | - PitchMultiplier |  |
| StartTime | float  | - How far in to the dialogue to begin playback at |  |
| AttenuationSettings | USoundAttenuation *  | - Override attenuation settings package to play sound with |  |
| bAutoDestroy | bool | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAudioComponent *  | Audio Component to manipulate the playing dialogue with |  |

### SpawnForceFeedbackAtLocation

Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ForceFeedbackEffect | UForceFeedbackEffect *  | - effect to play |  |
| Location | FVector  | - World position to center the effect at | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - World rotation to center the effect at | cppstruct/detail/FRotator.json |
| bLooping | bool  |  |  |
| IntensityMultiplier | float  | - Intensity multiplier |  |
| StartTime | float  | - How far in to the feedback effect to begin playback at |  |
| AttenuationSettings | UForceFeedbackAttenuation *  | - Override attenuation settings package to play effect with |  |
| bAutoDestroy | bool | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UForceFeedbackComponent *  | Force Feedback Component to manipulate the playing feedback effect with |  |

### SpawnForceFeedbackAttached

Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ForceFeedbackEffect | UForceFeedbackEffect *  | - effect to play |  |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  | - Optional named point within the AttachComponent to attach to |  |
| Location | FVector  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset | cppstruct/detail/FRotator.json |
| LocationType | EAttachLocation :: Type  | - Specifies whether Location is a relative offset or an absolute world position |  |
| bStopWhenAttachedToDestroyed | bool  | - Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed. |  |
| bLooping | bool  |  |  |
| IntensityMultiplier | float  | - Intensity multiplier |  |
| StartTime | float  | - How far in to the feedback effect to begin playback at |  |
| AttenuationSettings | UForceFeedbackAttenuation *  | - Override attenuation settings package to play effect with |  |
| bAutoDestroy | bool | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UForceFeedbackComponent *  | Force Feedback Component to manipulate the playing feedback effect with |  |

### SetSubtitlesEnabled

Will set subtitles to be enabled or disabled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool | will enable subtitle drawing if true, disable if false. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AreSubtitlesEnabled

Returns whether or not subtitles are currently enabled.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if subtitles are enabled. |  |

### SetBaseSoundMix

Set the sound mix of the audio system for special EQing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InSoundMix | USoundMix * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSoundMixClassOverride

Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix, the sound class adjustment will be added to the sound mix.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InSoundMixModifier | USoundMix *  | The sound mix to modify. |  |
| InSoundClass | USoundClass *  | The sound class to override (or add) in the sound mix. |  |
| Volume | float  | The volume scale to set the sound class adjuster to. |  |
| Pitch | float  | The pitch scale to set the sound class adjuster to. |  |
| FadeInTime | float  | The interpolation time to use to go from the current sound class adjuster values to the new values. |  |
| bApplyToChildren | bool | Whether or not to apply this override to the sound class' children or to just the specified sound class. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearSoundMixClassOverride

Clears the override of the sound class adjuster in the given sound mix. If the override did not exist in the sound mix, this will do nothing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InSoundMixModifier | USoundMix *  | The sound mix to modify. |  |
| InSoundClass | USoundClass *  | The sound class to override (or add) in the sound mix. |  |
| FadeOutTime | float | The interpolation time to use to go from the current sound class adjuster override values to the non-override values. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PushSoundMixModifier

Push a sound mix modifier onto the audio system

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InSoundMixModifier | USoundMix * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PopSoundMixModifier

Pop a sound mix modifier from the audio system

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InSoundMixModifier | USoundMix * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearSoundMixModifiers

Clear all sound mix modifiers from the audio system

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ActivateReverbEffect

Activates a Reverb Effect without the need for a volume

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ReverbEffect | UReverbEffect *  | Reverb Effect to use |  |
| TagName | FName  | Tag to associate with Reverb Effect |  |
| Priority | float  | Priority of the Reverb Effect |  |
| Volume | float  | Volume level of Reverb Effect |  |
| FadeTime | float | Time before Reverb Effect is fully active |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DeactivateReverbEffect

Deactivates a Reverb Effect not applied by a volume

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| TagName | FName | Tag associated with Reverb Effect to remove |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentReverbEffect

Returns the highest priority reverb settings currently active from any source (volumes or manual setting).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UReverbEffect *  |  |  |

### SpawnDecalAtLocation

Spawns a decal at the given location and rotation, fire and forget. Does not replicate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| DecalMaterial | UMaterialInterface *  | - decal's material |  |
| DecalSize | FVector  | - size of decal | cppstruct/detail/FVector.json |
| Location | FVector  | - location to place the decal in world space | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - rotation to place the decal in world space | cppstruct/detail/FRotator.json |
| LifeSpan | float | - destroy decal component after time runs out (0 = infinite) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UDecalComponent *  |  |  |

### SpawnDecalAttached

Spawns a decal attached to and following the specified component. Does not replicate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DecalMaterial | UMaterialInterface *  | - decal's material |  |
| DecalSize | FVector  | - size of decal | cppstruct/detail/FVector.json |
| AttachToComponent | USceneComponent *  |  |  |
| AttachPointName | FName  | - Optional named point within the AttachComponent to spawn the emitter at |  |
| Location | FVector  | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset | cppstruct/detail/FVector.json |
| Rotation | FRotator  | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a realative offset | cppstruct/detail/FRotator.json |
| LocationType | EAttachLocation :: Type  | - Specifies whether Location is a relative offset or an absolute world position |  |
| LifeSpan | float | - destroy decal component after time runs out (0 = infinite) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UDecalComponent *  |  |  |

### BreakHitResult

Extracts data from a HitResult.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hit | FHitResult &  |  The source HitResult. | cppstruct/detail/FHitResult.json |
| bBlockingHit | bool &  | True if there was a blocking hit, false otherwise. |  |
| bInitialOverlap | bool &  | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |  |
| Time | float &  |  'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |  |
| Distance | float &  | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |  |
| Location | FVector &  | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. | cppstruct/detail/FVector.json |
| ImpactPoint | FVector &  | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. | cppstruct/detail/FVector.json |
| Normal | FVector &  | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. | cppstruct/detail/FVector.json |
| ImpactNormal | FVector &  | Normal of the hit in world space, for the object that was hit by the sweep. | cppstruct/detail/FVector.json |
| PhysMat | UPhysicalMaterial * &  | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |  |
| HitActor | AActor * &  | Actor hit by the trace. |  |
| HitComponent | UPrimitiveComponent * &  | PrimitiveComponent hit by the trace. |  |
| HitBoneName | FName &  | Name of the bone hit (valid only if we hit a skeletal mesh). |  |
| HitItem | int32 &  | Primitive-specific data recording which item in the primitive was hit |  |
| FaceIndex | int32 &  | If colliding with trimesh or landscape, index of face that was hit. |  |
| TraceStart | FVector &  |  | cppstruct/detail/FVector.json |
| TraceEnd | FVector & |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeHitResult

Create a HitResult struct

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bBlockingHit | bool  | True if there was a blocking hit, false otherwise. |  |
| bInitialOverlap | bool  | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |  |
| Time | float  |  'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |  |
| Distance | float  | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |  |
| Location | FVector  | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. | cppstruct/detail/FVector.json |
| ImpactPoint | FVector  | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. | cppstruct/detail/FVector.json |
| Normal | FVector  | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. | cppstruct/detail/FVector.json |
| ImpactNormal | FVector  | Normal of the hit in world space, for the object that was hit by the sweep. | cppstruct/detail/FVector.json |
| PhysMat | UPhysicalMaterial *  | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |  |
| HitActor | AActor *  | Actor hit by the trace. |  |
| HitComponent | UPrimitiveComponent *  | PrimitiveComponent hit by the trace. |  |
| HitBoneName | FName  | Name of the bone hit (valid only if we hit a skeletal mesh). |  |
| HitItem | int32  | Primitive-specific data recording which item in the primitive was hit |  |
| FaceIndex | int32  | If colliding with trimesh or landscape, index of face that was hit. |  |
| TraceStart | FVector  |  | cppstruct/detail/FVector.json |
| TraceEnd | FVector |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FHitResult  |  | cppstruct/detail/FHitResult.json |

### GetSurfaceType

Returns the EPhysicalSurface type of the given Hit.
	  To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hit | FHitResult & |  | cppstruct/detail/FHitResult.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPhysicalSurface  |  |  |

### FindCollisionUV

Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hit | FHitResult &  |  | cppstruct/detail/FHitResult.json |
| UVChannel | int32  |  |  |
| UV | FVector2D & |  | cppstruct/detail/FVector2D.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CreateSaveGameObject

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SaveGameClass | TSubclassOf < USaveGame > | Class of SaveGame to create |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  | 				New SaveGame object to write data to |  |

### CreateSaveGameObjectFromBlueprint

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SaveGameBlueprint | UBlueprint * | Blueprint of SaveGame to create |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  | 					New SaveGame object to write data to |  |

### SaveGameToSlot

Save the contents of the SaveGameObject to a slot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SaveGameObject | USaveGame *  | Object that contains data about the save game that we want to write out |  |
| SlotName | FString &  |  Name of save game slot to save to. |  |
| UserIndex | int32 | For some platforms, master user index to identify the user doing the saving. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 				Whether we successfully saved this information |  |

### DoesSaveGameExist

See if a save game exists with the specified name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FString &  |  Name of save game slot. |  |
| UserIndex | int32 | For some platforms, master user index to identify the user doing the saving. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BindLoadGameGuardEntranceCheckDelegate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Obj | UObject *  |  |  |
| FuncName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindLoadGameGuardExitCheckDelegate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Obj | UObject *  |  |  |
| FuncName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### LoadGameFromSlot

Load the contents from a given slot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FString &  |  Name of the save game slot to load from. |  |
| UserIndex | int32 | For some platforms, master user index to identify the user doing the loading. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  | SaveGameObject	Object containing loaded game state (NULL if load fails) |  |

### LoadGameFromSlotWithSizeLimit

Load the contents from a given slot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FString &  |  Name of the save game slot to load from. |  |
| UserIndex | int32  | For some platforms, master user index to identify the user doing the loading. |  |
| MaxSerSize | int32 | Specify the maxserializesize of archive, just working for fstring. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  | SaveGameObject	Object containing loaded game state (NULL if load fails) |  |

### LoadGameFromMemory

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectBytes | TArray < uint8 > &  |  |  |
| MaxSerSize | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  |  |  |

### LoadGameFromMemoryWithSizeLimit

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectBytes | TArray < uint8 > &  |  |  |
| MaxSerSize | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USaveGame *  |  |  |

### DeleteGameInSlot

Delete a save game in a particular slot.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FString &  |  Name of save game slot to delete. |  |
| UserIndex | int32 | For some platforms, master user index to identify the user doing the deletion. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if a file was actually able to be deleted. use DoesSaveGameExist to distinguish between delete failures and failure due to file not existing. |  |

### GetWorldDeltaSeconds

获得当前每帧的delta time，单位秒

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 每帧的delta time |  |

### GetTimeSeconds

获得当前游戏开始之后的时间，单位秒，受时间膨胀和游戏暂停影响

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 游戏时间 |  |

### GetUnpausedTimeSeconds

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 游戏时间 |  |

### GetRealTimeSeconds

获得当前游戏开始之后的真实时间，单位秒，不受时间膨胀和游戏暂停影响

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 游戏时间 |  |

### GetAudioTimeSeconds

获得当前游戏开始之后的时间，单位秒，不受时间膨胀影响，但受时间暂停影响

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 游戏时间 |  |

### GetAccurateRealTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Seconds | int32 &  |  |  |
| PartialSeconds | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableLiveStreaming

~ DVRStreaming API 
	
	  Toggle live DVR streaming.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enable | bool |  If true enable streaming, otherwise disable. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlatformName

Returns the string name of the current platform, to perform different behavior based on platform.
	  (Platform names include Windows, Mac, IOS, Android, PS4, XboxOne, HTML5, Linux)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### BlueprintSuggestProjectileVelocity

Calculates an launch velocity for a projectile to hit a specified point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| TossVelocity | FVector &  | (output) Result launch velocity. | cppstruct/detail/FVector.json |
| StartLocation | FVector  | Intended launch location | cppstruct/detail/FVector.json |
| EndLocation | FVector  | Desired landing location | cppstruct/detail/FVector.json |
| LaunchSpeed | float  | Desired launch speed |  |
| OverrideGravityZ | float  | Optional gravity override. 0 means "do not override". |  |
| TraceOption | ESuggestProjVelocityTraceOption :: Type  | Controls whether or not to validate a clear path by tracing along the calculated arc |  |
| CollisionRadius | float  | Radius of the projectile (assumed spherical), used when tracing |  |
| bFavorHighArc | bool  | If true and there are 2 valid solutions, will return the higher arc. If false, will favor the lower arc. |  |
| bDrawDebug | bool | When true, a debug arc is drawn (red for an invalid arc, green for a valid arc) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 				Returns false if there is no valid solution or the valid solutions are blocked.  Returns true otherwise. |  |

### Blueprint_PredictProjectilePath_ByObjectType

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| OutHit | FHitResult &  |   Predicted hit result, if the projectile will hit something | cppstruct/detail/FHitResult.json |
| OutPathPositions | TArray < FVector > &  |  Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |  |
| OutLastTraceDestination | FVector &  | Goal position of the final trace it did. Will not be in the path if there is a hit. | cppstruct/detail/FVector.json |
| StartPos | FVector  |   First start trace location | cppstruct/detail/FVector.json |
| LaunchVelocity | FVector  |  Velocity the "virtual projectile" is launched at | cppstruct/detail/FVector.json |
| bTracePath | bool  |   Trace along the entire path to look for blocking hits |  |
| ProjectileRadius | float  |  Radius of the virtual projectile to sweep against the environment |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  |  ObjectTypes to trace against, if bTracePath is true. |  |
| bTraceComplex | bool  |  Use TraceComplex (trace against triangles not primitives) |  |
| ActorsToIgnore | TArray < AActor * > &  |  Actors to exclude from the traces |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  Debug type (one-frame, duration, persistent) |  |
| DrawDebugTime | float  |  Duration of debug lines (only relevant for DrawDebugType::Duration) |  |
| SimFrequency | float  |  Determines size of each sub-step in the simulation (chopping up MaxSimTime) |  |
| MaxSimTime | float  |   Maximum simulation time for the virtual projectile. |  |
| OverrideGravityZ | float |  Optional override of Gravity (if 0, uses WorldGravityZ) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 						True if hit something along the path if tracing for collision. |  |

### Blueprint_PredictProjectilePath_ByTraceChannel

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something (if tracing with collision).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| OutHit | FHitResult &  |   Predicted hit result, if the projectile will hit something | cppstruct/detail/FHitResult.json |
| OutPathPositions | TArray < FVector > &  |  Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |  |
| OutLastTraceDestination | FVector &  | Goal position of the final trace it did. Will not be in the path if there is a hit. | cppstruct/detail/FVector.json |
| StartPos | FVector  |   First start trace location | cppstruct/detail/FVector.json |
| LaunchVelocity | FVector  |  Velocity the "virtual projectile" is launched at | cppstruct/detail/FVector.json |
| bTracePath | bool  |   Trace along the entire path to look for blocking hits |  |
| ProjectileRadius | float  |  Radius of the virtual projectile to sweep against the environment |  |
| TraceChannel | TEnumAsByte < ECollisionChannel >  |  TraceChannel to trace against, if bTracePath is true. |  |
| bTraceComplex | bool  |  Use TraceComplex (trace against triangles not primitives) |  |
| ActorsToIgnore | TArray < AActor * > &  |  Actors to exclude from the traces |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  Debug type (one-frame, duration, persistent) |  |
| DrawDebugTime | float  |  Duration of debug lines (only relevant for DrawDebugType::Duration) |  |
| SimFrequency | float  |  Determines size of each sub-step in the simulation (chopping up MaxSimTime) |  |
| MaxSimTime | float  |   Maximum simulation time for the virtual projectile. |  |
| OverrideGravityZ | float |  Optional override of Gravity (if 0, uses WorldGravityZ) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 						True if hit something along the path (if tracing with collision). |  |

### Blueprint_PredictProjectilePath_Advanced

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
	 Returns true if it hit something.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PredictParams | FPredictProjectilePathParams &  |  Input params to the trace (start location, velocity, time to simulate, etc). | cppstruct/detail/FPredictProjectilePathParams.json |
| PredictResult | FPredictProjectilePathResult & |  Output result of the trace (Hit result, array of locationvelocitytimes for each trace step, etc). | cppstruct/detail/FPredictProjectilePathResult.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 						True if hit something along the path (if tracing with collision). |  |

### SuggestProjectileVelocity_CustomArc

Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
	 Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
	 Does no tracing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| OutLaunchVelocity | FVector &  |  Returns the launch velocity required to reach the EndPos | cppstruct/detail/FVector.json |
| StartPos | FVector  |   Start position of the simulation | cppstruct/detail/FVector.json |
| EndPos | FVector  |   Desired end location for the simulation | cppstruct/detail/FVector.json |
| OverrideGravityZ | float  |  Optional override of WorldGravityZ |  |
| ArcParam | float |   Change height of arc between 0.0-1.0 where 0.5 is the default medium arc |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetWorldOriginLocation

获取世界原点位置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | world上下文对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntVector  | 世界原点 |  |

### SetWorldOriginLocation

设置世界原点位置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| NewLocation | FIntVector | 世界原点 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWorldOriginLocationByLua

设置世界原点位置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| X | int32  |  |  |
| Y | int32  |  |  |
| Z | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SyncSetNewWorldOrigin

同步设置世界原点位置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| X | int32  |  |  |
| Y | int32  |  |  |
| Z | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RebaseLocalOriginOntoZero

返回基于原点坐标的local坐标

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| WorldLocation | FVector |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | origin based position | cppstruct/detail/FVector.json |

### RebaseZeroOriginOntoLocal

返回local坐标基于原点的坐标

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| WorldLocation | FVector |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | local location | cppstruct/detail/FVector.json |

### GrassOverlappingSphereCount

Counts how many grass foliage instances overlap a given sphere.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| StaticMesh | UStaticMesh *  |  |  |
| CenterPosition | FVector  | The center position of the sphere. | cppstruct/detail/FVector.json |
| Radius | float |  The radius of the sphere. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | Number of foliage instances with their mesh set to Mesh that overlap the sphere. |  |

### DeprojectScreenToWorld

获取给定2D屏幕空间中的坐标投影到3D世界空间中的坐标

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController *  | 玩家的PlayerController |  |
| ScreenPosition | FVector2D &  | 屏幕空间中的坐标 | cppstruct/detail/FVector2D.json |
| WorldPosition | FVector &  | 输出的世界空间坐标 | cppstruct/detail/FVector.json |
| WorldDirection | FVector & | 输出的方向向量，世界空间中，给定点远离相机方向的方向向量 | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 是否转换成功 |  |

### ProjectWorldToScreen

获取给定3D世界空间中的坐标投影到2D屏幕空间中的坐标

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController *  | 玩家的PlayerController |  |
| WorldPosition | FVector &  | 世界空间中的坐标 | cppstruct/detail/FVector.json |
| ScreenPosition | FVector2D &  | 输出的屏幕空间坐标 | cppstruct/detail/FVector2D.json |
| bPlayerViewportRelative | bool | 是否与玩家视口相关 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 是否转换成功 |  |

### MarkNetPropertyDirtyFromName

Mark a particular net property of an UObject as dirty (for networking), thus it will be take into consideration in next replication

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  UObject to be marked dirty |  |
| PropertyName | FName  | Name of the particular net property to be marked dirty |  |
| LifetimeCondition | ELifetimeCondition |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetKeyValue

Break up a key=value pair into its key and value.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pair | FString &  |  The string containing a pair to split apart. |  |
| Key | FString &  |  (out) Key portion of Pair. If no = in string will be the same as Pair. |  |
| Value | FString & |  (out) Value portion of Pair. If no = in string will be empty. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ParseOption

Find an option in the options string and return it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Options | FString  | The string containing the options. |  |
| Key | FString & |  The key to find the value of in Options. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 			The value associated with Key if Key found in Options string. |  |

### HasOption

Returns whether a key exists in an options string.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Options | FString  | The string containing the options. |  |
| InKey | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			Whether Key was found in Options. |  |

### GetIntOption

Find an option in the options string and return it as an integer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Options | FString &  | The string containing the options. |  |
| Key | FString &  |  The key to find the value of in Options. |  |
| DefaultValue | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | 			The value associated with Key as an integer if Key found in Options string, otherwise DefaultValue. |  |

### HasLaunchOption

Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OptionToCheck | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the launch option was specified on the commandline, false otherwise |  |

### GetDeviceQualityLevel

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetDeviceTCQualityGrade

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetDeviceMemoryLevel

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetDeviceMemorySize

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### EnableObjArrayAutoResize

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConsoleIntVariable

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FString &  |  |  |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UpdateComponentToWorld

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorComponent | UActorComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsLongScreen

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsWinReleaseBuild

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### RecordDSLaunchState

record ds launch state, collect for ds shutdown error report, add by czcheng

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| state | int32 | launch state, see details in EDSLaunchState |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RecordDSShutdownErrorInfo

record ds shutdown error info, collect for ds shutdown error report, add by czcheng

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ErrorCode | int32  | shutdown error code, see details in EDSShutdownErrorCode |  |
| ErrMsg | FString & | error message |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

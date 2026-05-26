# ULevelStreaming

- Symbol Type: class
- Symbol Path: Others / ULevelStreaming
- Source JSON Path: class/detail/Others/ULevelStreaming.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULevelStreaming.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

Abstract base class of container object encapsulating data required for streaming and providing 
  interface for when a level should be streamed in and out of memory.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName_DEPRECATED | FName | Deprecated name of the package containing the level to load. Use GetWorldAsset() or GetWorldAssetPackageFName() instead. |  |
| WorldAsset | TSoftObjectPtr < UWorld > | The reference to the world containing the level to load |  |
| PackageNameToLoad | FName | If this isn't Name_None, then we load from this package on disk to the new package named PackageName |  |
| LODPackageNames | TArray < FName > | LOD versions of this level |  |
| LevelTransform | FTransform | Transform applied to actors after loading. |  |
| bShouldBeVisibleInEditor | uint32 | Whether this level should be visible in the Editor |  |
| bLocked | uint32 | Whether this level is locked; that is, its actors are read-only. |  |
| bShouldBeLoaded | uint32 | Whether the level should be loaded |  |
| bShouldBeVisible | uint32 | Whether the level should be visible if it is loaded |  |
| bIsStatic | uint32 | Whether this level only contains static actors that aren't affected by gameplay or replication.<br>	  If true, the engine can make certain optimizations and will add this level to the StaticLevels collection. |  |
| bShouldBlockOnLoad | uint32 | Whether we want to force a blocking load |  |
| LevelLODIndex | int32 | Requested LOD. Non LOD sub-levels have Index = -1 |  |
| bDisableDistanceStreaming | uint32 | Whether this level streaming object should be ignored by world composition distance streaming, <br>	   so streaming state can be controlled by other systems (ex: in blueprints) |  |
| bDrawOnLevelStatusMap | uint32 | If true, will be drawn on the 'level streaming status' map (STAT LEVELMAP console command) |  |
| DrawColor_DEPRECATED | FColor | Deprecated level color used for visualization. |  |
| LevelColor | FLinearColor | The level color used for visualization. (Show -> Advanced -> Level Coloration) |  |
| EditorStreamingVolumes | TArray < ALevelStreamingVolume * > | The level streaming volumes bound to this level. |  |
| MinTimeBetweenVolumeUnloadRequests | float | Cooldown time in seconds between volume-based unload requests.  Used in preventing spurious unload requests. |  |
| Keywords | TArray < FString > | List of keywords to filter on in the level browser |  |
| LoadedLevel | ULevel * | Pointer to Level object if currently loaded streamed in. |  |
| PendingUnloadLevel | ULevel * | Pointer to a Level object that was previously active and was replaced with a new LoadedLevel (for LOD switching) |  |
| UnloadingLevels | TArray < ULevel * > | Array to save unloading levels. |  |
| LevelStreamingInfo | FLevelLoadConditionInfo |  |  |
| FolderPath | FName | The folder path for this level within the world browser. This is only available in editor builds. <br>		A NONE path indicates that it exists at the root. It is '' separated. |  |

## Functions

### GetWorldAssetPackageFName

Gets the package name for the world asset referred to by this level streaming as an FName

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API FName |  |  |

### GetLoadedLevel

Gets a pointer to the LoadedLevel value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API class ULevel * |  |  |

### IsLevelVisible

Returns whether streaming level is visible

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### IsLevelLoaded

Returns whether streaming level is loaded

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### IsStreamingStatePending

Returns whether level has streaming state change pending

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### CreateInstance

Creates a new instance of this streaming level with a provided unique instance name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UniqueInstanceName | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULevelStreaming *  |  |  |

### GetLevelScriptActor

Returns the Level Script Actor of the level if the level is loaded and valid

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API ALevelScriptActor * |  |  |

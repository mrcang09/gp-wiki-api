# ULevelStreamingKismet

- Symbol Type: class
- Symbol Path: Others / ULevelStreamingKismet
- Source JSON Path: class/detail/Others/ULevelStreamingKismet.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULevelStreamingKismet.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInitiallyLoaded | uint32 | Whether the level should be loaded at startup |  |
| bInitiallyVisible | uint32 | Whether the level should be visible at startup if it is loaded |  |

## Functions

### LoadLevelInstance

Stream in a level with a specific location and rotation. You can create multiple instances of the same level!
 	
 	 The level to be loaded does not have to be in the persistent map's Levels list, however to ensure that the .umap does get
 	 packaged, please be sure to include the .umap in your Packaging Settings:
 	
 	   Project Settings -> Packaging -> List of Maps to Include in a Packaged Build (you may have to show advanced or type in filter)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LevelName | FString &  | - Level package name, ex: GameMapsMyMapName, specifying short name like MyMapName will force very slow search on disk |  |
| Location | FVector &  | - World space location where the level should be spawned |  |
| Rotation | FRotator &  | - World space rotation for rotating the entire level |  |
| bOutSuccess | bool & | - Whether operation was successful (map was found and added to the sub-levels list) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API ULevelStreamingKismet *  | Streaming level object for a level instance |  |

### CreateLevelInstanceWithLevelName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LevelName | FString &  |  |  |
| UniqueName | FString &  |  |  |
| Trans | FTransform &  |  |  |
| bOutSuccess | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API ULevelStreamingKismet *  |  |  |

### CreateLevelInstanceWithLevel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OriStreamingLevel | ULevelStreaming *  |  |  |
| UniqueName | FString &  |  |  |
| Trans | FTransform &  |  |  |
| bOutSuccess | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API ULevelStreamingKismet *  |  |  |

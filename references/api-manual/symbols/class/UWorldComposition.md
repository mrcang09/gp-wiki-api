# UWorldComposition

- Symbol Type: class
- Symbol Path: Others / UWorldComposition
- Source JSON Path: class/detail/Others/UWorldComposition.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWorldComposition.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

WorldComposition represents world structure:
 	- Holds list of all level packages participating in this world and theirs base parameters (bounding boxes, offset from origin)
 	- Holds list of streaming level objects to stream in and out based on distance from current view point
   - Handles properly levels repositioning during level loading and saving

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Package2WorldTileExtraInfo | TMap < FName , FWorldTileExtraInfo > |  |  |
| LODStealConfigs | TArray < FLODStealConfig > |  |  |
| TilesStreaming | TArray < ULevelStreaming * > |  |  |
| TilesStreamingTimeThreshold | double |  |  |
| bLoadAllTilesDuringCinematic | bool |  |  |
| bRebaseOriginIn3DSpace | bool |  |  |
| RebaseOriginDistance | float |  |  |
| TileBoundsVerifyScale | float |  |  |
| bFlushPool | bool |  |  |
| ServerExcludedLevels | TArray < FString > |  |  |
| ClientExcludedLevels | TArray < FString > |  |  |
| UGCPIEMapBlackList | TArray < FString > |  |  |
| UGCWhiteListSubLevelPaths | TArray < FString > |  |  |
| DeviceExcludedLevels | TArray < FString > |  |  |
| DynamicSubLevelPaths | TArray < FString > |  |  |
| BlackLevelPaths | TArray < FString > |  |  |
| SpecifiedBuildingLevels | TArray < FString > |  |  |
| ClientLoadRadiusFactor | float |  |  |

## Functions

### CheckBisNeedSavedLevelToFileInServer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

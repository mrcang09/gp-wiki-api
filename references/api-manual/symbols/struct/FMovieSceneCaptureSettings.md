# FMovieSceneCaptureSettings

- Symbol Type: struct
- Symbol Path: FMovieSceneCaptureSettings
- Source JSON Path: cppstruct/detail/FMovieSceneCaptureSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneCaptureSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Common movie-scene capture settings

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutputDirectory | FDirectoryPath | The directory to output the captured file(s) in |  |
| GameModeOverride | TSubclassOf < AGameModeBase > | Optional game mode to override the map's default game mode with.  This can be useful if the game's normal mode displays UI elements or loading screens that you don't want captured. |  |
| OutputFormat | FString |  |  |
| bOverwriteExisting | bool | Whether to overwrite existing files or not |  |
| bUseRelativeFrameNumbers | bool | True if frame numbers in the output files should be relative to zero, rather than the actual frame numbers in the originating animation content |  |
| HandleFrames | int32 | Number of frame handles to include for each shot |  |
| ZeroPadFrameNumbers | uint8 | How much to zero-pad frame numbers on filenames |  |
| FrameRate | int32 | The frame rate at which to capture |  |
| BitRate | int32 | The bit rate at which to capture |  |
| MovieLiveUrl | FString |  |  |
| bFixedTimeStep | bool |  |  |
| Resolution | FCaptureResolution | The resolution at which to capture |  |
| bEnableTextureStreaming | bool | Whether to texture streaming should be enabled while capturing.  Turning off texture streaming may cause much more memory to be used, but also reduces the chance of blurry textures in your captured video. |  |
| bCinematicEngineScalability | bool | Whether to enable cinematic engine scalability settings |  |
| bCinematicMode | bool | Whether to enable cinematic mode whilst capturing |  |
| bAllowMovement | bool | Whether to allow player movement whilst capturing |  |
| bAllowTurning | bool | Whether to allow player rotation whilst capturing |  |
| bShowPlayer | bool | Whether to show the local player whilst capturing |  |
| bShowHUD | bool | Whether to show the in-game HUD whilst capturing |  |

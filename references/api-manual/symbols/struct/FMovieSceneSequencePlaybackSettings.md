# FMovieSceneSequencePlaybackSettings

- Symbol Type: struct
- Symbol Path: FMovieSceneSequencePlaybackSettings
- Source JSON Path: cppstruct/detail/FMovieSceneSequencePlaybackSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequencePlaybackSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Settings for the level sequence player actor.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LoopCount | int32 | Number of times to loop playback. -1 for infinite, else the number of times to loop before stopping |  |
| PlayRate | float | The rate at which to playback the animation |  |
| bRandomStartTime | bool | Start playback at a random time |  |
| StartTime | float | Start playback at the specified time |  |
| bRestoreState | bool | Flag used to specify whether actor states should be restored on stop |  |
| bDisableMovementInput | bool | Disable Input from player during play |  |
| bDisableLookAtInput | bool | Disable LookAt Input from player during play |  |
| bHidePlayer | bool | Hide Player Pawn during play |  |
| bHideHud | bool | Hide HUD during play |  |
| bEnableHDR | bool | EnableHDR When Play Sequence |  |
| BindingOverrides | TScriptInterface < IMovieSceneBindingOverridesInterface > | Interface that defines overridden bindings for this sequence |  |

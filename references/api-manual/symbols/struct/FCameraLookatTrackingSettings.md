# FCameraLookatTrackingSettings

- Symbol Type: struct
- Symbol Path: FCameraLookatTrackingSettings
- Source JSON Path: cppstruct/detail/FCameraLookatTrackingSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCameraLookatTrackingSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Settings to control the camera's lookat feature

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableLookAtTracking | uint8 | True to enable lookat tracking, false otherwise. <br>	UPROPERTY(Interp, EditAnywhere, BlueprintReadWrite, Category = "LookAt") |  |
| bDrawDebugLookAtTrackingPosition | uint8 | True to draw a debug representation of the lookat location |  |
| LookAtTrackingInterpSpeed | float | Controls degree of smoothing. 0.f for no smoothing, higher numbers for fastertighter tracking. |  |
| ActorToTrack | AActor * | If set, camera will track this actor's location |  |
| RelativeOffset | FVector | Offset from actor position to look at. Relative to actor if tracking an actor, relative to world otherwise. |  |
| bAllowRoll | uint8 | True to allow user-defined roll, false otherwise. |  |

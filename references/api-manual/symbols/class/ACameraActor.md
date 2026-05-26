# ACameraActor

- Symbol Type: class
- Symbol Path: Others / ACameraActor
- Source JSON Path: class/detail/Others/ACameraActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ACameraActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

A CameraActor is a camera viewpoint that can be placed in a level.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AutoActivateForPlayer | TEnumAsByte < EAutoReceiveInput :: Type > | Specifies which player controller, if any, should automatically use this Camera when the controller is active. |  |
| CameraComponent | UCameraComponent * | The camera component for this camera |  |
| SceneComponent | USceneComponent * |  |  |
| bConstrainAspectRatio_DEPRECATED | uint32 |  |  |
| AspectRatio_DEPRECATED | float |  |  |
| FOVAngle_DEPRECATED | float |  |  |
| PostProcessBlendWeight_DEPRECATED | float |  |  |
| PostProcessSettings_DEPRECATED | FPostProcessSettings |  |  |

## Functions

### GetAutoActivatePlayerIndex

Returns index of the player for whom we auto-activate, or INDEX_NONE (-1) if disabled.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

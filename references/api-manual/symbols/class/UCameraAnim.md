# UCameraAnim

- Symbol Type: class
- Symbol Path: Others / UCameraAnim
- Source JSON Path: class/detail/Others/UCameraAnim.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCameraAnim.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A predefined animation to be played on a camera

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CameraInterpGroup | UInterpGroup * | The UInterpGroup that holds our actual interpolation data. |  |
| AnimLength | float | Length, in seconds. |  |
| BoundingBox | FBox | AABB in local space. |  |
| bRelativeToInitialTransform | uint8 | If true, assume all transform keys are intended be offsets from the start of the animation. This allows the animation to be authored at any world location and be applied as a delta to the camera. <br>	  If false, assume all transform keys are authored relative to the world origin. Positions will be directly applied as deltas to the camera. |  |
| bRelativeToInitialFOV | uint8 | If true, assume all FOV keys are intended be offsets from the start of the animation.<br>	 If false, assume all FOV keys are authored relative to the current FOV of the camera at the start of the animation. |  |
| BaseFOV | float | The base FOV that all FOV keys are relative to. |  |
| BasePostProcessSettings | FPostProcessSettings | Default PP settings to put on the animated camera. For modifying PP without keyframes. |  |
| BasePostProcessBlendWeight | float | Default PP blend weight to put on the animated camera. For modifying PP without keyframes. |  |
| PreviewInterpGroup | UInterpGroup * | This is to preview and they only exists in editor |  |

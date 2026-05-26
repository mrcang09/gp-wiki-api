# UCameraModifier_CameraShake

- Symbol Type: class
- Symbol Path: Others / UCameraModifier_CameraShake
- Source JSON Path: class/detail/Others/UCameraModifier_CameraShake.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCameraModifier_CameraShake.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A UCameraModifier_CameraShake is a camera modifier that can apply a UCameraShake to 
  the owning camera.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActiveShakes | TArray < UCameraShake * > | List of active CameraShake instances |  |
| SplitScreenShakeScale | float | Scaling factor applied to all camera shakes in when in splitscreen mode. Normally used to reduce shaking, since shakes feel more intense in a smaller viewport. |  |
| CacheShakeInsMap | TMap < TSubclassOf < UCameraShake > , FCacheCameraShakeData > |  |  |

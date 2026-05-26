# UReflectionCaptureComponent

- Symbol Type: class
- Symbol Path: Others / UReflectionCaptureComponent
- Source JSON Path: class/detail/Others/UReflectionCaptureComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UReflectionCaptureComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CaptureOffsetComponent | UBillboardComponent * |  |  |
| ReflectionSourceType | EReflectionSourceType | Indicates where to get the reflection source from. |  |
| IndoorOutdoorMask | TEnumAsByte < EIndoorOutdoorMask > |  |  |
| Cubemap | UTextureCube * | Cubemap to use for reflection if ReflectionSourceType is set to RS_SpecifiedCubemap. |  |
| SourceCubemapAngle | float | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |  |
| Brightness | float | A brightness control to scale the captured scene's reflection intensity. |  |
| CaptureOffset | FVector | World space offset to apply before capturing. |  |
| EnabledPlatform | EReflectionPlatform |  |  |
| StateId | FGuid |  |  |

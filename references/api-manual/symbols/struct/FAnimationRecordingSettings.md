# FAnimationRecordingSettings

- Symbol Type: struct
- Symbol Path: FAnimationRecordingSettings
- Source JSON Path: cppstruct/detail/FAnimationRecordingSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationRecordingSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Settings describing how to record an animation

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bRecordInWorldSpace | bool | Whether to record animation in world space, defaults to true |  |
| bRemoveRootAnimation | bool | Whether to remove the root bone transform from the animation |  |
| bAutoSaveAsset | bool | Whether to auto-save asset when recording is completed. Defaults to false |  |
| SampleRate | float | Sample rate of the recorded animation (in Hz) |  |
| Length | float | Maximum length of the animation recorded (in seconds). If zero the animation will keep on recording until stopped. |  |
| InterpMode | TEnumAsByte < ERichCurveInterpMode > | Interpolation mode for the recorded keys. |  |
| TangentMode | TEnumAsByte < ERichCurveTangentMode > | Tangent mode for the recorded keys. |  |

# FReverbSettings

- Symbol Type: struct
- Symbol Path: FReverbSettings
- Source JSON Path: cppstruct/detail/FReverbSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FReverbSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Struct encapsulating settings for reverb effects.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bApplyReverb | uint32 | Whether to apply the reverb settings below. |  |
| ReverbType_DEPRECATED | TEnumAsByte < enum ReverbPreset > | The reverb preset to employ. |  |
| ReverbEffect | UReverbEffect * | The reverb asset to employ. |  |
| Volume | float | Volume level of the reverb affect. |  |
| FadeTime | float | Time to fade from the current reverb settings into this setting, in seconds. |  |

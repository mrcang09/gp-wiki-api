# FPassiveSoundMixModifier

- Symbol Type: struct
- Symbol Path: FPassiveSoundMixModifier
- Source JSON Path: cppstruct/detail/FPassiveSoundMixModifier.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FPassiveSoundMixModifier.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Structure containing information on a SoundMix to activate passively.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoundMix | USoundMix * | The SoundMix to activate |  |
| MinVolumeThreshold | float | Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active. |  |
| MaxVolumeThreshold | float | Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active. |  |

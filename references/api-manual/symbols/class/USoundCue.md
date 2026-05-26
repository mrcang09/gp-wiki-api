# USoundCue

- Symbol Type: class
- Symbol Path: Others / USoundCue
- Source JSON Path: class/detail/Others/USoundCue.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USoundCue.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

The behavior of audio playback is defined within Sound Cues.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverrideAttenuation | uint32 | Indicates whether attenuation should use the Attenuation Overrides or the Attenuation Settings asset |  |
| FirstNode | USoundNode * |  |  |
| VolumeMultiplier | float | Volume multiplier for the Sound Cue |  |
| PitchMultiplier | float | Pitch multiplier for the Sound Cue |  |
| AttenuationOverrides | FSoundAttenuationSettings | Attenuation settings to use if Override Attenuation is set to true |  |
| SubtitlePriority | float |  |  |
| AllNodes | TArray < USoundNode * > |  |  |
| SoundCueGraph | UEdGraph * |  |  |

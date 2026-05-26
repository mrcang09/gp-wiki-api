# UMovieSceneAudioSection

- Symbol Type: class
- Symbol Path: Others / UMovieSceneAudioSection
- Source JSON Path: class/detail/Others/UMovieSceneAudioSection.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneAudioSection.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Audio section, for use in the master audio, or by attached audio objects

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sound | USoundBase * | The sound cue or wave that this section plays |  |
| StartOffset | float | The offset into the beginning of the audio clip |  |
| AudioStartTime_DEPRECATED | float | The absolute time that the sound starts playing at |  |
| AudioDilationFactor_DEPRECATED | float | The amount which this audio is time dilated by |  |
| AudioVolume_DEPRECATED | float | The volume the sound will be played with. |  |
| SoundVolume | FRichCurve | The volume the sound will be played with. |  |
| PitchMultiplier | FRichCurve | The pitch multiplier the sound will be played with. |  |
| bSuppressSubtitles | bool |  |  |
| bOverrideAttenuation | bool | Should the attenuation settings on this section be used. |  |
| AttenuationSettings | USoundAttenuation * | The attenuation settings to use. |  |
| OnQueueSubtitles | FOnQueueSubtitles | Called when subtitles are sent to the SubtitleManager.  Set this delegate if you want to hijack the subtitles for other purposes |  |
| OnAudioFinished | FOnAudioFinished | called when we finish playing audio, either because it played to completion or because a Stop() call turned it off early |  |
| OnAudioPlaybackPercent | FOnAudioPlaybackPercent |  |  |

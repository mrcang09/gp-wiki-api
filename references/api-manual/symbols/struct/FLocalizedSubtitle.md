# FLocalizedSubtitle

- Symbol Type: struct
- Symbol Path: FLocalizedSubtitle
- Source JSON Path: cppstruct/detail/FLocalizedSubtitle.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLocalizedSubtitle.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

A subtitle localized to a specific language.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LanguageExt | FString | The 3-letter language for this subtitle |  |
| Subtitles | TArray < FSubtitleCue > | Subtitle cues.  If empty, use SoundNodeWave's SpokenText as the subtitle.  Will often be empty,<br>	  as the contents of the subtitle is commonly identical to what is spoken. |  |
| bMature | uint32 | true if this sound is considered to contain mature content. |  |
| bManualWordWrap | uint32 | true if the subtitles have been split manually. |  |
| bSingleLine | uint32 | true if the subtitles should be displayed one line at a time. |  |

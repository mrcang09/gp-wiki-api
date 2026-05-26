# FSlateSound

- Symbol Type: struct
- Symbol Path: FSlateSound
- Source JSON Path: cppstruct/detail/FSlateSound.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSlateSound.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Description

An intermediary to make UBaseSound available for Slate to play sounds

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ResourceObject | UObject * | Pointer to the USoundBase. Holding onto it as a UObject because USoundBase is not available in Slate core.<br>	  Edited via FSlateSoundStructCustomization to ensure you can only set USoundBase assets on it. |  |

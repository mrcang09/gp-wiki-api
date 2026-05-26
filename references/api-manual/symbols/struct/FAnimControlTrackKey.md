# FAnimControlTrackKey

- Symbol Type: struct
- Symbol Path: FAnimControlTrackKey
- Source JSON Path: cppstruct/detail/FAnimControlTrackKey.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimControlTrackKey.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Description

Structure used for holding information for one animation played on the Anim Control track.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartTime | float | Position in the Matinee sequence to start playing this animation. |  |
| AnimSeq | UAnimSequence * | Animation Sequence to play |  |
| AnimStartOffset | float | Time to start playing AnimSequence at. |  |
| AnimEndOffset | float | Time to end playing the AnimSequence at. |  |
| AnimPlayRate | float | Playback speed of this animation. |  |
| bLooping | uint32 | Should this animation loop. |  |
| bReverse | uint32 | Whether to play the animation in reverse or not. |  |

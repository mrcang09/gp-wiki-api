# FAnimSegment

- Symbol Type: struct
- Symbol Path: FAnimSegment
- Source JSON Path: cppstruct/detail/FAnimSegment.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSegment.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

this is anim segment that defines what animation and how

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimReference | UAnimSequenceBase * | Anim Reference to play - only allow AnimSequence or AnimComposite |  |
| StartPos | float | Start Pos within this AnimCompositeBase |  |
| AnimStartTime | float | Time to start playing AnimSequence at. |  |
| AnimEndTime | float | Time to end playing the AnimSequence at. |  |
| AnimPlayRate | float | Playback speed of this animation. If you'd like to reverse, set -1 |  |
| LoopingCount | int32 |  |  |

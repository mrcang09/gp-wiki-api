# FRawAnimSequenceTrack

- Symbol Type: struct
- Symbol Path: FRawAnimSequenceTrack
- Source JSON Path: cppstruct/detail/FRawAnimSequenceTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRawAnimSequenceTrack.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Raw keyframe data for one track.  Each array will contain either NumFrames elements or 1 element.
  One element is used as a simple compression scheme where if all keys are the same, they'll be
  reduced to 1 key that is constant over the entire sequence.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PosKeys | TArray < FVector > | Position keys. |  |
| RotKeys | TArray < FQuat > | Rotation keys. |  |
| ScaleKeys | TArray < FVector > | Scale keys. |  |

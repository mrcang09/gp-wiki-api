# FRootMotionExtractionStep

- Symbol Type: struct
- Symbol Path: FRootMotionExtractionStep
- Source JSON Path: cppstruct/detail/FRootMotionExtractionStep.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRootMotionExtractionStep.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Struct defining a RootMotionExtractionStep.
  When extracting RootMotion we can encounter looping animations (wrap around), or different animations.
  We break those up into different steps, to help with RootMotion extraction, 
  as we can only extract a contiguous range per AnimSequence.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimSequence | UAnimSequence * | AnimSequence ref |  |
| StartPosition | float | Start position to extract root motion from. |  |
| EndPosition | float | End position to extract root motion to. |  |

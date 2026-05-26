# UDefaultLevelSequenceInstanceData

- Symbol Type: class
- Symbol Path: Others / UDefaultLevelSequenceInstanceData
- Source JSON Path: class/detail/Others/UDefaultLevelSequenceInstanceData.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDefaultLevelSequenceInstanceData.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

Default instance data class that level sequences understand. Implements IMovieSceneTransformOrigin.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TransformOriginActor | AActor * | When set, this actor's world position will be used as the transform origin for all absolute transform sections |  |
| TransformOrigin | FTransform | Specifies a transform that offsets all absolute transform sections in this sequence. Will compound with attach tracks. Scale is ignored. Not applied to Relative or Additive sections. |  |
| ShouldIgnoreScale | bool |  |  |

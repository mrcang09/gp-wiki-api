# FMovieSceneSequenceTransform

- Symbol Type: struct
- Symbol Path: FMovieSceneSequenceTransform
- Source JSON Path: cppstruct/detail/FMovieSceneSequenceTransform.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceTransform.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Movie scene sequence transform class that transforms from one time-space to another.
 
  @note The transform can be thought of as the top row of a 2x2 matrix, where the bottom row is the identity:
  			| TimeScale	Offset	|
 			| 0			1		|
 
  As such, traditional matrix mathematics can be applied to transform between different sequence's time-spaces.
  Transforms apply offset first, then time scale.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TimeScale | float | The sequence's time scale (or play rate) |  |
| Offset | float | Scalar time offset applied before the scale |  |

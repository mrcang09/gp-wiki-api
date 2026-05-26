# FMovieSceneEvaluationGroupLUTIndex

- Symbol Type: struct
- Symbol Path: FMovieSceneEvaluationGroupLUTIndex
- Source JSON Path: cppstruct/detail/FMovieSceneEvaluationGroupLUTIndex.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroupLUTIndex.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Lookup table index for a group of evaluation templates

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LUTOffset | int32 | The offset within FMovieSceneEvaluationGroup::SegmentPtrLUT that this index starts |  |
| NumInitPtrs | int32 | The number of initialization pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset. |  |
| NumEvalPtrs | int32 | The number of evaluation pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset + NumInitPtrs. |  |

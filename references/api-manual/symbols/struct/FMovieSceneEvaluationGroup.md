# FMovieSceneEvaluationGroup

- Symbol Type: struct
- Symbol Path: FMovieSceneEvaluationGroup
- Source JSON Path: cppstruct/detail/FMovieSceneEvaluationGroup.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroup.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Holds segment pointers for all segments that are active for a given range of the sequence

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LUTIndices | TArray < FMovieSceneEvaluationGroupLUTIndex > | Array of indices that define all the flush groups in the range. |  |
| SegmentPtrLUT | TArray < FMovieSceneEvaluationFieldSegmentPtr > | A grouping of evaluation pointers that occur in this range of the sequence |  |

# FMovieSceneEvaluationField

- Symbol Type: struct
- Symbol Path: FMovieSceneEvaluationField
- Source JSON Path: cppstruct/detail/FMovieSceneEvaluationField.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationField.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Memory layout optimized primarily for speed of searching the applicable ranges

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Ranges | TArray < FFloatRange > | Ranges stored separately for fast (cache efficient) lookup. Each index has a corresponding entry in FMovieSceneEvaluationField::Groups. |  |
| Groups | TArray < FMovieSceneEvaluationGroup > | Groups that store segment pointers for each of the above ranges. Each index has a corresponding entry in FMovieSceneEvaluationField::Ranges. |  |
| MetaData | TArray < FMovieSceneEvaluationMetaData > | Meta data that maps to entries in the 'Ranges' array. |  |

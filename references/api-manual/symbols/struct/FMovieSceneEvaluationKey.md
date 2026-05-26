# FMovieSceneEvaluationKey

- Symbol Type: struct
- Symbol Path: FMovieSceneEvaluationKey
- Source JSON Path: cppstruct/detail/FMovieSceneEvaluationKey.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationKey.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Keyable struct that represents a particular entity within an evaluation template (either a sectiontemplate or a track)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SequenceID | FMovieSceneSequenceID | ID of the sequence that the entity is contained within |  |
| TrackIdentifier | FMovieSceneTrackIdentifier | ID of the track this key relates to |  |
| SectionIdentifier | uint32 | ID of the section this key relates to (or -1 where this key relates to a track) |  |

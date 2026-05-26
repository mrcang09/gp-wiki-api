# FMovieSceneEvaluationTrack

- Symbol Type: struct
- Symbol Path: FMovieSceneEvaluationTrack
- Source JSON Path: cppstruct/detail/FMovieSceneEvaluationTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationTrack.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Evaluation track that is stored within an evaluation template for a sequence.
  Contains user-defined evaluation templates, and an optional track implementation

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectBindingID | FGuid | ID of the possessable or spawnable within the UMovieScene this track belongs to, if any. Zero guid where this relates to a master track. |  |
| EvaluationPriority | uint16 | Evaluation priority. Highest is evaluated first |  |
| EvaluationMethod | EEvaluationMethod | Evaluation method - static or swept |  |
| EvaluationRunSide | int32 |  |  |
| MinRunnableTCQuality | int32 |  |  |
| RunTagArray | TArray < FString > |  |  |
| Segments | TArray < FMovieSceneSegment > | Array of segmented ranges contained within the track. |  |
| ChildTemplates | TArray < FMovieSceneEvalTemplatePtr > | Domain-specific evaluation templates (normally 1 per section) |  |
| TrackTemplate | FMovieSceneTrackImplementationPtr | Domain-specific track implementation override. |  |
| EvaluationGroup | FName | Flush group that determines whether this track belongs to a group of tracks |  |
| bEvaluateInPreroll | uint32 | Whether this track is evaluated in preroll |  |
| bEvaluateInPostroll | uint32 | Whether this track is evaluated in postroll |  |

# UMovieSceneSequence

- Symbol Type: class
- Symbol Path: Others / UMovieSceneSequence
- Source JSON Path: class/detail/Others/UMovieSceneSequence.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequence.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Abstract base class for movie scene animations (C++ version).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EvaluationTemplate | FCachedMovieSceneEvaluationTemplate |  |  |
| TemplateParameters | FMovieSceneTrackCompilationParams |  |  |
| InstancedSubSequenceEvaluationTemplates | TMap < UObject * , FCachedMovieSceneEvaluationTemplate > |  |  |
| bParentContextsAreSignificant | bool | true if the result of GetParentObject is significant in object resolution for LocateBoundObjects.<br>	  When true, if GetParentObject returns nullptr, the PlaybackContext will be used for LocateBoundObjects, other wise the object's parent will be used<br>	  When false, the PlaybackContext will always be used for LocateBoundObjects |  |

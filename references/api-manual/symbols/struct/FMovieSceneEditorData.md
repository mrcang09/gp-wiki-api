# FMovieSceneEditorData

- Symbol Type: struct
- Symbol Path: FMovieSceneEditorData
- Source JSON Path: cppstruct/detail/FMovieSceneEditorData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEditorData.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Editor only data that needs to be saved between sessions for editing but has no runtime purpose

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ExpansionStates | TMap < FString , FMovieSceneExpansionState > | Map of node path -> expansion state. |  |
| WorkingRange | FFloatRange | User-defined working range in which the entire sequence should reside. |  |
| ViewRange | FFloatRange | The last view-range that the user was observing |  |

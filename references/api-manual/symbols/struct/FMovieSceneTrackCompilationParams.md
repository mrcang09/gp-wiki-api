# FMovieSceneTrackCompilationParams

- Symbol Type: struct
- Symbol Path: FMovieSceneTrackCompilationParams
- Source JSON Path: cppstruct/detail/FMovieSceneTrackCompilationParams.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackCompilationParams.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Movie scene compilation parameters. Serialized items contribute to a compiled template's cached hash

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bForEditorPreview | bool | Whether we're generating for an editor preview, or for efficient runtime evaluation |  |
| bDuringBlueprintCompile | bool | Whether we're generating during a blueprint compile. As such, UObject types may not have been fully loaded. |  |

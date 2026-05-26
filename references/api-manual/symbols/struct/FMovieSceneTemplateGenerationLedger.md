# FMovieSceneTemplateGenerationLedger

- Symbol Type: struct
- Symbol Path: FMovieSceneTemplateGenerationLedger
- Source JSON Path: cppstruct/detail/FMovieSceneTemplateGenerationLedger.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTemplateGenerationLedger.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LastTrackIdentifier | FMovieSceneTrackIdentifier |  |  |
| TrackReferenceCounts | TMap < FMovieSceneTrackIdentifier , int32 > | Map of track identifiers to number of references within th template (generally 1, maybe >1 for shared tracks) |  |
| TrackSignatureToTrackIdentifier | TMap < FGuid , FMovieSceneTrackIdentifiers > | Map of track signature to array of track identifiers that it created |  |

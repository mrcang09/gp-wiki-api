# FMovieSceneTrackEvalOptions

- Symbol Type: struct
- Symbol Path: FMovieSceneTrackEvalOptions
- Source JSON Path: cppstruct/detail/FMovieSceneTrackEvalOptions.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackEvalOptions.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Generic evaluation options for any track

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bCanEvaluateNearestSection | uint32 | true when the value of bEvalNearestSection is to be considered for the track |  |
| bEvalNearestSection | uint32 | When evaluating empty space on a track, will evaluate the last position of the previous section (if possible), or the first position of the next section, in that order of preference. |  |
| bEvaluateInPreroll | uint32 | Evaluate this track as part of its parent sub-section's pre-roll, if applicable |  |
| bEvaluateInPostroll | uint32 | Evaluate this track as part of its parent sub-section's post-roll, if applicable |  |
| bEvaluateNearestSection_DEPRECATED | uint32 |  |  |

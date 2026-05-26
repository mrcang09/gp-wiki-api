# UMovieSceneSection

- Symbol Type: class
- Symbol Path: Others / UMovieSceneSection
- Source JSON Path: class/detail/Others/UMovieSceneSection.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSection.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Base class for movie scene sections

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EvalOptions | FMovieSceneSectionEvalOptions |  |  |
| Easing | FMovieSceneEasingSettings |  |  |
| StartTime | float | The start time of the section |  |
| EndTime | float | The end time of the section |  |
| RowIndex | int32 | The row index that this section sits on |  |
| OverlapPriority | int32 | This section's priority over overlapping sections |  |
| bIsActive | uint32 | Toggle whether this section is activeinactive |  |
| bIsInfinite | uint32 | Toggle to set this section to be infinite |  |
| PreRollTime | float | The amount of time to prepare this section for evaluation before it actually starts. |  |
| PostRollTime | float | The amount of time to continue 'postrolling' this section for after evaluation has ended. |  |
| bIsLocked | uint32 | Toggle whether this section is lockedunlocked |  |
| BlendType | FOptionalMovieSceneBlendType |  |  |

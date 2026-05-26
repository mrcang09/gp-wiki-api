# FMovieScenePossessable

- Symbol Type: struct
- Symbol Path: FMovieScenePossessable
- Source JSON Path: cppstruct/detail/FMovieScenePossessable.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieScenePossessable.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

MovieScenePossessable is a "typed slot" used to allow the MovieScene to control an already-existing object

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Guid | FGuid | Unique identifier of the possessable object. |  |
| Name | FString | Name label for this slot |  |
| PossessedObjectClass | UClass * | Type of the object we'll be possessing |  |
| ParentGuid | FGuid | GUID relating to this possessable's parent, if applicable. |  |

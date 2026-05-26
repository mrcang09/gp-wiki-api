# FMovieSceneSpawnable

- Symbol Type: struct
- Symbol Path: FMovieSceneSpawnable
- Source JSON Path: cppstruct/detail/FMovieSceneSpawnable.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSpawnable.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

MovieSceneSpawnable describes an object that can be spawned for this MovieScene

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Guid | FGuid | Unique identifier of the spawnable object. |  |
| Name | FString | Name label |  |
| ObjectTemplate | UObject * |  |  |
| ChildPossessables | TArray < FGuid > | Set of GUIDs to possessable object bindings that are bound to an object inside this spawnable |  |
| Ownership | ESpawnOwnership | Property indicating where ownership responsibility for this object lies |  |
| GeneratedClass_DEPRECATED | UClass * | Deprecated generated class |  |

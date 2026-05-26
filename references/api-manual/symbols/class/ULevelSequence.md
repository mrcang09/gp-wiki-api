# ULevelSequence

- Symbol Type: class
- Symbol Path: Others / ULevelSequence
- Source JSON Path: class/detail/Others/ULevelSequence.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequence.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

Movie scene animation for Actors.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MovieScene | UMovieScene * | Pointer to the movie scene that controls this animation. |  |
| ObjectReferences | FLevelSequenceObjectReferenceMap | Legacy object references - should be read-only. Not deprecated because they need to still be saved |  |
| BindingReferences | FLevelSequenceBindingReferences | References to bound objects. |  |
| PossessedObjects_DEPRECATED | TMap < FString , FLevelSequenceObject > | Deprecated property housing old possessed object bindings |  |
| DirectorClass | UClass * | The class that is used to spawn this level sequence's director instance.<br>	  Director instances are allocated on-demand one per sequence during evaluation and are used by event tracks for triggering events. |  |
| DirectorBlueprint | UBlueprint * | A pointer to the director blueprint that generates this sequence's DirectorClass. |  |

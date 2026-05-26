# FLevelSequenceObject

- Symbol Type: struct
- Symbol Path: FLevelSequenceObject
- Source JSON Path: cppstruct/detail/FLevelSequenceObject.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceObject.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

Structure for animated Actor objects.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectOrOwner | TLazyObjectPtr < UObject > | The object or the owner of the object being possessed. |  |
| ComponentName | FString | Optional name of an ActorComponent. |  |
| CachedComponent | TWeakObjectPtr < UObject > | Cached pointer to the Actor component (only if ComponentName is set). |  |

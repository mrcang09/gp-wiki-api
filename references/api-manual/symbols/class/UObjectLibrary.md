# UObjectLibrary

- Symbol Type: class
- Symbol Path: Others / UObjectLibrary
- Source JSON Path: class/detail/Others/UObjectLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UObjectLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

Class that holds a library of Objects

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectBaseClass | UClass * | Class that Objects must be of. If ContainsBlueprints is true, this is the native class that the blueprints are instances of and not UClass |  |
| bHasBlueprintClasses | bool | True if this library holds blueprint classes, false if it holds other objects |  |
| Objects | TArray < UObject * > | List of Objects in library |  |
| WeakObjects | TArray < TWeakObjectPtr < UObject > > | Weak pointers to objects |  |
| bUseWeakReferences | bool | If this library should use weak pointers |  |
| bIsFullyLoaded | bool | True if we've already fully loaded this library, can't do it twice |  |

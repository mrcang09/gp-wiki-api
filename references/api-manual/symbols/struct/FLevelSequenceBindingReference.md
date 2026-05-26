# FLevelSequenceBindingReference

- Symbol Type: struct
- Symbol Path: FLevelSequenceBindingReference
- Source JSON Path: cppstruct/detail/FLevelSequenceBindingReference.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceBindingReference.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

An external reference to an level sequence object, resolvable through an arbitrary context.
  
  Bindings consist of an optional package name, and the path to the object within that package.
  Where package name is empty, the reference is a relative path from a specific outer (the context).
  Currently, the package name should only ever be empty for component references, which must remain relative bindings to work correctly with spawnables and reinstanced actors.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName_DEPRECATED | FString | Replaced by ExternalObjectPath |  |
| ExternalObjectPath | FSoftObjectPath | Path to a specific actorcomponent inside an external package |  |
| ObjectPath | FString | Object path relative to a passed in context object, this is used if ExternalObjectPath is invalid |  |

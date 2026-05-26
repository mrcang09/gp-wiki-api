# FFoliageTypeObject

- Symbol Type: struct
- Symbol Path: FFoliageTypeObject
- Source JSON Path: cppstruct/detail/FFoliageTypeObject.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FFoliageTypeObject.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

A wrapper struct used to allow the use of either FoliageType assets or FoliageType blueprint classes

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FoliageTypeObject | UObject * | The foliage type that will be spawned by the procedural foliage simulation |  |
| TypeInstance | UFoliageType * | The actual instance of the foliage type that is used for spawning |  |
| bIsAsset | bool | Whether this contains an asset object (as opposed to a BP class) |  |
| Type_DEPRECATED | TSubclassOf < UFoliageType_InstancedStaticMesh > |  |  |

# FMaterialParameterCollectionInfo

- Symbol Type: struct
- Symbol Path: FMaterialParameterCollectionInfo
- Source JSON Path: cppstruct/detail/FMaterialParameterCollectionInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialParameterCollectionInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

Stores information about a parameter collection that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateId | FGuid | Id that the collection had when this material was last compiled. |  |
| ParameterCollection | UMaterialParameterCollection * | The collection which this material has a dependency on. |  |

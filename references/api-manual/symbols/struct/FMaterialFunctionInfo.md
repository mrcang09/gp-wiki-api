# FMaterialFunctionInfo

- Symbol Type: struct
- Symbol Path: FMaterialFunctionInfo
- Source JSON Path: cppstruct/detail/FMaterialFunctionInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialFunctionInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

Stores information about a function that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateId | FGuid | Id that the function had when this material was last compiled. |  |
| Function | UMaterialFunction * | The function which this material has a dependency on. |  |

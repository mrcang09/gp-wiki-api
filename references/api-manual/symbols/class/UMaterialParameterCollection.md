# UMaterialParameterCollection

- Symbol Type: class
- Symbol Path: Others / UMaterialParameterCollection
- Source JSON Path: class/detail/Others/UMaterialParameterCollection.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialParameterCollection.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Asset class that contains a list of parameter names and their default values. 
  Any number of materials can reference these parameters and get new values when the parameter values are changed.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateId | FGuid | Used by materials using this collection to know when to recompile. |  |
| ScalarParameters | TArray < FCollectionScalarParameter > |  |  |
| VectorParameters | TArray < FCollectionVectorParameter > |  |  |

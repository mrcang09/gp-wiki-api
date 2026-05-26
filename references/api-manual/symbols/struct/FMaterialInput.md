# FMaterialInput

- Symbol Type: struct
- Symbol Path: FMaterialInput
- Source JSON Path: cppstruct/detail/FMaterialInput.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialInput.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutputIndex | int32 | Index into Expression's outputs array that this input is connected to. |  |
| InputName | FString | Optional name of the input.<br>	  Note that this is the only member which is not derived from the output currently connected. |  |
| Mask | int32 |  |  |
| MaskR | int32 |  |  |
| MaskG | int32 |  |  |
| MaskB | int32 |  |  |
| MaskA | int32 |  |  |
| ExpressionName | FName | Material expression name that this input is connected to, or None if not connected. Used only in cooked builds |  |
| Expression | UMaterialExpression * | Material expression that this input is connected to, or NULL if not connected. |  |

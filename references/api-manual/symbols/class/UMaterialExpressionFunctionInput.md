# UMaterialExpressionFunctionInput

- Symbol Type: class
- Symbol Path: Others / UMaterialExpressionFunctionInput
- Source JSON Path: class/detail/Others/UMaterialExpressionFunctionInput.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFunctionInput.json
- Mirrored At (UTC): 2026-05-19 08:23:32Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Preview | FExpressionInput | Used for previewing when editing the function, or when bUsePreviewValueAsDefault is enabled. |  |
| InputName | FString | The input's name, which will be drawn on the connector in function call expressions that use this function. |  |
| Description | FString | The input's description, which will be used as a tooltip on the connector in function call expressions that use this function. |  |
| Id | FGuid | Id of this input, used to maintain references through name changes. |  |
| InputType | TEnumAsByte < enum EFunctionInputType > | Type of this input.  <br>	  Input code chunks will be cast to this type, and a compiler error will be emitted if the cast fails. |  |
| PreviewValue | FVector4 | Value used to preview this input when editing the material function. |  |
| bUsePreviewValueAsDefault | uint32 | Whether to use the preview value or texture as the default value for this input. |  |
| SortPriority | int32 | Controls where the input is displayed relative to the other inputs. |  |
| bCompilingFunctionPreview | uint32 | true when this expression is being compiled in a function preview, <br>	  false when this expression is being compiled into a material that uses the function.<br>	  Only valid in Compile() |  |

# UKismetMaterialLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetMaterialLibrary
- Source JSON Path: class/detail/Others/UKismetMaterialLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetMaterialLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### SetScalarParameterValue

Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Collection | UMaterialParameterCollection *  |  |  |
| ParameterName | FName  |  |  |
| ParameterValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetVectorParameterValue

Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Collection | UMaterialParameterCollection *  |  |  |
| ParameterName | FName  |  |  |
| ParameterValue | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetScalarParameterValue

Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Collection | UMaterialParameterCollection *  |  |  |
| ParameterName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API float  |  |  |

### GetVectorParameterValue

Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Collection | UMaterialParameterCollection *  |  |  |
| ParameterName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API FLinearColor  |  |  |

### CreateDynamicMaterialInstance

Creates a Dynamic Material Instance which you can modify during gameplay.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Parent | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API class UMaterialInstanceDynamic *  |  |  |

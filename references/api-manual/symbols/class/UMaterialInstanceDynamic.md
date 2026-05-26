# UMaterialInstanceDynamic

- Symbol Type: class
- Symbol Path: Others / UMaterialInstanceDynamic
- Source JSON Path: class/detail/Others/UMaterialInstanceDynamic.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInstanceDynamic.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Functions

### SetScalarParameterValue

Set a MID scalar (float) parameter value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetScalarParameterValue

Get the current scalar (float) parameter value from an MID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SetTextureParameterValue

Set an MID texture parameter value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Value | UTexture * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetTextureParameterValue

Get the current MID texture parameter value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UTexture *  |  |  |

### SetVectorParameterValue

Set an MID vector parameter value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Value | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetVectorParameterValue

Get the current MID vector parameter value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### K2_InterpolateMaterialInstanceParams

Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
	  The output is the object itself (this).
	  Supports the case SourceA==this || SourceB==this
	  Both material have to be from the same base material

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceA | UMaterialInstance *  | value that is used for Alpha=0, silently ignores the case if 0 |  |
| SourceB | UMaterialInstance *  | value that is used for Alpha=1, silently ignores the case if 0 |  |
| Alpha | float | usually in the range 0..1, values outside the range extrapolate |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_CopyMaterialInstanceParameters

Copies over parameters given a material interface (copy each instance following the hierarchy)
	  Very slow implementation, avoid using at runtime. Hopefully we can replace ity later with something like CopyInterpParameters()
	  The output is the object itself (this).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Source | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyInterpParameters

Copies over parameters given a material instance (only copy from the instance, not following the hierarchy)
	  much faster than K2_CopyMaterialInstanceParameters(),
	  The output is the object itself (this).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Source | UMaterialInstance * | ignores the call if 0 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyParameterOverrides

Copy parameter values from another material instance. This will copy only
	  parameters explicitly overridden in that material instance!!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialInstance | UMaterialInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

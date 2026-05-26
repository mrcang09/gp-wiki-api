# UAnimSingleNodeInstance

- Symbol Type: class
- Symbol Path: Others / UAnimSingleNodeInstance
- Source JSON Path: class/detail/Others/UAnimSingleNodeInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimSingleNodeInstance.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Functions

### SetLooping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsLooping | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlayRate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPlayRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReverse

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInReverse | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPosition | float  |  |  |
| bFireNotifies | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPositionWithPreviousTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPosition | float  |  |  |
| InPreviousTime | float  |  |  |
| bFireNotifies | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlendSpaceInput

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendInput | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlaying

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsPlaying | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLength

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### PlayAnim

For AnimSequence specific

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsLooping | bool  |  |  |
| InPlayRate | float  |  |  |
| InStartPosition | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopAnim

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetAnimationAsset

Set New Asset - calls InitializeAnimation, for now we need MeshComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAsset | UAnimationAsset *  |  |  |
| bIsLooping | bool  |  |  |
| InPlayRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAnimationAsset

Get the currently used asset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAnimationAsset * |  |  |

### SetPreviewCurveOverride

Set pose value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PoseName | FName &  |  |  |
| Value | float  |  |  |
| bRemoveIfZero | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

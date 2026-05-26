# UImage

- Symbol Type: class
- Symbol Path: Others / UImage
- Source JSON Path: class/detail/Others/UImage.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UImage.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

The image widget allows you to display a Slate Brush, or texture or material in the UI.
 
   No Children

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BrushImage | TSoftObjectPtr < UObject > |  |  |
| bIsEnhancedImage | bool |  |  |
| ForceAsyncLoadReference | bool |  |  |
| BrushAssetReference | FStringAssetReference |  |  |
| Brush | FSlateBrush | Image to draw |  |
| BrushMaterialParamNames | FString |  |  |
| BrushDelegate | FGetSlateBrush | A bindable delegate for the Image. |  |
| ColorAndOpacity | FLinearColor | Color and opacity |  |
| ColorAndOpacityDelegate | FGetLinearColor | A bindable delegate for the ColorAndOpacity. |  |
| bIsUseEnhancedHitTest | bool | 是否使用自定义触摸响应区域，在运行时修改无效 |  |
| HitTestAreaRadius | float | 圆形响应区域的半径，最大为控件边长一半，-1为控件大小一半 |  |
| OnMouseButtonDownEvent | FOnPointerEvent |  |  |

## Functions

### GetBrush

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSlateBrush |  |  |

### SetColorAndOpacity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColorAndOpacity | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColorRGBStr

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HexString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushImageReference

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetReference | FStringAssetReference |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushImageReferenceWithMatchSize

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetReference | FStringAssetReference  |  |  |
| bMatchSize | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushImageReferenceWithColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetReference | FStringAssetReference  |  |  |
| Color | FLinearColor  |  |  |
| bMatchSize | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOpacity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOpacity | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrush

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBrush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushFromAsset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Asset | USlateBrushAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushFromTexture

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Texture | UTexture2D *  |  |  |
| bMatchSize | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushFromTextureDynamic

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Texture | UTexture2DDynamic *  |  |  |
| bMatchSize | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushFromMaterial

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDynamicMaterial

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic * |  |  |

### SetDisablePaint

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDisablePaint | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReleaseAsyncSetBrushHandle

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnAsyncLoadImageAssetComplete

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnAsyncLoadAssetComplete

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

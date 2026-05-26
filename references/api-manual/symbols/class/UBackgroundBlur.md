# UBackgroundBlur

- Symbol Type: class
- Symbol Path: Others / UBackgroundBlur
- Source JSON Path: class/detail/Others/UBackgroundBlur.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBackgroundBlur.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

A background blur is a container widget that can contain one child widget, providing an opportunity 
  to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.
 
   Single Child
   Blur Effect

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Padding | FMargin | The padding area between the slot and the content it contains. |  |
| HorizontalAlignment | TEnumAsByte < EHorizontalAlignment > | The alignment of the content horizontally. |  |
| VerticalAlignment | TEnumAsByte < EVerticalAlignment > | The alignment of the content vertically. |  |
| bApplyAlphaToBlur | bool | True to modulate the strength of the blur based on the widget alpha. |  |
| BlurStrength | float | How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the gpu. |  |
| bOverrideAutoRadiusCalculation | bool | Whether or not the radius should be computed automatically or if it should use the radius |  |
| BlurType | TEnumAsByte < EBlurType > | Blur type |  |
| BlurDirection | float | Blur direction for directional blur |  |
| BlurCenter | FVector2D | Blur center for radial and rotate blur |  |
| BlurRadius | int32 | This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur<br>	  A larger value is more costly but allows for stronger blurs. |  |
| BlurMask | UTexture * | A blur mask texture |  |
| LowQualityFallbackBrush | FSlateBrush | An image to draw instead of applying a blur when low quality override mode is enabled. <br>	  You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1. <br>	  This is usually done in the project's scalability settings |  |
| BlurMaskBrush | FSlateBrush |  |  |

## Functions

### SetPadding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPadding | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHorizontalAlignment

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InHorizontalAlignment | EHorizontalAlignment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVerticalAlignment

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVerticalAlignment | EVerticalAlignment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetApplyAlphaToBlur

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInApplyAlphaToBlur | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlurRadius

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlurRadius | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlurStrength

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InStrength | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlurDirection

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDirection | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlurCenter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCenter | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBlurMask

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTexture | UTexture * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLowQualityFallbackBrush

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBrush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

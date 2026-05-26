# UTextRenderComponent

- Symbol Type: class
- Symbol Path: Others / UTextRenderComponent
- Source JSON Path: class/detail/Others/UTextRenderComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTextRenderComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

Renders text in the world with given font. Contains usual font related attributes such as Scale, Alignment, Color etc.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Text | FText | Text content, can be multi line using <br> as line separator |  |
| TextMaterial | UMaterialInterface * | Text material |  |
| Font | UFont * | Text font |  |
| HorizontalAlignment | TEnumAsByte < enum EHorizTextAligment > | Horizontal text alignment |  |
| VerticalAlignment | TEnumAsByte < enum EVerticalTextAligment > | Vertical text alignment |  |
| TextRenderColor | FColor | Color of the text, can be accessed as vertex color |  |
| XScale | float | Horizontal scale, default is 1.0 |  |
| YScale | float | Vertical scale, default is 1.0 |  |
| WorldSize | float | Vertical size of the fonts largest character in world units. Transform, XScale and YScale will affect final size. |  |
| InvDefaultSize | float | The inverse of the Font's character height. |  |
| HorizSpacingAdjust | float | Horizontal adjustment per character, default is 0.0 |  |
| VertSpacingAdjust | float | Vertical adjustment per character, default is 0.0 |  |
| bAlwaysRenderAsText | uint32 | Allows text to draw unmodified when using debug visualization modes. |  |

## Functions

### SetText

Change the text value and signal the primitives to be rebuilt 
	  The FString variant is deprecated in favor of the FText variant

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetText

Change the text value and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTextMaterial

Change the text material and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFont

Change the font and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | UFont * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHorizontalAlignment

Change the horizontal alignment and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | EHorizTextAligment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVerticalAlignment

Change the vertical alignment and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | EVerticalTextAligment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTextRenderColor

Change the text render color and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetXScale

Change the text X scale and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetYScale

Change the text Y scale and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHorizSpacingAdjust

Change the text horizontal spacing adjustment and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVertSpacingAdjust

Change the text vertical spacing adjustment and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWorldSize

Change the world size of the text and signal the primitives to be rebuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTextLocalSize

Get local size of text

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetTextWorldSize

Get world space size of text

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

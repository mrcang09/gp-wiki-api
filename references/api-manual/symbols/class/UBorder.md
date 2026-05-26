# UBorder

- Symbol Type: class
- Symbol Path: Others / UBorder
- Source JSON Path: class/detail/Others/UBorder.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBorder.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

A border is a container widget that can contain one child widget, providing an opportunity 
  to surround it with a background image and adjustable padding.
 
   Single Child
   Image

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HorizontalAlignment | TEnumAsByte < EHorizontalAlignment > | The alignment of the content horizontally. |  |
| VerticalAlignment | TEnumAsByte < EVerticalAlignment > | The alignment of the content vertically. |  |
| bShowEffectWhenDisabled | uint8 | Whether or not to show the disabled effect when this border is disabled |  |
| ContentColorAndOpacity | FLinearColor | Color and opacity multiplier of content in the border |  |
| ContentColorAndOpacityDelegate | FGetLinearColor | A bindable delegate for the ContentColorAndOpacity. |  |
| ResetBlendColor | bool |  |  |
| Padding | FMargin | The padding area between the slot and the content it contains. |  |
| Background | FSlateBrush | Brush to drag as the background |  |
| BackgroundDelegate | FGetSlateBrush | A bindable delegate for the Brush. |  |
| BrushColor | FLinearColor | Color and opacity of the actual border image |  |
| BrushColorDelegate | FGetLinearColor | A bindable delegate for the BrushColor. |  |
| DesiredSizeScale | FVector2D | Scales the computed desired size of this border and its contents. Useful<br>	  for making things that slide open without having to hard-code their size.<br>	  Note: if the parent widget is set up to ignore this widget's desired size,<br>	  then changing this value will have no effect. |  |
| OnMouseButtonDownEvent | FOnPointerEvent |  |  |
| OnMouseButtonUpEvent | FOnPointerEvent |  |  |
| OnMouseMoveEvent | FOnPointerEvent |  |  |
| OnMouseDoubleClickEvent | FOnPointerEvent |  |  |

## Functions

### SetContentColorAndOpacity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InContentColorAndOpacity | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetResetBlendColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bResetBlendColor | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

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

### SetBrushColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBrushColor | FLinearColor |  |  |

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
| Texture | UTexture2D * |  |  |

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

### SetDesiredSizeScale

Sets the DesireSizeScale of this border.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InScale | FVector2D |  The X and Y multipliers for the desired size |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

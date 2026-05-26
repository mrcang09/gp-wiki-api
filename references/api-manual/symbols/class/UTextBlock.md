# UTextBlock

- Symbol Type: class
- Symbol Path: Others / UTextBlock
- Source JSON Path: class/detail/Others/UTextBlock.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTextBlock.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

A simple static text widget.
 
   No Children
   Text

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Text | FText | The text to display |  |
| TextDelegate | FGetText | A bindable delegate to allow logic to drive the text of the widget |  |
| ColorAndOpacity | FSlateColor | The color of the text |  |
| ColorAndOpacityDelegate | FGetSlateColor | A bindable delegate for the ColorAndOpacity. |  |
| Font | FSlateFontInfo | The font to render the text with |  |
| ShadowOffset | FVector2D | The direction the shadow is cast |  |
| ShadowColorAndOpacity | FLinearColor | The color of the shadow |  |
| ShadowColorAndOpacityDelegate | FGetLinearColor | A bindable delegate for the ShadowColorAndOpacity. |  |
| MinDesiredWidth | float | The minimum desired size for the text |  |
| AutoEllipsisText | bool |  |  |
| MutiEllipsisText | bool |  |  |
| MutiEllipsisLine | int32 |  |  |
| bWrapWithInvalidationPanel | bool | If true, it will automatically wrap this text widget with an invalidation panel |  |

## Functions

### SetColorAndOpacity

Sets the color and opacity of the text in this text block

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColorAndOpacity | FSlateColor | The new text color and opacity |  |

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

### SetOpacity

Sets the opacity of the text in this text block

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOpacity | float | The new text opacity |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetShadowColorAndOpacity

Sets the color and opacity of the text drop shadow
	  Note: if opacity is zero no shadow will be drawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InShadowColorAndOpacity | FLinearColor | The new drop shadow color and opacity |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetShadowOffset

Sets the offset that the text drop shadow should be drawn at

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InShadowOffset | FVector2D | The new offset |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFont

Dynamically set the font info for this text block

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFontInfo | FSlateFontInfo | THe new font info |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetJustification

Set the text justification for this text block

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InJustification | ETextJustify :: Type | new justification |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVerticalJustification

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InJustification | ETextVerticalJustify :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNeedVerticalJustificationWhenOverflow

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMinDesiredWidth

Set the minimum desired width for this text block

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMinDesiredWidth | float | new minimum desired width |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAutoEllipsisText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAutoEllipsisText | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWrapTextAt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InWrapTextAt | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMutiEllipsisText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMutiEllipsisText | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetText

Gets the widget text

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText | The widget text |  |

### GetLocalText

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText |  |  |

### SetText

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText | The text to assign to the widget |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

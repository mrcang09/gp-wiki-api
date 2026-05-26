# USpinBox

- Symbol Type: class
- Symbol Path: Others / USpinBox
- Source JSON Path: class/detail/Others/USpinBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USpinBox.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float | Value stored in this spin box |  |
| ValueDelegate | FGetFloat | A bindable delegate to allow logic to drive the value of the widget |  |
| WidgetStyle | FSpinBoxStyle | The Style |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * |  |  |
| Delta | float | The amount by which to change the spin box value as the slider moves. |  |
| SliderExponent | float | The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta). |  |
| Font | FSlateFontInfo | Font color and opacity (overrides style) |  |
| Justification | TEnumAsByte < ETextJustify :: Type > | The justification the value text should appear as. |  |
| MinDesiredWidth | float | The minimum width of the spin box |  |
| ClearKeyboardFocusOnCommit | bool | Whether to remove the keyboard focus from the spin box when the value is committed |  |
| SelectAllTextOnCommit | bool | Whether to select the text in the spin box when the value is committed |  |
| ForegroundColor | FSlateColor |  |  |
| bOverride_MinValue | uint32 | Whether the optional MinValue attribute of the widget is set |  |
| bOverride_MaxValue | uint32 | Whether the optional MaxValue attribute of the widget is set |  |
| bOverride_MinSliderValue | uint32 | Whether the optional MinSliderValue attribute of the widget is set |  |
| bOverride_MaxSliderValue | uint32 | Whether the optional MaxSliderValue attribute of the widget is set |  |
| MinValue | float | The minimum allowable value that can be manually entered into the spin box |  |
| MaxValue | float | The maximum allowable value that can be manually entered into the spin box |  |
| MinSliderValue | float | The minimum allowable value that can be specified using the slider |  |
| MaxSliderValue | float | The maximum allowable value that can be specified using the slider |  |

## Functions

### GetValue

Get the current value of the spin box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetValue

Set the value of the spin box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetMinValue

Get the current minimum value that can be manually set in the spin box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetMinValue

Set the minimum value that can be manually set in the spin box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMinValue

Clear the minimum value that can be manually set in the spin box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetMaxValue

Get the current maximum value that can be manually set in the spin box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetMaxValue

Set the maximum value that can be manually set in the spin box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMaxValue

Clear the maximum value that can be manually set in the spin box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetMinSliderValue

Get the current minimum value that can be specified using the slider.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetMinSliderValue

Set the minimum value that can be specified using the slider.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMinSliderValue

Clear the minimum value that can be specified using the slider.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetMaxSliderValue

Get the current maximum value that can be specified using the slider.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetMaxSliderValue

Set the maximum value that can be specified using the slider.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMaxSliderValue

Clear the maximum value that can be specified using the slider.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetForegroundColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForegroundColor | FSlateColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

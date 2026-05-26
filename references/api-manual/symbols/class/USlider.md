# USlider

- Symbol Type: class
- Symbol Path: Others / USlider
- Source JSON Path: class/detail/Others/USlider.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USlider.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.
 
   No Children

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float | The volume value to display. |  |
| ValueDelegate | FGetFloat | A bindable delegate to allow logic to drive the value of the widget |  |
| WidgetStyle | FSliderStyle | The progress bar style |  |
| Orientation | TEnumAsByte < EOrientation > | The slider's orientation. |  |
| SliderBarColor | FLinearColor | The color to draw the slider bar in. |  |
| SliderHandleColor | FLinearColor | The color to draw the slider handle in. |  |
| IndentHandle | bool | Whether the slidable area should be indented to fit the handle. |  |
| Locked | bool | Whether the handle is interactive or fixed. |  |
| StepSize | float | The amount to adjust the value by, when using a controller or keyboard |  |
| IsFocusable | bool | Should the slider be focusable? |  |
| SupportClickChange | bool |  |  |

## Functions

### GetValue

Gets the current value of the slider.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetValue

Sets the current value of the slider.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIndentHandle

Sets if the slidable area should be indented to fit the handle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLocked

Sets the handle to be interactive or fixed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStepSize

Sets the amount to adjust the value by, when using a controller or keyboard

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSliderBarColor

Sets the color of the slider bar

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSliderHandleColor

Sets the color of the handle bar

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

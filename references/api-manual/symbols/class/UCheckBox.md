# UCheckBox

- Symbol Type: class
- Symbol Path: Others / UCheckBox
- Source JSON Path: class/detail/Others/UCheckBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCheckBox.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and 
  'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
  or as radio buttons.
  
   Single Child
   Toggle

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CheckedState | ECheckBoxState | Whether the check box is currently in a checked state |  |
| CheckedStateDelegate | FGetCheckBoxState | A bindable delegate for the IsChecked. |  |
| WidgetStyle | FCheckBoxStyle | The checkbox bar style |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * | Style of the check box |  |
| UncheckedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is unchecked |  |
| UncheckedHoveredImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is unchecked and hovered |  |
| UncheckedPressedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is unchecked and pressed |  |
| CheckedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is checked |  |
| CheckedHoveredImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is checked and hovered |  |
| CheckedPressedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is checked and pressed |  |
| UndeterminedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is in an ambiguous state and hovered |  |
| UndeterminedHoveredImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is checked and hovered |  |
| UndeterminedPressedImage_DEPRECATED | USlateBrushAsset * | Image to use when the checkbox is in an ambiguous state and pressed |  |
| HorizontalAlignment | TEnumAsByte < EHorizontalAlignment > | How the content of the toggle button should align within the given space |  |
| Padding_DEPRECATED | FMargin | Spacing between the check box image and its content |  |
| BorderBackgroundColor_DEPRECATED | FSlateColor | The color of the background border |  |
| IsFocusable | bool | Sometimes a button should only be mouse-clickable and never keyboard focusable. |  |

## Functions

### IsPressed

Returns true if this button is currently pressed

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsChecked

Returns true if the checkbox is currently checked

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetCheckedState

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECheckBoxState | the full current checked state. |  |

### SetIsChecked

Sets the checked state.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsChecked | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCheckedState

Sets the checked state.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCheckedState | ECheckBoxState |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

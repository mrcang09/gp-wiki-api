# UComboBoxKey

- Symbol Type: class
- Symbol Path: Others / UComboBoxKey
- Source JSON Path: class/detail/Others/UComboBoxKey.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UComboBoxKey.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.
  Use OnGenerateConentWidgetEvent to return a custom built widget.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Options | TArray < TSharedPtr < FName > > | . |  |
| SelectedOption | TSharedPtr < FName > |  |  |
| WidgetStyle | FComboBoxStyle | The combobox style. |  |
| ItemStyle | FTableRowStyle | The item row style. |  |
| ScrollBarStyle | FScrollBarStyle | The scroll bar style. |  |
| ForegroundColor | FSlateColor | The foreground color to pass through the hierarchy. |  |
| ContentPadding | FMargin |  |  |
| MaxListHeight | float | The max height of the combobox list that opens |  |
| bHasDownArrow | bool | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |  |
| bEnableGamepadNavigationMode | bool | When false, directional keys will change the selection. When true, ComboBox<br>	  must be activated and will only capture arrow input while activated. |  |
| bIsFocusable | bool | When true, allows the combo box to receive keyboard focus |  |

## Functions

### AddOption

Add an element to the option list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### RemoveOption

Remove an element to the option list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool  |  |  |

### ClearOptions

Remove all the elements of the option list.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void |  |  |

### ClearSelection

Clear the current selection.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void |  |  |

### SetSelectedOption

Set the current selected option.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetSelectedOption

Get the current selected option

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API FName |  |  |

### IsOpen

Is the combobox menu opened.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool |  |  |

### SetContentPadding

Set the padding for content.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPadding | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetContentPadding

Get the padding for content.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API FMargin |  |  |

### IsEnableGamepadNavigationMode

Is the combobox navigated by gamepad.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool |  |  |

### SetEnableGamepadNavigationMode

Set whether the combobox is navigated by gamepad.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InEnableGamepadNavigationMode | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### IsHasDownArrow

Is the combobox arrow showing.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool |  |  |

### SetHasDownArrow

Set whether the combobox arrow is showing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InHasDownArrow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetMaxListHeight

Get the maximum height of the combobox list.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API float |  |  |

### SetMaxListHeight

Set the maximum height of the combobox list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaxHeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetWidgetStyle

Get the style of the combobox.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const UMG_API FComboBoxStyle & |  |  |

### SetWidgetStyle

Set the style of the combobox.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InWidgetStyle | FComboBoxStyle & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetItemStyle

Get the style of the items.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const UMG_API FTableRowStyle & |  |  |

### SetItemStyle

Set the style of the items.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InItemStyle | FTableRowStyle & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### GetScrollBarStyle

Get the style of the scrollbar.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const UMG_API FScrollBarStyle & |  |  |

### IsFocusable

Is the combobox focusable.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool |  |  |

### GetForegroundColor

Get the foreground color of the button.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API FSlateColor |  |  |

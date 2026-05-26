# UComboBoxString

- Symbol Type: class
- Symbol Path: Others / UComboBoxString
- Source JSON Path: class/detail/Others/UComboBoxString.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UComboBoxString.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefaultOptions | TArray < FString > | The default list of items to be displayed on the combobox. |  |
| SelectedOption | FString | The item in the combobox to select by default |  |
| WidgetStyle | FComboBoxStyle | The style. |  |
| ItemStyle | FTableRowStyle | The item row style. |  |
| ScrollBarStyle | FScrollBarStyle | The scroll bar style. |  |
| ContentPadding | FMargin |  |  |
| MaxListHeight | float | The max height of the combobox list that opens |  |
| HasDownArrow | bool | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |  |
| EnableGamepadNavigationMode | bool | When false, directional keys will change the selection. When true, ComboBox <br>	 must be activated and will only capture arrow input while activated. |  |
| Font | FSlateFontInfo | The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent<br>	  to factory each new entry. |  |
| ForegroundColor | FSlateColor | The foreground color to pass through the hierarchy. |  |
| bIsFocusable | bool |  |  |
| bForceNotify | bool |  |  |
| OnGenerateWidgetEvent | FGenerateWidgetForString | Called when the widget is needed for the item. |  |
| OnGenerateSelectWidgetEvent | FGenerateWidgetForString |  |  |

## Functions

### AddOption

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveOption

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FindOptionIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetOptionAtIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### ClearOptions

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClearSelection

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RefreshOptions

Refreshes the list of options.  If you added new ones, and want to update the list even if it's
	  currently being displayed use this.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetSelectedOption

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Option | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSelectedOption

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetOptionCount

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | The number of options |  |

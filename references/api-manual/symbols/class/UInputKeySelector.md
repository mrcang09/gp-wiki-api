# UInputKeySelector

- Symbol Type: class
- Symbol Path: Others / UInputKeySelector
- Source JSON Path: class/detail/Others/UInputKeySelector.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInputKeySelector.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

A widget for selecting a single key or a single key with a modifier.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetStyle | FButtonStyle | The button style used at runtime |  |
| TextStyle | FTextBlockStyle | The button style used at runtime |  |
| SelectedKey | FInputChord | The currently selected key chord. |  |
| Font_DEPRECATED | FSlateFontInfo |  |  |
| Margin | FMargin | The amount of blank space around the text used to display the currently selected key. |  |
| ColorAndOpacity_DEPRECATED | FLinearColor |  |  |
| KeySelectionText | FText | Sets the text which is displayed while selecting keys. |  |
| NoKeySpecifiedText | FText | Sets the text to display when no key text is available or not selecting a key. |  |
| bAllowModifierKeys | bool | When true modifier keys such as control and alt are allowed in the <br>	 input chord representing the selected key, if false modifier keys are ignored. |  |
| bAllowGamepadKeys | bool | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |  |
| EscapeKeys | TArray < FKey > | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |  |

## Functions

### SetSelectedKey

Sets the currently selected key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSelectedKey | FInputChord & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetKeySelectionText

Sets the text which is displayed while selecting keys.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InKeySelectionText | FText |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNoKeySpecifiedText

Sets the text to display when no key text is available or not selecting a key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNoKeySpecifiedText | FText |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllowModifierKeys

Sets whether or not modifier keys are allowed in the selected key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInAllowModifierKeys | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllowGamepadKeys

Sets whether or not gamepad keys are allowed in the selected key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInAllowGamepadKeys | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetIsSelectingKey

Returns true if the widget is currently selecting a key, otherwise returns false.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetTextBlockVisibility

Sets the visibility of the text block.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVisibility | ESlateVisibility |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

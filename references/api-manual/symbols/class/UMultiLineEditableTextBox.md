# UMultiLineEditableTextBox

- Symbol Type: class
- Symbol Path: Others / UMultiLineEditableTextBox
- Source JSON Path: class/detail/Others/UMultiLineEditableTextBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMultiLineEditableTextBox.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Allows a user to enter multiple lines of text

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Text | FText | The text content for this editable text box widget |  |
| HintText | FText | Hint text that appears when there is no text in the text box |  |
| HintTextDelegate | FGetText | A bindable delegate to allow logic to drive the hint text of the widget |  |
| WidgetStyle | FEditableTextBoxStyle | The style |  |
| TextStyle | FTextBlockStyle | The text style |  |
| bIsReadOnly | bool | Sets whether this text block can be modified interactively by the user |  |
| AllowContextMenu | bool | Whether the context menu can be opened |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * |  |  |
| Font_DEPRECATED | FSlateFontInfo | Font color and opacity (overrides Style) |  |
| ForegroundColor_DEPRECATED | FLinearColor | Text color and opacity (overrides Style) |  |
| BackgroundColor_DEPRECATED | FLinearColor | The color of the backgroundborder around the editable text (overrides Style) |  |
| ReadOnlyForegroundColor_DEPRECATED | FLinearColor | Text color and opacity when read-only (overrides Style) |  |

## Functions

### GetText

Provide a alternative mechanism for error reporting.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText |  |  |

### SetText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHintText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetError

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InError | FText |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIsReadOnly

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bReadOnly | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIsEnableMultiLineTextInsertNewLine

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

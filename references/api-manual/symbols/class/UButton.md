# UButton

- Symbol Type: class
- Symbol Path: Others / UButton
- Source JSON Path: class/detail/Others/UButton.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UButton.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

The button is a click-able primitive widget to enable basic interaction, you
  can place any other widget inside a button to make a more complex and
  interesting click-able element in your UI.
 
   Single Child
   Clickable

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Style_DEPRECATED | USlateWidgetStyleAsset * | The template style asset, used to seed the mutable instance of the style. |  |
| WidgetStyle | FButtonStyle | The button style used at runtime |  |
| ColorAndOpacity | FLinearColor | The color multiplier for the button content |  |
| BackgroundColor | FLinearColor | The color multiplier for the button background |  |
| ClickMethod | TEnumAsByte < EButtonClickMethod :: Type > | The type of mouse action required by the user to trigger the buttons 'Click' |  |
| TouchMethod | TEnumAsByte < EButtonTouchMethod :: Type > | The type of touch action required by the user to trigger the buttons 'Click' |  |
| ListenEscMethod | TEnumAsByte < EListenEscMethod :: Type > | 通过命名识别关闭按钮，识别忽略大小写下划线，推荐命名(Button_Close,NewButton_Close...) |  |
| ListenActions | TArray < FButtonListenAction > | 通过监听Action，来统一模拟按键点击，扩展Esc模拟点击功能 |  |
| IsTipsBgBtn | bool | 是否为Tips背景按钮 |  |
| IsFocusable | bool | Sometimes a button should only be mouse-clickable and never keyboard focusable. |  |
| IsPassMouseEvent | bool |  |  |
| IsImgAlphaBtn | bool |  |  |
| bUseCustomSettings | bool |  |  |
| CustomHitAreaTexture | UTexture2D * |  |  |
| CustomHitAreaAlpha | int |  |  |
| bIsShowHover | bool |  |  |
| OnMouseButtonDownEvent | FOnPointerEvent |  |  |
| OnMouseButtonUpEvent | FOnPointerEvent |  |  |
| OnMouseMoveEvent | FOnPointerEvent |  |  |
| InputActionBindings | FButtonInputActionBindingsStruct |  |  |
| EscRespondSetting | FEscRespondSetting |  |  |
| IsThisFrameClicked | bool |  |  |

## Functions

### SetStyle

Sets the color multiplier for the button background

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InStyle | FButtonStyle & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColorAndOpacity

Sets the color multiplier for the button content

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColorAndOpacity | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBackgroundColor

Sets the color multiplier for the button background

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBackgroundColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsPressed

Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the user is actively pressing the button otherwise false. |  |

### Release

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetClickMethod

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InClickMethod | EButtonClickMethod :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTouchMethod

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTouchMethod | EButtonTouchMethod :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetReleasedReason

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8 |  |  |

### SetListenEscMethod

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InListenEscMethod | EListenEscMethod :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetListenEscMethod

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EListenEscMethod :: Type |  |  |

### SetShowHover

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InShowHover | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddListenAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActionName | FName  |  |  |
| InType | EButtonListenActionEvent :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveListenAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActionName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearListenActions

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCacheLayerId

return CacheLayerId only windows

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### RespondEscape

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetButtonsFromAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutButtons | TArray < UButton * > &  |  |  |
| InAction | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClearInvalidForListenActions

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetButtonsFromTipsBg

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UButton * > |  |  |

### SetButtonClickedGlobalEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InEvent | FOnButtonClickedGlobalEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearButtonClickedGlobalEvent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetIsFocusable

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFocusable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UScrollBox

- Symbol Type: class
- Symbol Path: Others / UScrollBox
- Source JSON Path: class/detail/Others/UScrollBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UScrollBox.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetStyle | FScrollBoxStyle | The style |  |
| WidgetBarStyle | FScrollBarStyle | The bar style |  |
| OverscrollLooseness | float | Overscroll Looseness |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * |  |  |
| BarStyle_DEPRECATED | USlateWidgetStyleAsset * |  |  |
| Orientation | TEnumAsByte < EOrientation > | The orientation of the scrolling and stacking in the box. |  |
| ScrollBarVisibility | ESlateVisibility | Visibility |  |
| ConsumeMouseWheel | EConsumeMouseWheel | Enable to always consume mouse wheel event, even when scrolling is not possible |  |
| ScrollbarThickness | FVector2D |  |  |
| AlwaysShowScrollbar | bool |  |  |
| AllowOverscroll | bool | Disable to stop scrollbars from activating inertial overscrolling |  |
| NavigationDestination | EDescendantScrollDestination |  |  |
| NavigationScrollPadding | float | The amount of padding to ensure exists between the item being navigated to, at the edge of the<br>	  scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to. |  |
| bAllowRightClickDragScrolling | bool | Option to disable right-click-drag scrolling |  |
| bScrollEnabled | bool | 启用滑动 |  |
| bScrollDisableHandled | bool | 启用滑动 |  |
| bPreciseScroll | bool | 启用精准滑动 |  |
| bDisableDragListScroll | bool | 依旧可以通过拖拽bar或者鼠标滚轮滑动, 仅PC版生效 |  |

## Functions

### SetOrientation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewOrientation | EOrientation |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScrollBarVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScrollBarVisibility | ESlateVisibility |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScrollbarThickness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScrollbarThickness | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAlwaysShowScrollbar

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAlwaysShowScrollbar | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllowOverscroll

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAllowOverscroll | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCacheOverscrollOffset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetOverscrollLooseness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| v | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScrollEnabled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InScrollEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScrollDisableHandled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InScrollDisableHandled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScrollPrecise

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InScrollPrecise | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDragListScrollEnabled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDragListScrollEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsReachEnd

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsLargerThanContentSize

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetScrollOffset

Updates the scroll offset of the scrollbox.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScrollOffset | float | is in Slate Units. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetScrollOffset

Gets the scroll offset of the scrollbox in Slate Units.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### ScrollToStart

Scrolls the ScrollBox to the top instantly

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ScrollToEnd

Scrolls the ScrollBox to the bottom instantly during the next layout pass.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopScroll

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ScrollWidgetIntoView

Scrolls the ScrollBox to the widget during the next layout pass.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetToFind | UWidget *  |  |  |
| AnimateScroll | bool  |  |  |
| ScrollDestination | EDescendantScrollDestination |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

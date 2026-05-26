# UWidgetSwitcher

- Symbol Type: class
- Symbol Path: Others / UWidgetSwitcher
- Source JSON Path: class/detail/Others/UWidgetSwitcher.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSwitcher.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActiveWidgetIndex | int32 | The slot index to display |  |
| bHideInactiveWidgets | bool |  |  |
| ActiveWidgetIndexDelegate | FGetInt32 |  |  |

## Functions

### GetNumWidgets

Gets the number of widgets that this switcher manages.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetActiveWidgetIndex

Gets the slot index of the currently active widget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetLocalActiveWidgetIndex

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetActiveWidgetIndex

Activates the widget at the specified index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActiveWidget

Activates the widget and makes it the active index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetWidgetAtIndex

Get a widget at the provided index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget *  |  |  |

### GetActiveWidget

Get the reference of the currently active widget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget * |  |  |

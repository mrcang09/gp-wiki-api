# UPanelWidget

- Symbol Type: class
- Symbol Path: Others / UPanelWidget
- Source JSON Path: class/detail/Others/UPanelWidget.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPanelWidget.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Slots | TArray < UPanelSlot * > | The slots in the widget holding the child widgets of this panel. |  |
| CachedContents_ForGC | TArray < UWidget * > |  |  |

## Functions

### GetChildrenCount

Gets number of child widgets in the container.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetChildAt

Gets the widget at an index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 | The index of the widget. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget *  | The widget at the given index, or nothing if there is no widget there. |  |

### GetChildIndex

Gets the index of a specific child widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### HasChild

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if panel contains this widget |  |

### RemoveChildAt

Removes a child by it's index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### AddChild

Adds a new child widget to the container.  Returns the base slot type, 
	  requires casting to turn it into the type specific to the container.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPanelSlot *  |  |  |

### InsertChildAtIndex

Insert a widget at a specific index, available in game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32  |  |  |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPanelSlot *  |  |  |

### ShiftChildToIndex

Moves the child widget from its current index to the new index provided, available in game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32  |  |  |
| Child | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveChild

Removes a specific widget from the container.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the widget was found and removed. |  |

### HasAnyChildren

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if there are any child widgets in the panel |  |

### ClearChildren

Remove all child widgets from the panel widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

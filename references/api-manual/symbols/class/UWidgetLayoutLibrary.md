# UWidgetLayoutLibrary

- Symbol Type: class
- Symbol Path: Others / UWidgetLayoutLibrary
- Source JSON Path: class/detail/Others/UWidgetLayoutLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetLayoutLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Functions

### ProjectWorldLocationToWidgetPosition

Gets the projected world to screen position for a player, then converts it into a widget
	  position, which takes into account any quality scaling.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController *  | The player controller to project the position in the world to their screen. |  |
| WorldLocation | FVector  | The world location to project from. |  |
| ScreenPosition | FVector2D & | The position in the viewport with quality scale removed and DPI scale remove. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the position projects onto the screen. |  |

### GetViewportScale

Gets the current DPI Scale being applied to the viewport and all the Widgets.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetViewportSize

Gets the size of the game viewport.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### GetViewportWidgetGeometry

Gets the geometry of the widget holding all widgets added to the "Viewport".  You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGeometry  |  |  |

### GetPlayerScreenWidgetGeometry

Gets the geometry of the widget holding all widgets added to the "Player Screen". You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGeometry  |  |  |

### GetMousePositionOnPlatform

Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### GetMousePositionOnViewport

Gets the platform's mouse cursor position in the local space of the viewport widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### GetMousePositionScaledByDPI

Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
	  to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.
	 
	  MousePositionScaledByDPI = MousePosition  (1  ViewportScale).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController *  |  |  |
| LocationX | float &  |  |  |
| LocationY | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SlotAsBorderSlot

Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a border panel. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UBorderSlot *  |  |  |

### SlotAsCanvasSlot

Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a canvas panel. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCanvasPanelSlot *  |  |  |

### SlotAsGridSlot

Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a grid panel. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGridSlot *  |  |  |

### SlotAsHorizontalBoxSlot

Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a Horizontal Box. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UHorizontalBoxSlot *  |  |  |

### SlotAsOverlaySlot

Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a overlay panel. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UOverlaySlot *  |  |  |

### SlotAsUniformGridSlot

Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a uniform grid panel. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUniformGridSlot *  |  |  |

### SlotAsVerticalBoxSlot

Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * | The child widget of a Vertical Box. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UVerticalBoxSlot *  |  |  |

### RemoveAllWidgets

Removes all widgets from the viewport.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNewUsedLayerPolicy

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget *  |  |  |
| NewLayerPolicy | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

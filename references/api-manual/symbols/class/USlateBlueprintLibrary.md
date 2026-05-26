# USlateBlueprintLibrary

- Symbol Type: class
- Symbol Path: Others / USlateBlueprintLibrary
- Source JSON Path: class/detail/Others/USlateBlueprintLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USlateBlueprintLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Functions

### IsUnderLocation

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry &  |  |  |
| AbsoluteCoordinate | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the provided location in absolute coordinates is within the bounds of this geometry. |  |

### AbsoluteToLocal

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry &  |  |  |
| AbsoluteCoordinate | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  | Transforms AbsoluteCoordinate into the local space of this Geometry. |  |

### LocalToAbsolute

Translates local coordinates into absolute coordinates
	 
	  Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry &  |  |  |
| LocalCoordinate | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  Absolute coordinates |  |

### GetLocalSize

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  | the size of the geometry in local space. |  |

### GetAbsoluteSize

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  | the size of the geometry in absolute space. |  |

### GetAbsolutePosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### EqualEqual_SlateBrush

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FSlateBrush &  |  |  |
| B | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether brushes A and B are identical. |  |

### LocalToViewport

Translates local coordinate of the geometry provided into local viewport coordinates.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Geometry | FGeometry &  |  |  |
| LocalCoordinate | FVector2D  |  |  |
| PixelPosition | FVector2D &  | The position in the game's viewport, usable for line traces and |  |
| ViewportPosition | FVector2D & | The position in the space of other widgets in the viewport. Like if you wanted |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AbsoluteToViewport

Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| AbsoluteDesktopCoordinate | FVector2D  |  |  |
| PixelPosition | FVector2D &  | The position in the game's viewport, usable for line traces and |  |
| ViewportPosition | FVector2D & | The position in the space of other widgets in the viewport. Like if you wanted |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScreenToWidgetLocal

Translates a screen position in pixels into the local space of a widget with the given geometry.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Geometry | FGeometry &  |  |  |
| ScreenPosition | FVector2D  |  |  |
| LocalCoordinate | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScreenToWidgetAbsolute

Translates a screen position in pixels into absolute application coordinates.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ScreenPosition | FVector2D  |  |  |
| AbsoluteCoordinate | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScreenToViewport

Translates a screen position in pixels into the local space of the viewport widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ScreenPosition | FVector2D  |  |  |
| ViewportPosition | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSlateConstant_GlobalScrollAmount

Provide GetGlobalScrollAmount() to Lua.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### ReleaseAllMouseCapture

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReleaseMouseCaptureWithIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReleaseAllMousePassThroughCapture

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReleaseMousePassThroughCaptureWithIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMouseCaptor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerIndex | int32  |  |  |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetMousePassThroughCaptor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerIndex | int32  |  |  |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

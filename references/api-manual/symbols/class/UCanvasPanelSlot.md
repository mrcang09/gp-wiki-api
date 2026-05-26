# UCanvasPanelSlot

- Symbol Type: class
- Symbol Path: Others / UCanvasPanelSlot
- Source JSON Path: class/detail/Others/UCanvasPanelSlot.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCanvasPanelSlot.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LayoutData | FAnchorData | The anchoring information for the slot |  |
| bAutoSize | bool | When AutoSize is true we use the widget's desired size |  |
| ZOrder | int32 | The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top). |  |
| bAntiAdaptation | bool |  |  |

## Functions

### SetLayout

Sets the layout data of the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLayoutData | FAnchorData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLayout

Gets the layout data of the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FAnchorData |  |  |

### SetPosition

Sets the position of the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPosition | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPosition

Gets the position of the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetSize

Sets the size of the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSize | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSize

Gets the size of the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetOffsets

Sets the offset data of the slot, which could be position and size, or margins depending on the anchor points

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOffset | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOffsets

Gets the offset data of the slot, which could be position and size, or margins depending on the anchor points

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FMargin |  |  |

### SetAnchors

Sets the anchors on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnchors | FAnchors |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAnchors

Gets the anchors on the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FAnchors |  |  |

### SetAlignment

Sets the alignment on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAlignment | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAlignment

Gets the alignment on the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetAutoSize

Sets if the slot to be auto-sized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InbAutoSize | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAutoSize

Gets if the slot to be auto-sized

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetZOrder

Sets the z-order on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InZOrder | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetZOrder

Gets the z-order on the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetAntiAdaptation

Sets the bAntiAdaptation on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InbAntiAdaptation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAntiAdaptation

Gets the bAntiAdaptation on the slot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetMinimum

Sets the anchors on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMinimumAnchors | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMaximum

Sets the anchors on the slot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaximumAnchors | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnAntiAdaptationOffsetsChange

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

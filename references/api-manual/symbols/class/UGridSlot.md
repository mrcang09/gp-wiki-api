# UGridSlot

- Symbol Type: class
- Symbol Path: Others / UGridSlot
- Source JSON Path: class/detail/Others/UGridSlot.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGridSlot.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

A slot for UGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Padding | FMargin | The padding area between the slot and the content it contains. |  |
| HorizontalAlignment | TEnumAsByte < EHorizontalAlignment > | The alignment of the object horizontally. |  |
| VerticalAlignment | TEnumAsByte < EVerticalAlignment > | The alignment of the object vertically. |  |
| Row | int32 | The row index of the cell this slot is in |  |
| RowSpan | int32 |  |  |
| Column | int32 | The column index of the cell this slot is in |  |
| ColumnSpan | int32 |  |  |
| Layer | int32 | Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset. |  |
| Nudge | FVector2D | Offset this slot's content by some amount; positive values offset to lower right |  |

## Functions

### SetPadding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPadding | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRow

Sets the row index of the slot, this determines what cell the slot is in the panel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRow | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRowSpan

How many rows this this slot spans over

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRowSpan | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColumn

Sets the column index of the slot, this determines what cell the slot is in the panel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColumn | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColumnSpan

How many columns this slot spans over

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColumnSpan | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLayer

Sets positive values offset this cell to be hit-tested and drawn on top of others.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLayer | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHorizontalAlignment

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InHorizontalAlignment | EHorizontalAlignment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVerticalAlignment

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVerticalAlignment | EVerticalAlignment |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

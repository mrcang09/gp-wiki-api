# UDragDropOperation

- Symbol Type: class
- Symbol Path: Others / UDragDropOperation
- Source JSON Path: class/detail/Others/UDragDropOperation.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDragDropOperation.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FString | A simple string tag you can optionally use to provide extra metadata about the operation. |  |
| Payload | UObject * | The payload of the drag operation.  This can be any UObject that you want to pass along as dragged data.  If you <br>	  were building an inventory screen this would be the UObject representing the item being moved to another slot. |  |
| DefaultDragVisual | UWidget * | The Drag Visual is the widget to display when dragging the item.  Normally people create a new widget to represent the <br>	  temporary drag. |  |
| Pivot | EDragPivot | Controls where the drag widget visual will appear when dragged relative to the pointer performing<br>	  the drag operation. |  |
| Offset | FVector2D | A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual. |  |
| StartOffset | FVector2D |  |  |
| bRemoveMoveAnimDelay | bool |  |  |

## Functions

### Drop

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DragCancelled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Dragged

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

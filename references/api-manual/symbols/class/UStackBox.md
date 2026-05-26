# UStackBox

- Symbol Type: class
- Symbol Path: Others / UStackBox
- Source JSON Path: class/detail/Others/UStackBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UStackBox.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A stack box widget is a layout panel allowing child widgets to be automatically laid out
  vertically or horizontally.
 
   Many Children
   Flows Vertical or Horizontal

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Orientation | TEnumAsByte < EOrientation > | The orientation of the stack box. |  |

## Functions

### GetOrientation

Get the orientation of the stack box.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API EOrientation |  |  |

### SetOrientation

Set the orientation of the stack box. The existing elements will be rearranged.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InType | EOrientation |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API void  |  |  |

### AddChildToStackBox

Adds a new child widget to the container.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API UStackBoxSlot *  |  |  |

### ReplaceStackBoxChildAt

Replace the widget at the given index it with a different widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32  |  |  |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API bool  |  |  |

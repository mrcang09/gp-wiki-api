# UCircularThrobber

- Symbol Type: class
- Symbol Path: Others / UCircularThrobber
- Source JSON Path: class/detail/Others/UCircularThrobber.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCircularThrobber.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A throbber widget that orients images in a spinning circle.
  
   No Children
   Spinner Progress

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NumberOfPieces | int32 | How many pieces there are |  |
| Period | float | The amount of time for a full circle (in seconds) |  |
| Radius | float | The radius of the circle. If the throbber is a child of Canvas Panel, the 'Size to Content' option must be enabled in order to set Radius. |  |
| PieceImage_DEPRECATED | USlateBrushAsset * | Image to use for each segment of the throbber |  |
| Image | FSlateBrush |  |  |
| bEnableRadius | bool |  |  |

## Functions

### SetNumberOfPieces

Sets how many pieces there are.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNumberOfPieces | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPeriod

Sets the amount of time for a full circle (in seconds).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPeriod | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRadius

Sets the radius of the circle.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRadius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

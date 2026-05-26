# UScrollBar

- Symbol Type: class
- Symbol Path: Others / UScrollBar
- Source JSON Path: class/detail/Others/UScrollBar.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UScrollBar.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetStyle | FScrollBarStyle | Style of the scrollbar |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * |  |  |
| bAlwaysShowScrollbar | bool |  |  |
| Orientation | TEnumAsByte < EOrientation > |  |  |
| Thickness | FVector2D | The thickness of the scrollbar thumb |  |

## Functions

### SetState

Set the offset and size of the track's thumb.
	 Note that the maximum offset is 1.0-ThumbSizeFraction.
	 If the user can view 13 of the items in a single page, the maximum offset will be ~0.667f

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOffsetFraction | float  |   Offset of the thumbnail from the top as a fraction of the total available scroll space. |  |
| InThumbSizeFraction | float | Size of thumbnail as a fraction of the total available scroll space. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

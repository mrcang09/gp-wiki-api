# UArrowComponent

- Symbol Type: class
- Symbol Path: Others / UArrowComponent
- Source JSON Path: class/detail/Others/UArrowComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UArrowComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

A simple arrow rendered using lines. Useful for indicating which way an object is facing.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ArrowColor | FColor |  |  |
| ArrowSize | float |  |  |
| bIsScreenSizeScaled | bool | Set to limit the screen size of this arrow |  |
| ScreenSize | float | The size on screen to limit this arrow to (in screen space) |  |
| bTreatAsASprite | uint32 | If true, don't show the arrow when EngineShowFlags.BillboardSprites is disabled. |  |

## Functions

### SetArrowColor

Updates the arrow's colour, and tells it to refresh

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

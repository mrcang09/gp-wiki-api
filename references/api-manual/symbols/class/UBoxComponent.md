# UBoxComponent

- Symbol Type: class
- Symbol Path: Others / UBoxComponent
- Source JSON Path: class/detail/Others/UBoxComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBoxComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

A box generally used for simple collision. Bounds are rendered as lines in the editor.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoxExtent | FVector | The extents (radii dimensions) of the box |  |
| LineThickness | float | Used to control the line thickness when rendering |  |

## Functions

### SetBoxExtent

Change the box extent size. This is the unscaled size, before component scale is applied.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoxExtent | FVector  |  |  |
| bUpdateOverlaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetScaledBoxExtent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetUnscaledBoxExtent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

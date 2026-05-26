# UMeshVertexPainterKismetLibrary

- Symbol Type: class
- Symbol Path: Others / UMeshVertexPainterKismetLibrary
- Source JSON Path: class/detail/Others/UMeshVertexPainterKismetLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMeshVertexPainterKismetLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Functions

### PaintVerticesSingleColor

Paints vertex colors on a mesh component in a specified color.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMeshComponent | UStaticMeshComponent *  |  |  |
| FillColor | FLinearColor &  |  |  |
| bConvertToSRGB | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PaintVerticesLerpAlongAxis

Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMeshComponent | UStaticMeshComponent *  |  |  |
| StartColor | FLinearColor &  |  |  |
| EndColor | FLinearColor &  |  |  |
| Axis | EVertexPaintAxis  |  |  |
| bConvertToSRGB | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemovePaintedVertices

Removes vertex colors on a mesh component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMeshComponent | UStaticMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UPaperTerrainComponent

- Symbol Type: class
- Symbol Path: Others / UPaperTerrainComponent
- Source JSON Path: class/detail/Others/UPaperTerrainComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperTerrainComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

The terrain visualization component for an associated spline component.
  This takes a 2D terrain material and instances sprite geometry along the spline path.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TerrainMaterial | UPaperTerrainMaterial * | The terrain material to apply to this component (set of rules for which sprites are used on different surfaces or the interior) |  |
| bClosedSpline | bool |  |  |
| bFilledSpline | bool |  |  |
| AssociatedSpline | UPaperTerrainSplineComponent * |  |  |
| RandomSeed | int32 | Random seed used for choosing which spline meshes to use. |  |
| SegmentOverlapAmount | float | The overlap amount between segments |  |
| TerrainColor | FLinearColor | The color of the terrain (passed to the sprite material as a vertex color) |  |
| ReparamStepsPerSegment | int32 | Number of steps per spline segment to place in the reparameterization table |  |
| SpriteCollisionDomain | TEnumAsByte < ESpriteCollisionMode :: Type > | Collision domain (no collision, 2D (experimental), or 3D) |  |
| CollisionThickness | float | The extrusion thickness of collision geometry when using a 3D collision domain |  |
| CachedBodySetup | UBodySetup * | Description of collision |  |

## Functions

### SetTerrainColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

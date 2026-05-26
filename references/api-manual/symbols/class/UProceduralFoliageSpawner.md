# UProceduralFoliageSpawner

- Symbol Type: class
- Symbol Path: Others / UProceduralFoliageSpawner
- Source JSON Path: class/detail/Others/UProceduralFoliageSpawner.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageSpawner.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RandomSeed | int32 | The seed used for generating the randomness of the simulation. |  |
| TileSize | float | Length of the tile (in cm) along one axis. The total area of the tile will be TileSizeTileSize. |  |
| NumUniqueTiles | int32 | The number of unique tiles to generate. The final simulation is a procedurally determined combination of the various unique tiles. |  |
| MinimumQuadTreeSize | float | Minimum size of the quad tree used during the simulation. Reduce if too many instances are in splittable leaf quads (as warned in the log). |  |
| FoliageTypes | TArray < FFoliageTypeObject > | The types of foliage to procedurally spawn. |  |
| bNeedsSimulation | bool |  |  |

## Functions

### Simulate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NumSteps | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

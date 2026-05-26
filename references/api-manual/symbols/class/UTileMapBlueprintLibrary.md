# UTileMapBlueprintLibrary

- Symbol Type: class
- Symbol Path: Others / UTileMapBlueprintLibrary
- Source JSON Path: class/detail/Others/UTileMapBlueprintLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTileMapBlueprintLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

A collection of utility methods for working with tile map components
 
  @see UPaperTileMap, UPaperTileMapComponent

## Functions

### GetTileUserData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tile | FPaperTileInfo |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### GetTileTransform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tile | FPaperTileInfo |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### BreakTile

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tile | FPaperTileInfo  |  |  |
| TileIndex | int32 &  |  |  |
| TileSet | UPaperTileSet * &  |  |  |
| bFlipH | bool &  |  |  |
| bFlipV | bool &  |  |  |
| bFlipD | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeTile

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TileIndex | int32  |  |  |
| TileSet | UPaperTileSet *  |  |  |
| bFlipH | bool  |  |  |
| bFlipV | bool  |  |  |
| bFlipD | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPaperTileInfo  |  |  |

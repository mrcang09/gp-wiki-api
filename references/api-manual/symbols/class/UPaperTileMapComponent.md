# UPaperTileMapComponent

- Symbol Type: class
- Symbol Path: Others / UPaperTileMapComponent
- Source JSON Path: class/detail/Others/UPaperTileMapComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileMapComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

A component that handles rendering and collision for a single instance of a UPaperTileMap asset.
 
  This component is created when you drag a tile map asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  NOTE: This is an early access preview class.  While not considered production-ready, it is a step beyond
  'experimental' and is being provided as a preview of things to come:
   - We will try to provide forward-compatibility for content you create.
   - The classes may change significantly in the future.
   - The code is in an early state and may not meet the desired polish  quality bar.
   - There is probably no documentation or example content yet.
   - They will be promoted out of 'Early Access' when they are production ready.
 
  @see UPrimitiveComponent, UPaperTileMap

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MapWidth_DEPRECATED | int32 |  |  |
| MapHeight_DEPRECATED | int32 |  |  |
| TileWidth_DEPRECATED | int32 |  |  |
| TileHeight_DEPRECATED | int32 |  |  |
| DefaultLayerTileSet_DEPRECATED | UPaperTileSet * |  |  |
| Material_DEPRECATED | UMaterialInterface * |  |  |
| TileLayers_DEPRECATED | TArray < UPaperTileLayer * > |  |  |
| TileMapColor | FLinearColor |  |  |
| UseSingleLayerIndex | int32 |  |  |
| bUseSingleLayer | bool |  |  |
| TileMap | UPaperTileMap * |  |  |
| bShowPerTileGridWhenSelected | bool |  |  |
| bShowPerLayerGridWhenSelected | bool |  |  |
| bShowOutlineWhenUnselected | bool |  |  |

## Functions

### CreateNewTileMap

Creates a new tile map of the specified size, replacing the TileMap reference (or dropping the previous owned one)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MapWidth | int32  | Width of the map (in tiles) |  |
| MapHeight | int32  | Height of the map (in tiles) |  |
| TileWidth | int32  | Width of one tile (in pixels) |  |
| TileHeight | int32  | Height of one tile (in pixels) |  |
| PixelsPerUnrealUnit | float  |  |  |
| bCreateLayer | bool | Should an empty layer be created? |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OwnsTileMap

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetTileMap

Change the PaperTileMap used by this instance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTileMap | UPaperTileMap * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetMapSize

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MapWidth | int32 &  |  |  |
| MapHeight | int32 &  |  |  |
| NumLayers | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTile

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | int32  |  |  |
| Y | int32  |  |  |
| Layer | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPaperTileInfo  |  |  |

### SetTile

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | int32  |  |  |
| Y | int32  |  |  |
| Layer | int32  |  |  |
| NewValue | FPaperTileInfo |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResizeMap

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewWidthInTiles | int32  |  |  |
| NewHeightInTiles | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddNewLayer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPaperTileLayer * |  |  |

### GetTileMapColor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor |  |  |

### SetTileMapColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLayerColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Layer | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### SetLayerColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor  |  |  |
| Layer | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeTileMapEditable

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetTileCornerPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TileX | int32  |  |  |
| TileY | int32  |  |  |
| LayerIndex | int32  |  |  |
| bWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTileCenterPosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TileX | int32  |  |  |
| TileY | int32  |  |  |
| LayerIndex | int32  |  |  |
| bWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTilePolygon

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TileX | int32  |  |  |
| TileY | int32  |  |  |
| Points | TArray < FVector > &  |  |  |
| LayerIndex | int32  |  |  |
| bWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDefaultCollisionThickness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Thickness | float  |  |  |
| bRebuildCollision | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLayerCollision

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Layer | int32  |  |  |
| bHasCollision | bool  |  |  |
| bOverrideThickness | bool  |  |  |
| CustomThickness | float  |  |  |
| bOverrideOffset | bool  |  |  |
| CustomOffset | float  |  |  |
| bRebuildCollision | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RebuildCollision

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

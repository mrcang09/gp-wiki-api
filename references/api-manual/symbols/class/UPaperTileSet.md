# UPaperTileSet

- Symbol Type: class
- Symbol Path: Others / UPaperTileSet
- Source JSON Path: class/detail/Others/UPaperTileSet.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileSet.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

A tile set is a collection of tiles pulled from a texture that can be used to fill out a tile map.
 
  @see UPaperTileMap, UPaperTileMapComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TileSize | FIntPoint |  |  |
| TileSheet | UTexture2D * |  |  |
| AdditionalSourceTextures | TArray < UTexture * > |  |  |
| BorderMargin | FIntMargin |  |  |
| PerTileSpacing | FIntPoint |  |  |
| DrawingOffset | FIntPoint |  |  |
| WidthInTiles | int32 |  |  |
| HeightInTiles | int32 |  |  |
| AllocatedWidth | int32 |  |  |
| AllocatedHeight | int32 |  |  |
| PerTileData | TArray < FPaperTileMetadata > |  |  |
| Terrains | TArray < FPaperTileSetTerrain > |  |  |
| TileWidth_DEPRECATED | int32 |  |  |
| TileHeight_DEPRECATED | int32 |  |  |
| Margin_DEPRECATED | int32 |  |  |
| Spacing_DEPRECATED | int32 |  |  |
| BackgroundColor | FLinearColor | The background color displayed in the tile set viewer |  |

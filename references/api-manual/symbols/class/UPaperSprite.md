# UPaperSprite

- Symbol Type: class
- Symbol Path: Others / UPaperSprite
- Source JSON Path: class/detail/Others/UPaperSprite.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperSprite.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

Sprite Asset
 
  Stores the data necessary to render a single 2D sprite (from a region of a texture)
  Can also contain collision shapes for the sprite.
 
  @see UPaperSpriteComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceUV | FVector2D |  |  |
| SourceDimension | FVector2D |  |  |
| SourceTexture | UTexture2D * |  |  |
| BakedSourceUV | FVector2D |  |  |
| AdditionalSourceTextures | TArray < UTexture * > |  |  |
| BakedSourceDimension | FVector2D |  |  |
| BakedSourceTexture | UTexture2D * |  |  |
| DefaultMaterial | UMaterialInterface * |  |  |
| AlternateMaterial | UMaterialInterface * |  |  |
| Sockets | TArray < FPaperSpriteSocket > |  |  |
| SpriteCollisionDomain | TEnumAsByte < ESpriteCollisionMode :: Type > |  |  |
| PixelsPerUnrealUnit | float |  |  |
| BodySetup | UBodySetup * |  |  |
| AlternateMaterialSplitIndex | int32 |  |  |
| BakedRenderData | TArray < FVector4 > |  |  |
| OriginInSourceImageBeforeTrimming | FVector2D |  |  |
| SourceImageDimensionBeforeTrimming | FVector2D |  |  |
| bTrimmedInSourceImage | bool |  |  |
| bRotatedInSourceImage | bool |  |  |
| SourceTextureDimension | FVector2D |  |  |
| PivotMode | TEnumAsByte < ESpritePivotMode :: Type > |  |  |
| CustomPivotPoint | FVector2D |  |  |
| bSnapPivotToPixelGrid | bool |  |  |
| CollisionGeometry | FSpriteGeometryCollection |  |  |
| CollisionThickness | float |  |  |
| RenderGeometry | FSpriteGeometryCollection |  |  |
| AtlasGroup | UPaperSpriteAtlas * |  |  |

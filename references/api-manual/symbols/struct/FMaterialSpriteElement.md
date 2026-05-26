# FMaterialSpriteElement

- Symbol Type: struct
- Symbol Path: FMaterialSpriteElement
- Source JSON Path: cppstruct/detail/FMaterialSpriteElement.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialSpriteElement.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface * | The material that the sprite is rendered with. |  |
| DistanceToOpacityCurve | UCurveFloat * | A curve that maps distance on the X axis to the sprite opacity on the Y axis. |  |
| bSizeIsInScreenSpace | uint32 | Whether the size is defined in screen-space or world-space. |  |
| BaseSizeX | float | The base width of the sprite, multiplied with the DistanceToSizeCurve. |  |
| BaseSizeY | float | The base height of the sprite, multiplied with the DistanceToSizeCurve. |  |
| DistanceToSizeCurve | UCurveFloat * | A curve that maps distance on the X axis to the sprite size on the Y axis. |  |

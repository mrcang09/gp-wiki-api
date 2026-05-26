# FSlateBrush

- Symbol Type: struct
- Symbol Path: FSlateBrush
- Source JSON Path: cppstruct/detail/FSlateBrush.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSlateBrush.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Description

An brush which contains information about how to draw a Slate element

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ImageSize | FVector2D | Size of the resource in Slate Units |  |
| Margin | FMargin | The margin to use in Box and Border modes |  |
| TintColor | FSlateColor | Tinting applied to the image. |  |
| ResourceObject | UObject * | The image to render for this brush, can be a UTexture or UMaterialInterface or an object implementing <br>	  the AtlasedTextureInterface. |  |
| ResourceName | FName | The name of the rendering resource to use |  |
| UVRegion | FBox2D | Optional UV region for an image<br>	   When valid - overrides UV region specified in resource proxy |  |
| DrawAs | TEnumAsByte < enum ESlateBrushDrawType :: Type > | How to draw the image |  |
| Tiling | TEnumAsByte < enum ESlateBrushTileType :: Type > | How to tile the image in Image mode |  |
| Mirroring | TEnumAsByte < enum ESlateBrushMirrorType :: Type > | How to mirror the image in Image mode.  This is normally only used for dynamic image brushes where the source texture<br>	    comes from a hardware device such as a web camera. |  |
| ImageType | TEnumAsByte < enum ESlateBrushImageType :: Type > | The type of image |  |
| bUseImageSizeAsTextureSize | uint8 |  |  |
| bIsDynamicallyLoaded | uint8 | Whether or not the brush path is a path to a UObject |  |
| bHasUObject_DEPRECATED | uint8 | Whether or not the brush has a UTexture resource |  |
| Tint_DEPRECATED | FLinearColor | Tinting applied to the image. |  |

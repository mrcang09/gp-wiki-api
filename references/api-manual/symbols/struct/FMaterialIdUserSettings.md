# FMaterialIdUserSettings

- Symbol Type: struct
- Symbol Path: FMaterialIdUserSettings
- Source JSON Path: cppstruct/detail/FMaterialIdUserSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMaterialIdUserSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BiomesInfoObjectList | TArray < ULandscapeBiomesInfoObject * > | List of BiomesInfoObject used by this Landscape Actor |  |
| CustomWeightAllocations | TArray < FLandscapeCustomWeightAllocation > |  |  |
| HoleIndex | uint8 |  |  |
| NoiseTexture | UTexture2D * | Noise Texture applied when sample splatmap |  |
| bEditMatIDProperty | bool |  |  |
| LandscapeCorner | FVector2D |  |  |
| NoiseTiling | FVector2D |  |  |
| NoiseMultiplier | float | Larger the value is, larger the UVOffset will applied when sample splatmap |  |
| NoiseLerpPercentFromEdge | float | Starting percentage of lerp from Edge to center of the component, to avoid shifted UV go over the component. |  |
| DiffuseArrayInfo | FTextureArrayInfo | Diffuse texture array used as base color to render the landscape |  |
| NormalArrayInfo | FTextureArrayInfo | Normalmap texture array used as base color to render the landscape |  |
| LayerInfoToAllocInfoMap | TMap < ULandscapeLayerInfoObject * , FMaterialIdLayerAllocInfo > | Valid LayerInfoObject to MaterialIdAllocInfo map. |  |
| MaterialIdLayerCount | int32 | MaterialId Layer Count, fixed with 2, align SJZ |  |
| CustomWeightPaintingColor | FLinearColor |  |  |
| DummyLayerInfoRemap | TMap < FName , ULandscapeLayerInfoObject * > |  |  |
| CustomWeightConfig | UCustomWeightConfig * |  |  |
| FallbackLayerConfig | UMatIDFallbackConfig * |  |  |

# ULandscapeMaterialIdLayerInfoObject

- Symbol Type: class
- Symbol Path: Others / ULandscapeMaterialIdLayerInfoObject
- Source JSON Path: class/detail/Others/ULandscapeMaterialIdLayerInfoObject.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMaterialIdLayerInfoObject.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BiomesOwner | ULandscapeBiomesInfoObject * | Owner Biomes of this LayerInfoObject. Do not modify this Owner unless necessary. |  |
| DisplayName | FName |  |  |
| LayerIndex | int32 | Layer index of this layer info object, can be re-ordered. |  |
| DiffuseTexture | UTexture2D * | Diffuse Texture |  |
| NormalmapTexture | UTexture2D * | Normalmap Texture |  |
| TextureRotation | float | Rotation (in degree) applied when sampling diffusenormal texture |  |
| TextureTiling | FVector2D | Scaling applied when sampling diffusenormal texture |  |
| HeightBlendThresholdSoftness | float | ThresholdSoftness adjusts how sharp the edges of the height blend will be. The greater the value is, the softer the edge would be. |  |
| HeightContrast | float | HeightContrast adjust sampled height value's contrast. |  |
| DeltaForceHeightBlendSharpness | float |  |  |
| DisplacementLocalBias | float | Convert displacement from texture space to world space, unit is meter. |  |
| DisplacementIntensity | float | Scalar applied to displacement, applied after LocalBias is applied. |  |

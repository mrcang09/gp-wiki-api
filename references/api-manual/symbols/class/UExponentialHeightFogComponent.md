# UExponentialHeightFogComponent

- Symbol Type: class
- Symbol Path: Others / UExponentialHeightFogComponent
- Source JSON Path: class/detail/Others/UExponentialHeightFogComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UExponentialHeightFogComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FogDensity | float | Global density factor. |  |
| CustomHightFogDensity | TArray < FCustomHeightFog > |  |  |
| bUseCustomFog | bool |  |  |
| CustomFogLow_Height | float |  |  |
| CustomFogLow_DensityCoefficient | float |  |  |
| CustomFogLow_Color | FLinearColor |  |  |
| CustomFogHigh_Height | float |  |  |
| CustomFogHigh_DensityCoefficient | float |  |  |
| CustomFogHigh_Color | FLinearColor |  |  |
| FogInscatteringColor | FLinearColor |  |  |
| InscatteringColorCubemap | UTextureCube * | Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.<br>	  When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled. |  |
| InscatteringColorCubemapAngle | float | Angle to rotate the InscatteringColorCubemap around the Z axis. |  |
| InscatteringTextureTint | FLinearColor | Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap. |  |
| FullyDirectionalInscatteringColorDistance | float | Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color. |  |
| NonDirectionalInscatteringColorDistance | float | Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color. |  |
| DirectionalInscatteringExponent | float | Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.  <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |  |
| DirectionalInscatteringStartDistance | float | Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |  |
| DirectionalInscatteringColor | FLinearColor | Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |  |
| FogHeightFalloff | float | Height density factor, controls how the density increases as height decreases.  <br>	  Smaller values make the visible transition larger. |  |
| FogMaxOpacity | float | Maximum opacity of the fog.  <br>	  A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,<br>	  A value of 0 means the fog color will not be factored in at all. |  |
| StartDistance | float | Distance from the camera that the fog will start, in world units. |  |
| FogCutoffDistance | float | Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in. |  |
| Priority | int32 | Priority to be rendered with, useful if more than one exponential fogs are visible concurrently |  |
| bEnableVolumetricFog | bool | Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation. <br>	  Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.<br>	  Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior. |  |
| VolumetricFogScatteringDistribution | float | Controls the scattering phase function - how much incoming light scatters in various directions.<br>	  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.  <br>	  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0. |  |
| VolumetricFogAlbedo | FColor | The height fog particle reflectiveness used by volumetric fog. <br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |  |
| VolumetricFogEmissive | FLinearColor | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting, <br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |  |
| VolumetricFogExtinctionScale | float | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |  |
| VolumetricFogDistance | float | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |  |
| VolumetricFogStaticLightingScatteringIntensity | float |  |  |
| bOverrideLightColorsWithFogInscatteringColors | bool | Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color. <br>	  Make sure your directional light has 'Atmosphere Sun Light' enabled!<br>	  Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting. |  |
| VolumetricFogStartDistance | float | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |  |
| VolumetricFogNoiseTexture | UTexture2D * |  |  |
| VolumetricFogNoiseTransform | FTransform |  |  |

## Functions

### SetFogDensity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCustomFogHeight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCustomFogDensityCoefficient

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCustomFogInscatteringColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FLinearColor  |  |  |
| index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFogInscatteringColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInscatteringColorCubemap

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | UTextureCube * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInscatteringColorCubemapAngle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFullyDirectionalInscatteringColorDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNonDirectionalInscatteringColorDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInscatteringTextureTint

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDirectionalInscatteringExponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDirectionalInscatteringStartDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDirectionalInscatteringColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFogHeightFalloff

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFogMaxOpacity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStartDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFogCutoffDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFog

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogScatteringDistribution

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogExtinctionScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogAlbedo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | FColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogEmissive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogStartDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogNoiseTexture

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | UTexture2D * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumetricFogNoiseTransform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Transform | FTransform |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

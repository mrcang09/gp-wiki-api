# UAtmosphericFogComponent

- Symbol Type: class
- Symbol Path: Others / UAtmosphericFogComponent
- Source JSON Path: class/detail/Others/UAtmosphericFogComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericFogComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Used to create fogging effects such as clouds.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SunMultiplier | float | Global scattering factor. |  |
| FogMultiplier | float | Scattering factor on object. |  |
| DensityMultiplier | float | Fog density control factor. |  |
| DensityOffset | float | Fog density offset to control opacity [-1.f ~ 1.f]. |  |
| DistanceScale | float | Distance scale. |  |
| AltitudeScale | float | Altitude scale (only Z scale). |  |
| DistanceOffset | float | Distance offset, in km (to handle large distance) |  |
| GroundOffset | float | Ground offset. |  |
| StartDistance | float | Start Distance. |  |
| SunDiscScale | float | Distance offset, in km (to handle large distance) |  |
| DefaultBrightness | float | Default light brightness. Used when there is no sunlight placed in the level. Unit is lumens |  |
| DefaultLightColor | FColor | Default light color. Used when there is no sunlight placed in the level. |  |
| bDisableSunDisk | uint32 | Disable Sun Disk rendering. |  |
| bDisableGroundScattering | uint32 | Disable Color scattering from ground. |  |
| PrecomputeParams | FAtmospherePrecomputeParameters |  |  |
| TransmittanceTexture_DEPRECATED | UTexture2D * |  |  |
| IrradianceTexture_DEPRECATED | UTexture2D * |  |  |

## Functions

### SetDefaultBrightness

Set brightness of the light

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewBrightness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetDefaultLightColor

Set color of the light

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLightColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetSunMultiplier

Set SunMultiplier

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSunMultiplier | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetFogMultiplier

Set FogMultiplier

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFogMultiplier | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetDensityMultiplier

Set DensityMultiplier

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDensityMultiplier | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetDensityOffset

Set DensityOffset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDensityOffset | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetDistanceScale

Set DistanceScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDistanceScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetAltitudeScale

Set AltitudeScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAltitudeScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetStartDistance

Set StartDistance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewStartDistance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetDistanceOffset

Set DistanceOffset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDistanceOffset | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### DisableSunDisk

Set DisableSunDisk

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSunDisk | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### DisableGroundScattering

Set DisableGroundScattering

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewGroundScattering | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetPrecomputeParams

Set PrecomputeParams, only valid in Editor mode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DensityHeight | float  |  |  |
| MaxScatteringOrder | int32  |  |  |
| InscatterAltitudeSampleNum | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### StartPrecompute

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

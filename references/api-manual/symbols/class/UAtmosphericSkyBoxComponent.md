# UAtmosphericSkyBoxComponent

- Symbol Type: class
- Symbol Path: Others / UAtmosphericSkyBoxComponent
- Source JSON Path: class/detail/Others/UAtmosphericSkyBoxComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericSkyBoxComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RenderDynamicSky | bool |  |  |
| Material | UMaterialInterface * |  |  |
| NoiseTexture | UTexture2D * |  |  |
| StaticMesh | UStaticMesh * |  |  |
| RadiusScale | float |  |  |
| MeshRotation | FRotator |  |  |
| RainyDegree | float |  |  |
| Atmosphere | FTOD_AtmosphereParameters |  |  |
| Day | FTOD_DayParameters |  |  |
| Light | FTOD_LightParameters |  |  |
| CloudsPbr | FTOD_CloudPBRParameters |  |  |
| World | FTOD_WorldParameters |  |  |
| Cycle | FTOD_CycleParameters |  |  |
| TodTime | FTOD_Time |  |  |
| TodAnimation | FTOD_Animation |  |  |
| TodSunParams | FTOD_Sun |  |  |
| TodMoonParams | FTOD_Moon |  |  |
| TodSunAndMoonParams | FTOD_SunAndMoon |  |  |
| TodStarsParams | FTOD_Stars |  |  |
| TodSpecialSkyParams | FTOD_SpecialSky |  |  |
| SunActor | AActor * |  |  |
| MoonActor | AActor * |  |  |
| LightingChannels | FLightingChannels |  |  |
| MaterialInstancesDynamic | UMaterialInstanceDynamic * |  |  |
| bIsMaterialInstanceDirty | bool |  |  |
| FixedTimeOfDay | bool |  |  |
| FixedCurrTime | float |  |  |
| bNeedUpdate | bool |  |  |

## Functions

### SetFixedCurrTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| time | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFixedTimeOfDay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsFiexd | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNeedUpdate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NeedUpdate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetMaterialInstancesDynamic

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic * |  |  |

# UVolumetricFogSphereComponent

- Symbol Type: class
- Symbol Path: Others / UVolumetricFogSphereComponent
- Source JSON Path: class/detail/Others/UVolumetricFogSphereComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UVolumetricFogSphereComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

Used to create local volumetric fog.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VolumetricFogAlbedo | FColor | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |  |
| VolumetricFogEmissive | FLinearColor | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |  |
| VolumetricFogExtinctionScale | float | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |  |

## Functions

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

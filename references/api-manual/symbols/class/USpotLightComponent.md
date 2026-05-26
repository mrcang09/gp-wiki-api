# USpotLightComponent

- Symbol Type: class
- Symbol Path: Others / USpotLightComponent
- Source JSON Path: class/detail/Others/USpotLightComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USpotLightComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A spot light component emits a directional cone shaped light (Eg a Torch).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InnerConeAngle | float | Degrees. |  |
| OuterConeAngle | float | Degrees. |  |
| bCastPhotonShadow | uint32 | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |  |
| NearPlaneOffset | float |  |  |
| FarPlaneOffset | float |  |  |
| LightShaftConeAngle | float | Degrees. <br>	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=LightShaft, meta=(UIMin = "1.0", UIMax = "180.0")) |  |

## Functions

### SetInnerConeAngle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInnerConeAngle | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOuterConeAngle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewOuterConeAngle | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

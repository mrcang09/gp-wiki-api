# UWindDirectionalSourceComponent

- Symbol Type: class
- Symbol Path: Others / UWindDirectionalSourceComponent
- Source JSON Path: class/detail/Others/UWindDirectionalSourceComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWindDirectionalSourceComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

Component that provides a directional wind source. Only affects SpeedTree assets.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Strength | float |  |  |
| Speed | float |  |  |
| MinGustAmount | float |  |  |
| MaxGustAmount | float |  |  |
| Radius | float |  |  |
| bPointWind | uint32 |  |  |

## Functions

### SetStrength

Because the actual data used to query wind is stored on the render thread in
	  an instance of FWindSourceSceneProxy all of our properties are read only.
	  The data can be manipulated with the following functions which will queue 
	  a render thread update for this component
	 
	 Sets the strength of the generated wind

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewStrength | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSpeed

Sets the windspeed of the generated wind

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewSpeed | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMinimumGustAmount

Set minimum deviation for wind gusts

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewMinGust | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMaximumGustAmount

Set maximum deviation for wind gusts

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewMaxGust | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRadius

Set the effect radius for point wind

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewRadius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWindType

Set the type of wind generator to use

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewType | EWindSourceType |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# AAudioVolume

- Symbol Type: class
- Symbol Path: Others / AAudioVolume
- Source JSON Path: class/detail/Others/AAudioVolume.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AAudioVolume.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Priority | float | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  is chosen. The order is undefined if two or more overlapping volumes have the same priority. |  |
| bEnabled | uint32 | whether this volume is currently enabled and able to affect sounds |  |
| Settings | FReverbSettings | Reverb settings to use for this volume. |  |
| AmbientZoneSettings | FInteriorSettings | Interior settings used for this volume |  |

## Functions

### SetPriority

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPriority | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEnabled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReverbSettings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewReverbSettings | FReverbSettings & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInteriorSettings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInteriorSettings | FInteriorSettings & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRep_bEnabled

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

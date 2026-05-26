# UPawnSensingComponent

- Symbol Type: class
- Symbol Path: Others / UPawnSensingComponent
- Source JSON Path: class/detail/Others/UPawnSensingComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPawnSensingComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

SensingComponent encapsulates sensory (ie sight and hearing) settings and functionality for an Actor,
  allowing the actor to seehear Pawns in the world. It does nothing on network clients.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HearingThreshold | float | Max distance at which a makenoise(1.0) loudness sound can be heard, regardless of occlusion |  |
| LOSHearingThreshold | float | Max distance at which a makenoise(1.0) loudness sound can be heard if unoccluded (LOSHearingThreshold should be > HearingThreshold) |  |
| SightRadius | float | Maximum sight distance. |  |
| SensingInterval | float | Amount of time between pawn sensing updates. Use SetSensingInterval() to adjust this at runtime. A value <= 0 prevents any updates. |  |
| HearingMaxSoundAge | float |  |  |
| bEnableSensingUpdates | uint32 | If true, component will perform sensing updates. At runtime change this using SetSensingUpdatesEnabled(). |  |
| bOnlySensePlayers | uint32 | If true, will only sense player-controlled pawns in the world. Default: true |  |
| bSeePawns | uint32 | If true, we will perform visibility tests and will trigger notifications when a Pawn is visible. Default: true |  |
| bHearNoises | uint32 | If true, we will perform audibility tests and will be notified when a Pawn makes a noise that can be heard. Default: true<br>	  IMPORTANT NOTE: If we can see pawns (bSeePawns is true), and the pawn is visible, noise notifications are not triggered. |  |
| PeripheralVisionAngle | float | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. |  |
| PeripheralVisionCosine | float | Cosine of limits of peripheral vision. Computed from PeripheralVisionAngle. |  |

## Functions

### SetSensingInterval

Changes the SensingInterval.
	  If we are currently waiting for an interval, this can either extend or shorten that interval.
	  A value <= 0 prevents any updates.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSensingInterval | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSensingUpdatesEnabled

Enables or disables sensing updates. The timer is reset in either case.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPeripheralVisionAngle

Sets PeripheralVisionAngle. Calculates PeripheralVisionCosine from PeripheralVisionAngle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPeripheralVisionAngle | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPeripheralVisionAngle

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPeripheralVisionCosine

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

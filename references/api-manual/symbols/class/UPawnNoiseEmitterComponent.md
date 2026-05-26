# UPawnNoiseEmitterComponent

- Symbol Type: class
- Symbol Path: Others / UPawnNoiseEmitterComponent
- Source JSON Path: class/detail/Others/UPawnNoiseEmitterComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPawnNoiseEmitterComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

PawnNoiseEmitterComponent tracks noise event data used by SensingComponents to hear a Pawn.
  This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAIPerceptionSystemCompatibilityMode | uint32 |  |  |
| LastRemoteNoisePosition | FVector |  |  |
| NoiseLifetime | float |  |  |
| LastRemoteNoiseVolume | float |  |  |
| LastRemoteNoiseTime | float |  |  |
| LastLocalNoiseVolume | float |  |  |
| LastLocalNoiseTime | float |  |  |

## Functions

### MakeNoise

Cache noises instigated by the owning pawn for AI sensing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NoiseMaker | AActor *  | - is the actual actor which made the noise |  |
| Loudness | float  | - is the relative loudness of the noise (0.0 to 1.0) |  |
| NoiseLocation | FVector & | - is the position of the noise |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

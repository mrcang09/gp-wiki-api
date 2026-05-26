# FSimSpaceSettings

- Symbol Type: struct
- Symbol Path: FSimSpaceSettings
- Source JSON Path: cppstruct/detail/FSimSpaceSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSimSpaceSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Description

Settings for the system which passes motion of the simulation's space into the simulation. This allows the simulation to pass a 
  fraction of the world space motion onto the bodies which allows Bone-Space and Component-Space simulations to react to world-space 
  movement in a controllable way.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MasterAlpha | float |  |  |
| VelocityScaleZ | float |  |  |
| MaxLinearVelocity | float |  |  |
| MaxAngularVelocity | float |  |  |
| MaxLinearAcceleration | float |  |  |
| MaxAngularAcceleration | float |  |  |
| ExternalLinearDrag_DEPRECATED | float |  |  |
| ExternalLinearDragV | FVector |  |  |
| ExternalLinearVelocity | FVector |  |  |
| ExternalAngularVelocity | FVector |  |  |

# FWalkableSlopeOverride

- Symbol Type: struct
- Symbol Path: FWalkableSlopeOverride
- Source JSON Path: cppstruct/detail/FWalkableSlopeOverride.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FWalkableSlopeOverride.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

Struct allowing control over "walkable" normals, by allowing a restriction or relaxation of what steepness is normally walkable.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WalkableSlopeBehavior | TEnumAsByte < EWalkableSlopeBehavior > | Behavior of this surface (whether we affect the walkable slope).<br>	  @see GetWalkableSlopeBehavior(), SetWalkableSlopeBehavior() |  |
| WalkableSlopeAngle | float | Override walkable slope angle (in degrees), applying the rules of the Walkable Slope Behavior.<br>	  @see GetWalkableSlopeAngle(), SetWalkableSlopeAngle() |  |

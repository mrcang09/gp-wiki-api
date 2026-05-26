# URotatingMovementComponent

- Symbol Type: class
- Symbol Path: Others / URotatingMovementComponent
- Source JSON Path: class/detail/Others/URotatingMovementComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/URotatingMovementComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

Performs continuous rotation of a component at a specific rotation rate.
  Rotation can optionally be offset around a pivot point.
  Collision testing is not performed during movement.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RotationRate | FRotator | How fast to update rollpitchyaw of the component we update. |  |
| PivotTranslation | FVector | Translation of pivot point around which we rotate, relative to current rotation.<br>	  For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur<br>	  around the point +100 units along the local X axis from the center of the object,<br>	  rather than around the object's origin (the default). |  |
| bRotationInLocalSpace | uint32 | Whether rotation is applied in local or world space. |  |
| bCirculatingRotation | bool |  |  |
| RotationAngle | FRotator |  |  |
| OriginRotator | FRotator |  |  |
| bCircleFlag | bool |  |  |

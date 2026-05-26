# FConstraintDrive

- Symbol Type: struct
- Symbol Path: FConstraintDrive
- Source JSON Path: cppstruct/detail/FConstraintDrive.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintDrive.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stiffness | float | The spring strength of the drive. Force proportional to the position error. |  |
| Damping | float | The damping strength of the drive. Force proportional to the velocity error. |  |
| MaxForce | float | The force limit of the drive. |  |
| bEnablePositionDrive | uint8 | EnablesDisables position drive (orientation if using angular drive) |  |
| bEnableVelocityDrive | uint8 | EnablesDisables velocity drive (angular velocity if using angular drive) |  |

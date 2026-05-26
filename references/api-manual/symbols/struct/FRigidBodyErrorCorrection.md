# FRigidBodyErrorCorrection

- Symbol Type: struct
- Symbol Path: FRigidBodyErrorCorrection
- Source JSON Path: cppstruct/detail/FRigidBodyErrorCorrection.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRigidBodyErrorCorrection.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Rigid body error correction data

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LinearDeltaThresholdSq | float | max squared position difference to perform velocity adjustment |  |
| LinearInterpAlpha | float | strength of snapping to desired linear velocity |  |
| LinearRecipFixTime | float | inverted duration after which linear velocity adjustment will fix error |  |
| AngularDeltaThreshold | float | max squared angle difference (in radians) to perform velocity adjustment |  |
| AngularInterpAlpha | float | strength of snapping to desired angular velocity |  |
| AngularRecipFixTime | float | inverted duration after which angular velocity adjustment will fix error |  |
| BodySpeedThresholdSq | float | min squared body speed to perform velocity adjustment |  |

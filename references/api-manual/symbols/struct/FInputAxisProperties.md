# FInputAxisProperties

- Symbol Type: struct
- Symbol Path: FInputAxisProperties
- Source JSON Path: cppstruct/detail/FInputAxisProperties.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisProperties.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Configurable properties for control axes, used to transform raw input into game ready values.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeadZone | float | What the dead zone of the axis is.  For control axes such as analog sticks. |  |
| Sensitivity | float | Scaling factor to multiply raw value by. |  |
| Exponent | float | For applying curves to [0..1] axes, e.g. analog sticks |  |
| bInvert | uint8 | Inverts reported values for this axis |  |

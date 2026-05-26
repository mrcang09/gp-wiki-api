# FInputAxisKeyMapping

- Symbol Type: struct
- Symbol Path: FInputAxisKeyMapping
- Source JSON Path: cppstruct/detail/FInputAxisKeyMapping.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisKeyMapping.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Defines a mapping between an axis and key

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisName | FName | Friendly name of axis, e.g "MoveForward" |  |
| Key | FKey | Key to bind it to. |  |
| Scale | float | Multiplier to use for the mapping when accumulating the axis value |  |
| KeySeq | uint8 | key sequence number: 0 for Primary key, 1 for Backup key |  |

# FRBFParams

- Symbol Type: struct
- Symbol Path: FRBFParams
- Source JSON Path: cppstruct/detail/FRBFParams.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRBFParams.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Parameters used by RBF solver

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetDimensions | int32 | How many dimensions input data has |  |
| Radius | float | Default radius for each target, scaled by per-Target ScaleFactor |  |
| Function | ERBFFunctionType |  |  |
| DistanceMethod | ERBFDistanceMethod |  |  |
| TwistAxis | TEnumAsByte < EBoneAxis > | Axis to use when DistanceMethod is SwingAngle |  |
| WeightThreshold | float | Weight below which we shouldn't bother returning a contribution from a target |  |

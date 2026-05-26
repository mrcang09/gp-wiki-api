# FEmitterDynamicParameter

- Symbol Type: struct
- Symbol Path: FEmitterDynamicParameter
- Source JSON Path: cppstruct/detail/FEmitterDynamicParameter.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FEmitterDynamicParameter.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

Helper structure for displaying the parameter.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParamName | FName | The parameter name - from the material DynamicParameter expression. READ-ONLY |  |
| bUseEmitterTime | uint32 | If true, use the EmitterTime to retrieve the value, otherwise use Particle RelativeTime. |  |
| bSpawnTimeOnly | uint32 | If true, only set the value at spawn time of the particle, otherwise update each frame. |  |
| ValueMethod | TEnumAsByte < enum EEmitterDynamicParameterValue > | Where to get the parameter value from. |  |
| bScaleVelocityByParamValue | uint32 | If true, scale the velocity value selected in ValueMethod by the evaluated ParamValue. |  |
| ParamValue | FRawDistributionFloat | The distriubtion for the parameter value. |  |

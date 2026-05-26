# FTimeStretchCurve

- Symbol Type: struct
- Symbol Path: FTimeStretchCurve
- Source JSON Path: cppstruct/detail/FTimeStretchCurve.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTimeStretchCurve.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

We have Sum(SamplingTimeStep) = T_Original = N  SamplingTimeStep
		dTO = dT_i  U  (1 + S  C_i)
		PR_i = U  (1 + S  C_i)
		dTO = dT_i  PR_i
		T_Target = T_Original  PR
		dTO_i = dT_i  U
		dTO_i = dT_i  U  (1 + S  C_i)
		dTO_i = dT_i  U  (1 + C_i)
		Sum(dTO_i) = Sum(dT_i  U  (1 + C_i))
		Sum(dTO_i) = Sum(dT_i)  U + Sum(dT_i  U  S  C_i))
		T_Original = T_Target  U + U  S  Sum(dT_i  C_i)
		S = (T_Original - T_Target  U)  (U  Sum(dT_i  C_i))
		S = (T_Original - T_Target  U)  (U  dT  Sum(C_i))
		Within these bounds, we can approximate dT_i, and also Sum(dT_i  C_i) by linear interpolation.
		dT_Original = dT_Target  U  (1 + S  C_i)
		We see that montage position = playback time  play rate.
		PR_i = U  (1.f + S  C_i).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SamplingRate | float |  |  |
| CurveValueMinPrecision | float |  |  |
| Markers | TArray < FTimeStretchCurveMarker > | Optimized list of markers. |  |
| Sum_dT_i_by_C_i | float | Cached Sum(dT_i  C_i) |  |

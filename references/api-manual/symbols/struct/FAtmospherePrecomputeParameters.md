# FAtmospherePrecomputeParameters

- Symbol Type: struct
- Symbol Path: FAtmospherePrecomputeParameters
- Source JSON Path: cppstruct/detail/FAtmospherePrecomputeParameters.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAtmospherePrecomputeParameters.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Structure storing Data for pre-computation

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DensityHeight | float | Rayleigh scattering density height scale, ranges from [0...1] |  |
| DecayHeight_DEPRECATED | float |  |  |
| MaxScatteringOrder | int32 | Maximum scattering order |  |
| TransmittanceTexWidth | int32 | Transmittance Texture Width |  |
| TransmittanceTexHeight | int32 | Transmittance Texture Height |  |
| IrradianceTexWidth | int32 | Irradiance Texture Width |  |
| IrradianceTexHeight | int32 | Irradiance Texture Height |  |
| InscatterAltitudeSampleNum | int32 | Number of different altitudes at which to sample inscatter color (size of 3D texture Z dimension) |  |
| InscatterMuNum | int32 | Inscatter Texture Height |  |
| InscatterMuSNum | int32 | Inscatter Texture Width |  |
| InscatterNuNum | int32 | Inscatter Texture Width |  |

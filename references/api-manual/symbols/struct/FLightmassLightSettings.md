# FLightmassLightSettings

- Symbol Type: struct
- Symbol Path: FLightmassLightSettings
- Source JSON Path: cppstruct/detail/FLightmassLightSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassLightSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

Per-light settings for Lightmass

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IndirectLightingSaturation | float | 0 will be completely desaturated, 1 will be unchanged |  |
| ShadowExponent | float | Controls the falloff of shadow penumbras |  |
| bUseAreaShadowsForStationaryLight | bool | Whether to use area shadows for stationary light precomputed shadowmaps.<br>	  Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp. |  |

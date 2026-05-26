# FIdeaBakingPrimitiveSettings

- Symbol Type: struct
- Symbol Path: FIdeaBakingPrimitiveSettings
- Source JSON Path: cppstruct/detail/FIdeaBakingPrimitiveSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FIdeaBakingPrimitiveSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IdeaMaterialDiffuse | float | When baking, use this diffuse calculate reflection fro sun related lighting, not use really material's diffuse texture |  |
| LightmapBoost | float | Scales the lightmap result of idea baking. |  |
| SunIntensity | float | By luciuszhang:<br>	 Control the sun intensity from the sky, unit is cdm^2, default value is 1.0. |  |
| DiscardPixelFrontfaceFactor | float | When ray intersected surface frontface counter lower DiscardPixelFrontfaceFactor  NumRays, the pixel will be discard. Larger value will help decrease black edge artifact.<br>	 But if scene has two side surface(like flags), will cause another artifact, pixels behind back side of flags maybe discarded wrong. |  |
| LocalLightsAffectMaxDistance | float | By luciuszhang:<br>	 Control the sun indirect intensity from the sky, unit is cdm^2, default value is 1.0. |  |

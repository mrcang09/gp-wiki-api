# FDepthFieldGlowInfo

- Symbol Type: struct
- Symbol Path: FDepthFieldGlowInfo
- Source JSON Path: cppstruct/detail/FDepthFieldGlowInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FDepthFieldGlowInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

info for glow when using depth field rendering

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableGlow | uint32 | whether to turn on the outline glow (depth field fonts only) |  |
| GlowColor | FLinearColor | base color to use for the glow |  |
| GlowOuterRadius | FVector2D | if bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y |  |
| GlowInnerRadius | FVector2D | if bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y |  |

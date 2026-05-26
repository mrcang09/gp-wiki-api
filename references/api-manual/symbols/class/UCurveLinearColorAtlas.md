# UCurveLinearColorAtlas

- Symbol Type: class
- Symbol Path: Others / UCurveLinearColorAtlas
- Source JSON Path: class/detail/Others/UCurveLinearColorAtlas.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCurveLinearColorAtlas.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

Manages gradient LUT textures for registered actors and assigns them to the corresponding materials on the actor

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TextureSize | uint32 |  |  |
| bSquareResolution | uint32 | Set texture height equal to texture width. |  |
| TextureHeight | uint32 |  |  |
| GradientCurves | TArray < UCurveLinearColor * > |  |  |
| bIsDirty | uint32 |  |  |
| bDisableAllAdjustments | uint32 | Disable all color adjustments to preserve negative values in curves. Color adjustments clamp to 0 when enabled. |  |
| bHasCachedColorAdjustments | uint32 |  |  |
| CachedColorAdjustments | FCurveAtlasColorAdjustments |  |  |

## Functions

### GetCurvePosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCurve | UCurveLinearColor *  |  |  |
| Position | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

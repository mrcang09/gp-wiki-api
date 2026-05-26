# UPixelProjectedReflectionComponent

- Symbol Type: class
- Symbol Path: Others / UPixelProjectedReflectionComponent
- Source JSON Path: class/detail/Others/UPixelProjectedReflectionComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPixelProjectedReflectionComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

UPixelProjectedReflectionComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PreviewBox | UBoxComponent * |  |  |
| NormalDistortionStrength | float | Controls the strength of normals when distorting the planar reflection. |  |
| SkyDistanceFadeoutStart | float | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |  |
| SkyDistanceFadeoutEnd | float | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |  |
| DistanceFromPlaneFadeStart_DEPRECATED | float |  |  |
| DistanceFromPlaneFadeEnd_DEPRECATED | float |  |  |
| DistanceFromPlaneFadeoutStart | float | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |  |
| DistanceFromPlaneFadeoutEnd | float | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |  |
| AngleFromPlaneFadeStart | float | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |  |
| AngleFromPlaneFadeEnd | float | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |  |
| HeightAdjustmentVolumes | TArray < APixelProjectedReflectionHeightAdjustmentVolume * > |  |  |
| VisibilityVolumes | TArray < APixelProjectedReflectionVisibilityVolume * > |  |  |

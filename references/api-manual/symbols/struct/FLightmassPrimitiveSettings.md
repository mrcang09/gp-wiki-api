# FLightmassPrimitiveSettings

- Symbol Type: struct
- Symbol Path: FLightmassPrimitiveSettings
- Source JSON Path: cppstruct/detail/FLightmassPrimitiveSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLightmassPrimitiveSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Description

Per-object settings for Lightmass

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseTwoSidedLighting | uint32 | If true, this object will be lit as if it receives light from both sides of its polygons. |  |
| bUseEmissiveForStaticLighting | uint32 | If true, allow using the emissive for static lighting. |  |
| EmissiveLightExplicitInfluenceRadius | float | Direct lighting influence radius.<br>	  The default is 0, which means the influence radius should be automatically generated based on the emissive light brightness.<br>	  Values greater than 0 override the automatic method. |  |
| bUseVertexNormalForHemisphereGather | uint32 | Typically the triangle normal is used for hemisphere gathering which prevents incorrect self-shadowing from artist-tweaked vertex normals.<br>	  However in the case of foliage whose vertex normal has been setup to match the underlying terrain, gathering in the direction of the vertex normal is desired. |  |
| EmissiveLightFalloffExponent | float | Direct lighting falloff exponent for mesh area lights created from emissive areas on this primitive. |  |
| bShadowIndirectOnly | uint32 | If true, this object will only shadow indirect lighting. |  |
| EmissiveBoost | float | Scales the emissive contribution of all materials applied to this object. |  |
| DiffuseBoost | float | Scales the diffuse contribution of all materials applied to this object. |  |
| FullyOccludedSamplesFraction | float | Fraction of samples taken that must be occluded in order to reach full occlusion. |  |

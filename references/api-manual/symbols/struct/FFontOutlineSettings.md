# FFontOutlineSettings

- Symbol Type: struct
- Symbol Path: FFontOutlineSettings
- Source JSON Path: cppstruct/detail/FFontOutlineSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FFontOutlineSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Settings for applying an outline to a font

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutlineSize | int32 | Size of the outline in slate units (at 1.0 font scale this unit is a pixel) |  |
| OutlineMaterial | UObject * | Optional material to apply to the outline |  |
| OutlineColor | FLinearColor | The color of the outline for any character in this font |  |
| bSeparateFillAlpha | bool | If checked, the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value<br>	  The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area |  |

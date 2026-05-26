# FStreamingTexturePrimitiveInfo

- Symbol Type: struct
- Symbol Path: FStreamingTexturePrimitiveInfo
- Source JSON Path: cppstruct/detail/FStreamingTexturePrimitiveInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FStreamingTexturePrimitiveInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:48Z

---

## Description

Information about a streaming texture that a primitive uses for rendering.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Texture | UTexture2D * |  |  |
| Bounds | FBoxSphereBounds | The streaming bounds of the texture, usually the component material bounds. <br>	  Usually only valid for registered component, as component bounds are only updated when the components are registered.<br>	  otherwise only PackedRelativeBox can be used.Irrelevant when the component is not registered, as the component could be moved by ULevel::ApplyWorldOffset()<br>	  In that case, only PackedRelativeBox is meaningful. |  |
| TexelFactor | float |  |  |
| PackedRelativeBox | uint32 | When non zero, this represents the relative box used to compute Bounds, using the component bounds as reference.<br>	  If available, this allows the texture streamer to generate the level streaming data before the level gets visible.<br>	  At that point, the component are not yet registered, and the bounds are unknown, but the precompiled build data is still available.<br>	  Also allows to update the relative bounds after a level get moved around from ApplyWorldOffset. |  |

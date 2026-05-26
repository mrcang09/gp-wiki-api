# UTextureRenderTargetCube

- Symbol Type: class
- Symbol Path: Others / UTextureRenderTargetCube
- Source JSON Path: class/detail/Others/UTextureRenderTargetCube.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTargetCube.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

TextureRenderTargetCube
 
  Cube render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular cube texture resource.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SizeX | int32 | The width of the texture. |  |
| ClearColor | FLinearColor | the color the texture is cleared to |  |
| OverrideFormat | TEnumAsByte < enum EPixelFormat > | The format of the texture data.											<br>	 Normally the format is derived from bHDR, this allows code to set the format explicitly. |  |
| bHDR | uint32 | Whether to support storing HDR values, which requires more memory. |  |
| bForceLinearGamma | uint32 | True to force linear gamma space for this render target |  |

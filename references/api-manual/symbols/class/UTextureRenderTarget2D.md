# UTextureRenderTarget2D

- Symbol Type: class
- Symbol Path: Others / UTextureRenderTarget2D
- Source JSON Path: class/detail/Others/UTextureRenderTarget2D.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTarget2D.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

TextureRenderTarget2D
 
  2D render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular 2D texture resource.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SizeX | int32 | The width of the texture. |  |
| SizeY | int32 | The height of the texture. |  |
| ClearColor | FLinearColor | the color the texture is cleared to |  |
| AddressX | TEnumAsByte < enum TextureAddress > | The addressing mode to use for the X axis. |  |
| AddressY | TEnumAsByte < enum TextureAddress > | The addressing mode to use for the Y axis. |  |
| bForceLinearGamma | uint32 | True to force linear gamma space for this render target |  |
| bHDR_DEPRECATED | uint32 | Whether to support storing HDR values, which requires more memory. |  |
| RenderTargetFormat | TEnumAsByte < enum ETextureRenderTargetFormat > | Format of the texture render target. <br>	  Data written to the render target will be quantized to this format, which can limit the range and precision.<br>	  The largest format (RTF_RGBA32f) uses 16x more memory and bandwidth than the smallest (RTF_R8) and can greatly affect performance.  <br>	  Use the smallest format that has enough precision and range for what you are doing. |  |
| bGPUSharedFlag | uint32 | Whether to support GPU sharing of the underlying native texture resource. |  |
| bAutoGenerateMips | uint32 | Whether to support Mip maps for this render target texture |  |
| OverrideFormat | TEnumAsByte < enum EPixelFormat > | Normally the format is derived from RenderTargetFormat, this allows code to set the format explicitly. |  |

# UCompositionGraphCaptureSettings

- Symbol Type: class
- Symbol Path: Others / UCompositionGraphCaptureSettings
- Source JSON Path: class/detail/Others/UCompositionGraphCaptureSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCompositionGraphCaptureSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IncludeRenderPasses | FCompositionGraphCapturePasses | A list of render passes to include in the capture. Leave empty to export all available passes. |  |
| bCaptureFramesInHDR | bool | Whether to capture the frames as HDR textures (.exr format) |  |
| HDRCompressionQuality | int32 | Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow) |  |
| CaptureGamut | TEnumAsByte < enum EHDRCaptureGamut > | The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled. |  |
| PostProcessingMaterial | FSoftObjectPath | Custom post processing material to use for rendering |  |

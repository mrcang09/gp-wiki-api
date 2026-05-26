# FLayerBlendInput

- Symbol Type: struct
- Symbol Path: FLayerBlendInput
- Source JSON Path: cppstruct/detail/FLayerBlendInput.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FLayerBlendInput.json
- Mirrored At (UTC): 2026-05-19 08:24:42Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LayerName | FName |  |  |
| BlendType | TEnumAsByte < ELandscapeLayerBlendType > |  |  |
| LayerInput | FExpressionInput |  |  |
| HeightInput | FExpressionInput |  |  |
| PreviewWeight | float |  |  |
| ConstLayerInput | FVector | only used if LayerInput is not hooked up |  |
| ConstHeightInput | float | only used if HeightInput is not hooked up |  |

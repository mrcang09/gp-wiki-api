# UMaterialExpressionSceneDepthWithoutWater

- Symbol Type: class
- Symbol Path: Others / UMaterialExpressionSceneDepthWithoutWater
- Source JSON Path: class/detail/Others/UMaterialExpressionSceneDepthWithoutWater.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepthWithoutWater.json
- Mirrored At (UTC): 2026-05-19 08:23:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputMode | TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type > | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |  |
| Input | FExpressionInput | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or<br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |  |
| ConstInput | FVector2D | only used if Input is not hooked up |  |
| FallbackDepth | float | Depth to fall back to in case the needed texture isn't available on a particular platform or configuration |  |

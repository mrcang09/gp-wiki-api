# UMaterialExpressionSceneDepth

- Symbol Type: class
- Symbol Path: Others / UMaterialExpressionSceneDepth
- Source JSON Path: class/detail/Others/UMaterialExpressionSceneDepth.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepth.json
- Mirrored At (UTC): 2026-05-19 08:23:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputMode | TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type > | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |  |
| Input | FExpressionInput | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or <br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |  |
| Coordinates_DEPRECATED | FExpressionInput |  |  |
| ConstInput | FVector2D | only used if Input is not hooked up |  |

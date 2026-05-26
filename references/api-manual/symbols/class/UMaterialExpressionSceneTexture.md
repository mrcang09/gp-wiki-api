# UMaterialExpressionSceneTexture

- Symbol Type: class
- Symbol Path: Others / UMaterialExpressionSceneTexture
- Source JSON Path: class/detail/Others/UMaterialExpressionSceneTexture.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneTexture.json
- Mirrored At (UTC): 2026-05-19 08:23:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Coordinates | FExpressionInput | UV in 0..1 range |  |
| SceneTextureId | TEnumAsByte < ESceneTextureId > | Which scene texture (screen aligned texture) we want to make a lookup into |  |
| bClampUVs | bool | Clamps texture coordinates to the range 0 to 1. Incurs a performance cost. |  |
| bFiltered | bool | Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions), some SceneTextures cannot be filtered |  |

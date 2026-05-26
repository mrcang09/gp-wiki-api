# ALandscape

- Symbol Type: class
- Symbol Path: Others / ALandscape
- Source JSON Path: class/detail/Others/ALandscape.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ALandscape.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialIdUserSettings | FMaterialIdUserSettings |  |  |
| UseFarLandNormalDistance | float |  |  |
| BlendFarLandNormalDistance | float |  |  |
| FarLandVertexColorThreshold | float |  |  |
| FarLandVertexColorBlendThreshold | float |  |  |
| bUseLandscapeDeform | bool |  |  |
| bCanUseMaterialIdShading | bool |  |  |
| CurrentBiomesIndex | int32 | Current selected biomes info |  |
| bTextureArrayDirty | bool |  |  |
| PaintingCustomWeightLayerIndex | int32 |  |  |
| MatIdLayerVisibility | TArray < bool > |  |  |
| FarLandDiffuseTexture | UTexture2D * |  |  |
| FarLandNormalTexture | UTexture2D * |  |  |
| FarLandInfoDebug | TMap < ULandscapeComponent * , FFarLandInfo > |  |  |
| ExportSplatmapTexture | UTexture2D * |  |  |
| Platform | EMyLandscapePlatfromConfiguration |  |  |
| PCConfig | FMyLandscapeConfigurationParams |  |  |
| MobileConfig | FMyLandscapeConfigurationParams |  |  |

## Functions

### EnumerateLandscapePaintMatIDLayers

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Landscape | ALandscapeProxy * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | LANDSCAPE_API TArray < FName >  |  |  |

### IsMaterialIDLandscape

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Landscape | ALandscapeProxy * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | LANDSCAPE_API bool  |  |  |

### SetLandscapeCorner

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | LANDSCAPE_API void |  |  |

### SplitFarLandTextureForComponent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetFarLandTextureInfo

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GenerateSplatmapMip

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | LANDSCAPE_API void |  |  |

### ExportWeightAsSplatmapMipEditor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | LANDSCAPE_API void |  |  |

### BuildLandscapeStaticMesh

UFUNCTION(CallInEditor, Category = "Build Static Mesh", meta = (CallInEditor = "true"))

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

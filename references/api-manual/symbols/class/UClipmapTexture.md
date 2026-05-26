# UClipmapTexture

- Symbol Type: class
- Symbol Path: Others / UClipmapTexture
- Source JSON Path: class/detail/Others/UClipmapTexture.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UClipmapTexture.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

Runtime virtual texture UObject

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bSkipOneMip | bool |  |  |
| DisFirstMip | float |  |  |
| bUsePointSample | bool |  |  |
| bUseBorder | bool |  |  |
| TileSize | int32 |  |  |
| FirstMipImageSize | int32 |  |  |
| NumTile | int32 |  |  |
| bUseCompressType | bool |  |  |
| NormalSetting | FClipmapSetting |  |  |
| CompressSetting | TMap < FString , FClipmapSetting > |  |  |
| bsRGB | bool |  |  |
| FileDDCPath | FString |  |  |
| ClipmapInfos | FClipmapInfos |  |  |
| CompressInfos | TMap < FString , FClipmapInfos > |  |  |
| DebugName | FString |  |  |
| HashNum | uint32 |  |  |
| Owner | UClipmapTextureComponent * |  |  |
| OriginTexture | UTexture2D * |  |  |
| TargetTexture | TSoftObjectPtr < UTexture2D > |  |  |

## Functions

### CreateClipmapTargetTexture

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

# UClipmapTextureComponent

- Symbol Type: class
- Symbol Path: Others / UClipmapTextureComponent
- Source JSON Path: class/detail/Others/UClipmapTextureComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UClipmapTextureComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

Component used to place a URuntimeVirtualTexture in the world.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClipmapTexture | UClipmapTexture * |  |  |
| bUseForCDLODMatID | bool |  |  |
| BoundsSourceActor | AActor * | Actor to copy the bounds from to set up the transform. |  |
| MipToDis | TMap < int32 , float > |  |  |
| ClipmapInfo | FVector4 |  |  |

## Functions

### SetTransformToBounds

Set this component transform to include the BoundsSourceActor bounds. Called by our UI details customization.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RefreshClipmapInfo

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

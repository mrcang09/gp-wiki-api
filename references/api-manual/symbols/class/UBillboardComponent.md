# UBillboardComponent

- Symbol Type: class
- Symbol Path: Others / UBillboardComponent
- Source JSON Path: class/detail/Others/UBillboardComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBillboardComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

A 2d texture that will be rendered always facing the camera.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sprite | UTexture2D * |  |  |
| bIsScreenSizeScaled | uint32 |  |  |
| ScreenSize | float |  |  |
| U | float |  |  |
| UL | float |  |  |
| V | float |  |  |
| VL | float |  |  |
| SpriteCategoryName_DEPRECATED | FName | Sprite category that the component belongs to. Value serves as a key into the localization file. |  |
| SpriteInfo | FSpriteCategoryInfo | Sprite category information regarding the component |  |
| bUseInEditorScaling | bool | Whether to use in-editor arrow scaling (i.e. to be affected by the global arrow scale) |  |

## Functions

### SetSprite

Change the sprite texture used by this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSprite | UTexture2D * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUV

Change the sprite's UVs

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewU | int32  |  |  |
| NewUL | int32  |  |  |
| NewV | int32  |  |  |
| NewVL | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSpriteAndUV

Change the sprite texture and the UV's used by this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSprite | UTexture2D *  |  |  |
| NewU | int32  |  |  |
| NewUL | int32  |  |  |
| NewV | int32  |  |  |
| NewVL | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UMediaTexture

- Symbol Type: class
- Symbol Path: Others / UMediaTexture
- Source JSON Path: class/detail/Others/UMediaTexture.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMediaTexture.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AddressX | TEnumAsByte < TextureAddress > | The addressing mode to use for the X axis. |  |
| AddressY | TEnumAsByte < TextureAddress > | The addressing mode to use for the Y axis. |  |
| AutoClear | bool | Whether to clear the texture when no media is being played (default = enabled). |  |
| ClearColor | FLinearColor | The color used to clear the texture if AutoClear is enabled (default = black). |  |
| MediaPlayer | UMediaPlayer * | The media player asset associated with this texture. |  |

## Functions

### GetAspectRatio

Gets the current aspect ratio of the texture.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | Texture aspect ratio. |  |

### GetHeight

Gets the current height of the texture.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | Texture height (in pixels). |  |

### GetWidth

Gets the current width of the texture.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | Texture width (in pixels). |  |

### ResetFirstFrame

Reset The IsFirstFrameRender&IsFirstFrameNotify to false for iOS

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

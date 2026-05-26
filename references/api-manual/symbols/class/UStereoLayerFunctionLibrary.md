# UStereoLayerFunctionLibrary

- Symbol Type: class
- Symbol Path: Others / UStereoLayerFunctionLibrary
- Source JSON Path: class/detail/Others/UStereoLayerFunctionLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UStereoLayerFunctionLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

StereoLayer Extensions Function Library

## Functions

### SetSplashScreen

Set splash screen attributes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Texture | UTexture *  |  (in) A texture to be used for the splash. B8R8G8A8 format. |  |
| Scale | FVector2D  |  (in) Scale of the texture. |  |
| Offset | FVector2D  |  (in) Position from which to start rendering the texture. |  |
| bShowLoadingMovie | bool  |  |  |
| bShowOnSet | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ShowSplashScreen

Show the splash screen and override the VR display

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### HideSplashScreen

Hide the splash screen and return to normal display.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EnableAutoLoadingSplashScreen

Enablesdisables splash screen to be automatically shown when LoadMap is called.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAutoShowEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

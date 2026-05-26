# UCineCameraComponent

- Symbol Type: class
- Symbol Path: Others / UCineCameraComponent
- Source JSON Path: class/detail/Others/UCineCameraComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCineCameraComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A specialized version of a camera component, geared toward cinematic usage.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FilmbackSettings | FCameraFilmbackSettings | Controls the filmback of the camera. |  |
| LensSettings | FCameraLensSettings | Controls the camera's lens. |  |
| FocusSettings | FCameraFocusSettings | Controls the camera's focus. |  |
| CurrentFocalLength | float | Current focal length of the camera (i.e. controls FoV, zoom) |  |
| CurrentAperture | float | Current aperture, in terms of f-stop (e.g. 2.8 for f2.8) |  |
| CurrentFocusDistance | float | Read-only. Control this value via FocusSettings. |  |
| FilmbackPresets | TArray < FNamedFilmbackPreset > | List of available filmback presets |  |
| LensPresets | TArray < FNamedLensPreset > | List of available lens presets |  |
| DefaultFilmbackPresetName | FString | Name of the default filmback preset |  |
| DefaultLensPresetName | FString | Name of the default lens preset |  |
| DefaultLensFocalLength | float | Default focal length (will be constrained by default lens) |  |
| DefaultLensFStop | float | Default aperture (will be constrained by default lens) |  |

## Functions

### GetHorizontalFieldOfView

Returns the horizonal FOV of the camera with current settings.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetVerticalFieldOfView

Returns the vertical FOV of the camera with current settings.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetFilmbackPresetName

Returns the filmback name of the camera with the current settings.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### SetFilmbackPresetByName

Set the current preset settings by preset name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPresetName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLensPresetName

Returns the lens name of the camera with the current settings.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### SetLensPresetByName

Set the current lens settings by preset name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPresetName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

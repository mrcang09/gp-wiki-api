# UMediaSource

- Symbol Type: class
- Symbol Path: Others / UMediaSource
- Source JSON Path: class/detail/Others/UMediaSource.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMediaSource.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Abstract base class for media sources.
 
  Media sources describe the location andor settings of media objects that can
  be played in a media player, such as a video file on disk, a video stream on
  the internet, or a web cam attached to or built into the target device. The
  location is encoded as a media URL string, whose URI scheme and optional file
  extension will be used to locate a suitable media player.

## Functions

### GetUrl

Get the media source's URL string (must be implemented in child classes).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The media URL. |  |

### Validate

Validate the media source settings (must be implemented in child classes).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if validation passed, false otherwise. |  |

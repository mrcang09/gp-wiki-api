# UFileMediaSource

- Symbol Type: class
- Symbol Path: Others / UFileMediaSource
- Source JSON Path: class/detail/Others/UFileMediaSource.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UFileMediaSource.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FilePath | FString | The path to the media file to be played.<br>	 <br>	  @see SetFilePath |  |
| PrecacheFile | bool | Load entire media file into memory and play from there (if possible). |  |

## Functions

### SetFilePath

Set the path to the media file that this source represents.
	 
	  Automatically converts full paths to media sources that reside in the
	  Engine's or project's ContentMovies directory into relative paths.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Path | FString & | The path to set. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

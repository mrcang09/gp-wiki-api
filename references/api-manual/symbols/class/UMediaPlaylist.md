# UMediaPlaylist

- Symbol Type: class
- Symbol Path: Others / UMediaPlaylist
- Source JSON Path: class/detail/Others/UMediaPlaylist.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMediaPlaylist.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Implements a media play list.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Loop | uint32 | Whether the play list should loop (default = true). |  |
| Items | TArray < UMediaSource * > | List of media sources to play. |  |

## Functions

### Add

Add a media source to the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MediaSource | UMediaSource * | The media source to append. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the media source was added, false otherwise. |  |

### AddFile

Add a media file path to the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FilePath | FString & | The file path to add. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the file was added, false otherwise. |  |

### AddUrl

Add a media URL to the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Url | FString & | The URL to add. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the URL was added, false otherwise. |  |

### Get

Get the media source at the specified index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 | The index of the media source to get. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMediaSource *  | The media source, or nullptr if the index doesn't exist. |  |

### GetNext

Get the next media source in the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOutIndex | int32 & | Index of the current media source (will contain the new index). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMediaSource *  | The media source after the current one, or nullptr if the list is empty. |  |

### GetPrevious

Get the previous media source in the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOutIndex | int32 & | Index of the current media source (will contain the new index). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMediaSource *  | The media source before the current one, or nullptr if the list is empty. |  |

### GetRandom

Get a random media source in the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutIndex | int32 & | Will contain the index of the returned media source. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMediaSource *  | The random media source, or nullptr if the list is empty. |  |

### Insert

Insert a media source into the play list at the given position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MediaSource | UMediaSource *  | The media source to insert. |  |
| Index | int32 | The index to insert into. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Num

Get the number of media sources in the play list.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | Number of media sources. |  |

### Remove

Remove all occurrences of the given media source in the play list.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MediaSource | UMediaSource * | The media source to remove. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the media source was removed, false otherwise. |  |

### RemoveAt

Remove the media source at the specified position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 | The index of the media source to remove. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the media source was removed, false otherwise. |  |

### Replace

Replace the media source at the specified position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32  | The index of the media source to replace. |  |
| Replacement | UMediaSource * | The replacement media source. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the media source was replaced, false otherwise. |  |

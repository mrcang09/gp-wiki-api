# UPaperFlipbookComponent

- Symbol Type: class
- Symbol Path: Others / UPaperFlipbookComponent
- Source JSON Path: class/detail/Others/UPaperFlipbookComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbookComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceFlipbook | UPaperFlipbook * | Flipbook currently being played |  |
| Material_DEPRECATED | UMaterialInterface * |  |  |
| PlayRate | float | Current play rate of the flipbook |  |
| bLooping | uint32 | Whether the flipbook should loop when it reaches the end, or stop |  |
| bReversePlayback | uint32 | If playback should move the current position backwards instead of forwards |  |
| bPlaying | uint32 | Are we currently playing (moving Position) |  |
| AccumulatedTime | float | Current position in the timeline |  |
| CachedFrameIndex | int32 | Last frame index calculated |  |
| SpriteColor | FLinearColor | Vertex color to apply to the frames |  |
| CachedBodySetup | UBodySetup * | The cached body setup |  |

## Functions

### SetFlipbook

Change the flipbook used by this instance (will reset the play time to 0 if it is a new flipbook).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFlipbook | UPaperFlipbook * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetFlipbook

Gets the flipbook used by this instance.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPaperFlipbook * |  |  |

### SetSpriteColor

Set color of the sprite

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Play

Start playback of flipbook

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PlayFromStart

Start playback of flipbook from the start

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Reverse

Start playback of flipbook in reverse

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReverseFromEnd

Start playback of flipbook in reverse from the end

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Stop

Stop playback of flipbook

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsPlaying

Get whether this flipbook is playing or not.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsReversing

Get whether we are reversing or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetPlaybackPositionInFrames

Jump to a position in the flipbook (expressed in frames). If bFireEvents is true, event functions will fire, otherwise they will not.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFramePosition | int32  |  |  |
| bFireEvents | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlaybackPositionInFrames

Get the current playback position (in frames) of the flipbook

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetPlaybackPosition

Jump to a position in the flipbook (expressed in seconds). If bFireEvents is true, event functions will fire, otherwise they will not.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPosition | float  |  |  |
| bFireEvents | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlaybackPosition

Get the current playback position (in seconds) of the flipbook

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetLooping

true means we should loop, false means we should not.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewLooping | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsLooping

Get whether we are looping or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetPlayRate

Sets the new play rate for this flipbook

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlayRate

Get the current play rate for this flipbook

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetNewTime

Set the new playback position time to use

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFlipbookLength

Get length of the flipbook (in seconds)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetFlipbookLengthInFrames

Get length of the flipbook (in frames)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetFlipbookFramerate

Get the nominal framerate that the flipbook will be played back at (ignoring PlayRate), in frames per second

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### OnRep_SourceFlipbook

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldFlipbook | UPaperFlipbook * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UTimelineComponent

- Symbol Type: class
- Symbol Path: Others / UTimelineComponent
- Source JSON Path: class/detail/Others/UTimelineComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTimelineComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
  Events can be triggered at keyframes along the timeline. 
  Floats, vectors, and colors are interpolated between keyframes along the timeline.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TheTimeline | FTimeline | The actual timeline structure |  |
| bIgnoreTimeDilation | uint32 | True if global time dilation should be ignored by this timeline, false otherwise. |  |

## Functions

### Play

Start playback of timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void |  |  |

### PlayFromStart

Start playback of timeline from the start

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void |  |  |

### Reverse

Start playback of timeline in reverse

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void |  |  |

### ReverseFromEnd

Start playback of timeline in reverse from the end

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void |  |  |

### Stop

Stop playback of timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void |  |  |

### IsPlaying

Get whether this timeline is playing or not.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### IsReversing

Get whether we are reversing or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### SetPlaybackPosition

Jump to a position in the timeline.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPosition | float  |  |  |
| bFireEvents | bool  | If true, event functions that are between current position and new playback position will fire. |  |
| bFireUpdate | bool | If true, the update output exec will fire after setting the new playback position. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetPlaybackPosition

Get the current playback position of the Timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API float |  |  |

### SetLooping

true means we would loop, false means we should not.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewLooping | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### IsLooping

Get whether we are looping or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### SetPlayRate

Sets the new play rate for this timeline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetPlayRate

Get the current play rate for this timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API float |  |  |

### SetNewTime

Set the new playback position time to use

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetTimelineLength

Get length of the timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API float |  |  |

### SetTimelineLength

Set length of the timeline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLength | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetTimelineLengthMode

Sets the length mode of the timeline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLengthMode | ETimelineLengthMode |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetIgnoreTimeDilation

Set whether to ignore time dilation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewIgnoreTimeDilation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetIgnoreTimeDilation

Get whether to ignore time dilation.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API bool |  |  |

### SetFloatCurve

Update a certain float track's curve

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFloatCurve | UCurveFloat *  |  |  |
| FloatTrackName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetVectorCurve

Update a certain vector track's curve

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewVectorCurve | UCurveVector *  |  |  |
| VectorTrackName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetLinearColorCurve

Update a certain linear color track's curve

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLinearColorCurve | UCurveLinearColor *  |  |  |
| LinearColorTrackName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### OnRep_Timeline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

# UMovieSceneSequencePlayer

- Symbol Type: class
- Symbol Path: Others / UMovieSceneSequencePlayer
- Source JSON Path: class/detail/Others/UMovieSceneSequencePlayer.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequencePlayer.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Abstract class that provides consistent player behaviour for various animation players

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Status | TEnumAsByte < EMovieScenePlayerStatus :: Type > | Movie player status. |  |
| bReversePlayback | uint32 | Whether we're currently playing in reverse. |  |
| bPendingFirstUpdate | uint32 | True where we're waiting for the first update of the sequence after calling StartPlayingNextTick. |  |
| Sequence | UMovieSceneSequence * | The sequence to play back |  |
| TimeCursorPosition | float | The current time cursor position within the sequence (in seconds) |  |
| StartTime | float | Time time at which to start playing the sequence (defaults to the lower bound of the sequence's play range) |  |
| EndTime | float | Time time at which to end playing the sequence (defaults to the upper bound of the sequence's play range) |  |
| CurrentNumLoops | int32 | The number of times we have looped in the current playback |  |
| PlaybackSettings | FMovieSceneSequencePlaybackSettings | Specific playback settings for the animation. |  |
| RootTemplateInstance | FMovieSceneRootEvaluationTemplateInstance | The root template instance we're evaluating |  |

## Functions

### Play

Start playback forwards from the current time cursor position, using the current play rate.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PlayReverse

Reverse playback.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ChangePlaybackDirection

Changes the direction of playback (go in reverse if it was going forward, or vice versa)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PlayLooping

Start playback from the current time cursor position, looping the specified number of times.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NumLoops | int32 | - The number of loops to play. -1 indicates infinite looping. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StartPlayingNextTick

Start playback from the current time cursor position, using the current play rate. Does not update the animation until next tick.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Pause

Pause playback.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Scrub

Scrub playback.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Stop

Stop playback.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GoToEndAndStop

Go to end and stop.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetPlaybackPosition

Get the current playback position

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetPlaybackPosition

Set the current playback position

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlaybackPosition | float | - The new playback position to set. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlaybackPostionWithloop

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTargetTimePostionWithloop

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### JumpToPosition

Jump to new playback position

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlaybackPosition | float | - The new playback position to set. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### JumpToPositionEx

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlaybackPosition | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsPlaying

Check whether the sequence is actively playing.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsPaused

Check whether the sequence is paused.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetLength

Get the playback length of the sequence

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPlayRate

Get the playback rate of this player.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### IsEvaluating

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetPlayRate

Set the playback rate of this player. Negative values will play the animation in reverse.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayRate | float | - The new rate of playback for the animation. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlayLoopCount

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NumLoops | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlaybackRange

Sets the range in time to be played back by this player, overriding the default range stored in the asset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewStartTime | float  | The new starting time for playback |  |
| NewEndTime | float | The new ending time for playback. Must be larger than the start time. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPlaybackStart

Get the offset within the level sequence to start playing

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPlaybackStartSeconds

Get the offset seconds within the level sequence to start playing

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPlaybackEnd

Get the offset within the level sequence to finish playing

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPlaybackEndSeconds

Get the offset seconds within the level sequence to finish playing

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetBoundObjects

Retrieve all objects currently bound to the specified binding identifier

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectBinding | FMovieSceneObjectBindingID |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UObject * >  |  |  |

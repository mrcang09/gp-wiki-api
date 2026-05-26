# ULevelSequencePlayer

- Symbol Type: class
- Symbol Path: Others / ULevelSequencePlayer
- Source JSON Path: class/detail/Others/ULevelSequencePlayer.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequencePlayer.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

ULevelSequencePlayer is used to actually "play" an level sequence asset at runtime.
 
  This class keeps track of playback state and provides functions for manipulating
  an level sequence while its playing.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AdditionalEventReceivers | TArray < UObject * > | Array of additional event receivers |  |

## Functions

### CreateLevelSequencePlayer

Create a new level sequence player.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | Context object from which to retrieve a UWorld. |  |
| LevelSequence | ULevelSequence *  | The level sequence to play. |  |
| Settings | FMovieSceneSequencePlaybackSettings  | The desired playback settings |  |
| OutActor | ALevelSequenceActor * & | The level sequence actor created to play this sequence. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULevelSequencePlayer *  |  |  |

### GetEventReceivers

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UObject * > |  |  |

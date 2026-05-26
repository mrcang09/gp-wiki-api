# ALevelSequenceActor

- Symbol Type: class
- Symbol Path: Others / ALevelSequenceActor
- Source JSON Path: class/detail/Others/ALevelSequenceActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ALevelSequenceActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

Actor responsible for controlling a specific level sequence in the world.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAutoPlay | bool |  |  |
| PlaybackSettings | FMovieSceneSequencePlaybackSettings |  |  |
| SequencePlayer | ULevelSequencePlayer * |  |  |
| LevelSequence | FSoftObjectPath |  |  |
| TempLevelSequence | ULevelSequence * |  |  |
| AdditionalEventReceivers | TArray < AActor * > |  |  |
| BurnInOptions | ULevelSequenceBurnInOptions * |  |  |
| BindingOverrides | UMovieSceneBindingOverrides * | Mapping of actors to override the sequence bindings with |  |
| bReduceFrequency | bool |  |  |
| ReduceFrameCount | int32 |  |  |
| IgnoreFrameTolerance | float |  |  |
| bOverrideInstanceData | uint8 | Enable specification of dynamic instance data to be supplied to the sequence during playback |  |
| DefaultInstanceData | UObject * | Instance data that can be used to dynamically control sequence evaluation at runtime |  |
| BurnInInstance | ULevelSequenceBurnIn * | Burn-in widget |  |
| OwnCharacter | AActor * | 所属玩家, feishen, 20210623 |  |

## Functions

### GetSequence

Get the level sequence being played by this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bLoad | bool  | Whether to load the sequence object if it is not already in memory. |  |
| bInitializePlayer | bool | Whether to initialize the player when the sequence has been loaded. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULevelSequence *  | Level sequence, or nullptr if not assigned or if it cannot be loaded. |  |

### SetSequence

Set the level sequence being played by this actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSequence | ULevelSequence * | The sequence object to set. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEventReceivers

Set an array of additional actors that will receive events triggerd from this sequence actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AdditionalReceivers | TArray < AActor * > | An array of actors to receive events |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBinding

Overrides the specified binding with the specified actors, optionally still allowing the bindings defined in the Level Sequence asset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Binding | FMovieSceneObjectBindingID  |  |  |
| Actors | TArray < AActor * > &  |  |  |
| bAllowBindingsFromAsset | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddBinding

Adds the specified actor to the overridden bindings for the specified binding ID, optionally still allowing the bindings defined in the Level Sequence asset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Binding | FMovieSceneObjectBindingID  |  |  |
| Actor | AActor *  |  |  |
| bAllowBindingsFromAsset | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveBinding

Removes the specified actor from the specified binding's actor array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Binding | FMovieSceneObjectBindingID  |  |  |
| Actor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetBinding

Resets the specified binding back to the defaults defined by the Level Sequence asset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Binding | FMovieSceneObjectBindingID |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetBindings

Resets all overridden bindings back to the defaults defined by the Level Sequence asset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UGCAddBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| TrackName | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FMovieSceneObjectBindingID  |  |  |

### UGCRemoveBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| TrackName | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FMovieSceneObjectBindingID  |  |  |

### ReceiveInitailizePlayer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetOwnCharacter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

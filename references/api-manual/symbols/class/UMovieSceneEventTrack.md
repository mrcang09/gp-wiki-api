# UMovieSceneEventTrack

- Symbol Type: class
- Symbol Path: Others / UMovieSceneEventTrack
- Source JSON Path: class/detail/Others/UMovieSceneEventTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventTrack.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Implements a movie scene track that triggers discrete events during playback.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bFireEventsWhenForwards | uint32 | If events should be fired when passed playing the sequence forwards. |  |
| bFireEventsWhenBackwards | uint32 | If events should be fired when passed playing the sequence backwards. |  |
| EventPosition | EFireEventsAtPosition | Defines where in the evaluation to trigger events |  |
| EventReceivers | TArray < FMovieSceneObjectBindingID > | Defines a list of object bindings on which to trigger the events in this track. When empty, events will trigger in the default event contexts for the playback environment (such as the level blueprint, or widget). |  |
| Sections | TArray < UMovieSceneSection * > | The track's sections. |  |

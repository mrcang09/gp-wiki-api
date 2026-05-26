# UInterpTrackEvent

- Symbol Type: class
- Symbol Path: Others / UInterpTrackEvent
- Source JSON Path: class/detail/Others/UInterpTrackEvent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackEvent.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EventTrack | TArray < struct FEventTrackKey > | Array of events to fire off. |  |
| bFireEventsWhenForwards | uint32 | If events should be fired when passed playing the sequence forwards. |  |
| bFireEventsWhenBackwards | uint32 | If events should be fired when passed playing the sequence backwards. |  |
| bFireEventsWhenJumpingForwards | uint32 | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |  |
| bUseCustomEventName | uint32 | If checked each key's event name is the exact name of the custom event function in level script that will be called |  |

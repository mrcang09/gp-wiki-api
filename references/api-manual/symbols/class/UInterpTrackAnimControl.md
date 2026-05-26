# UInterpTrackAnimControl

- Symbol Type: class
- Symbol Path: Others / UInterpTrackAnimControl
- Source JSON Path: class/detail/Others/UInterpTrackAnimControl.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackAnimControl.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FName | Name of slot to use when playing animation. Passed to Actor. <br>	 	When multiple tracks use the same slot name, they are each given a different ChannelIndex when SetAnimPosition is called. |  |
| AnimSeqs | TArray < struct FAnimControlTrackKey > | Track of different animations to play and when to start playing them. |  |
| bSkipAnimNotifiers | uint32 | Skip all anim notifiers |  |

# UAnimSequenceBase

- Symbol Type: class
- Symbol Path: Others / UAnimSequenceBase
- Source JSON Path: class/detail/Others/UAnimSequenceBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimSequenceBase.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Notifies | TArray < FAnimNotifyEvent > | Animation notifies, sorted by time (earliest notification first). |  |
| SequenceLength | float | Length (in seconds) of this AnimSequence if played back with a speed of 1.0. |  |
| RateScale | float | Number for tweaking playback rate of this animation globally. |  |
| bEnableExcludeNotifiesWhenPlayAsMontage | bool |  |  |
| RawCurveData | FRawCurveTracks | Raw uncompressed float curve data |  |

## Functions

### GetPlayLength

Returns the total play length of the montage, if played back with a speed of 1.0.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API virtual float |  |  |

# ULevelSequenceBurnIn

- Symbol Type: class
- Symbol Path: Others / ULevelSequenceBurnIn
- Source JSON Path: class/detail/Others/ULevelSequenceBurnIn.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequenceBurnIn.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

Base class for level sequence burn ins

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FrameInformation | FLevelSequencePlayerSnapshot | Snapshot of frame information. |  |
| LevelSequenceActor | ALevelSequenceActor * | The actor to get our burn in frames from |  |

## Functions

### SetSettings

Called when this burn in is receiving its settings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSettings | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSettingsClass

Get the settings class to use for this burn in

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSubclassOf < ULevelSequenceBurnInInitSettings > |  |  |

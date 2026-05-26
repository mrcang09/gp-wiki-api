# UPlayerInput

- Symbol Type: class
- Symbol Path: Others / UPlayerInput
- Source JSON Path: class/detail/Others/UPlayerInput.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPlayerInput.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

end: 单条记录，滑屏轨迹中的一个点 

  Object within PlayerController that processes player input.
  Only exists on the client in network games.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableKeyInput | bool |  |  |
| InputTouchCacheDataList | TArray < FInputTouchCacheData > |  |  |
| DebugExecBindings | TArray < struct FKeyBind > | Generic bindings of keys to Exec()-compatible strings for development purposes only |  |
| InvertedAxis | TArray < FName > | List of Axis Mappings that have been inverted |  |

## Functions

### SetMouseSensitivity

Exec function to change the mouse sensitivity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sensitivity | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBind

Exec function to add a debug exec command

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BindName | FName  |  |  |
| Command | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InvertAxisKey

Exec function to invert an axis key

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisKey | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InvertAxis

Exec function to invert an axis mapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearSmoothing

Exec function to reset mouse smoothing values

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

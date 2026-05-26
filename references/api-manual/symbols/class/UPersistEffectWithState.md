# UPersistEffectWithState

- Symbol Type: class
- Symbol Path: Others / UPersistEffectWithState
- Source JSON Path: class/detail/Others/UPersistEffectWithState.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectWithState.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

实现了状态机的PersistEffect，是PersistEffectSkill的基类

## Functions

### GetCurrentStateName

获取当前状态的名字
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName |  |  |

### GetCurrentStateTime

获取状态的运行时间
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### JumpToState

获取跳转到指定状态
	  生效范围: 服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateName | FName  | 跳转的目标状态名 |  |
| EnterTime | float  | 跳转到目标状态的时间 |  |
| bPause | bool | 是否暂停sequence播放 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

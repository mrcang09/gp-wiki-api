# AActivityBaseActor

- Symbol Type: class
- Symbol Path: Others / AActivityBaseActor
- Source JSON Path: class/detail/Others/AActivityBaseActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AActivityBaseActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

可实现可交互物基础功能的Actor

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OnActivityActorChangeState | FActivityChangeState | 状态变化事件委托<br>	 @param LeaveState 离开的状态 名<br>	 @param EnterState 进入的状态名 |  |

## Functions

### GetCurrentStateName

生效范围：SC
	  获取当前状态名

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName | 当前状态名 |  |

### GetCurrentStateTime

生效范围：SC
	  获取进入当前状态后所经过的时间

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | 当前状态经过的时间 |  |

### JumpToState

生效范围：S
	  跳转到指定状态

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateName | FName  | 要跳转的状态名 |  |
| EnterTime | float  | 进入状态的时间 |  |
| bPause | bool | 是否暂停 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Pause

生效范围：S
	  暂停当前状态的sequence的播放

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Resume

生效范围：S
	  恢复当前状态的sequence的播放

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CheckCurrentStateIsEntry

生效范围：SC
	  检查当前状态是否为状态机的入口状态

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否为入口状态 |  |

### GetCurrentSequnceIsEnd

生效范围：SC
	  检查当前sequence是否播放完毕

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否播放完毕 |  |

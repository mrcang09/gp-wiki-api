# UGCPlayerStateSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 角色系统 / UGCPlayerStateSystem
- Source JSON Path: class/detail/和平全局接口/角色系统/UGCPlayerStateSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPlayerStateSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

玩家数据/状态系统接口库

## Functions

### IsAlive

是否存活
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### IsExit

是否离开游戏（主动退出，非断线）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetUGCVIPLevel

获取 VIP Level
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetPlayerAccountInfo

获取玩家的账号数据
生效范围：服务器 & 客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPlayerAccountInfo |  |  |

### GetPlayerBattleInfo

获取玩家的战斗数据
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPlayerBattleInfo |  |  |

### SavePlayerArchiveData

保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）!!!!注意，不能在对局结算之后保存存档数据，在对局结算后调用此接口无法成功保存存档数据
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UID | number | 玩家 UID |  |
| ArchiveData | table | 存档数据 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetPlayerArchiveData

获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UID | number | 玩家 UID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table | 存档数据 |  |

### ClearPlayerArchiveData

清理玩家存档数据（GM 指令，仅开发环境生效）
生效范围：客户端

### GetPlayerPlatformGender

获取玩家账号性别
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlatformGender | number | 从DS获取的玩家性别 |  |
| UID | number | 玩家UID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 玩家账号性别，0 - 隐藏，1 - 男，2 - 女 |  |

### GetTeamID

获取 TeamID
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetPlayerKeyInt64

获取 64 位玩家 PlayerKey
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerState | PlayerState |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetPlayerKey

获取字符串玩家 PlayerKey
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerState | PlayerState |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string |  |  |

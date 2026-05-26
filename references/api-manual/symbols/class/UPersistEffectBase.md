# UPersistEffectBase

- Symbol Type: class
- Symbol Path: Others / UPersistEffectBase
- Source JSON Path: class/detail/Others/UPersistEffectBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBase.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

PersistEffectBase, PersistEffectSkill和PersistEffectBuff的基类

## Functions

### HasAuthority

检查当前对象是否运行在服务器端
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 否运行在服务器端 |  |

### IsAutonomous

检查当前对象是否运行在主控客户端
	  生效范围: 服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bConsiderObReplay | bool | 是否包含观战和回放时的主控端 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const bool  | 否运行在主控客户端 |  |

### RefreshValidTime

刷新PersistEffect的生效时间
	  生效范围: 服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetTickEnable

设置PersistEffect是否每帧执行Tick函数，在服务器调用只会开启服务器的Tick，在客户端调用只会开启客户端的Tick
	  生效范围: 服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetApplyTime

设置PersistEffect的生效时间
	  生效范围: 服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetApplyTime

获取PersistEffect的生效时间
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetTimeStamp

获取当前服务器时间戳
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### HasTag

检查当前技能或Buff是否有某个类型的Tag
	  生效范围SC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | FGameplayTag | 要检查的Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 是否有对应的Tag |  |

### GetRemainingTime

获取剩余时间

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | 剩余时间 |  |

### GetOwnerActor

获取PersistEffect所属的Actor
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### GetOwnerComponent

获取PersistEffect所属的组件
	  生效范围: 服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPersistBaseComponent * |  |  |

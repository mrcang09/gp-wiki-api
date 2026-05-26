# UGCPawnSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 角色系统 / UGCPawnSystem
- Source JSON Path: class/detail/和平全局接口/角色系统/UGCPawnSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPawnSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

角色系统接口库（废弃，已迁移到 UGCPlayerPawnSystem）

## Functions

### HasPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
是否在指定状态下
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PawnState | EPawnState | 角色状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### AllowPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
是否允许进入指定状态
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PawnState | EPawnState | 角色状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SwitchPoseState

【废弃】已迁移到 UGCPlayerPawnSystem
切换 Pose 状态
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PoseState | ESTEPoseState | 角色状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### EnterPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
进入指定状态
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PawnState | EPawnState | 角色状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### LeavePawnState

【废弃】已迁移到 UGCPlayerPawnSystem
离开指定状态
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PawnState | EPawnState | 角色状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### DisabledPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
禁用指定状态
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| PawnState | EPawnState | 角色状态 |  |
| IsDisabled | bool | 是否禁用 |  |

### GetIsFPP

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第一人称视角
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是不是 FPP 模式 |  |

### SetIsFPP

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第一人称视角
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| IsFPP | bool | 是否第一人称 |  |
| bForce | bool | 强制设置人称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 设置是否成功 |  |

### GetIsTPP

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第三人称视角
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否第三人称 |  |

### SetIsTPP

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第三人称视角
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| IsTPP | bool | 是否第三人称 |  |
| bForce | bool | 强制设置 TPP 模式 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 设置是否成功 |  |

### GetIsInvincible

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否无敌
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否无敌 |  |

### SetIsInvincible

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否无敌
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| IsInvincible | bool | 是否无敌 |  |

### TryEnterParachuteState

【废弃】已迁移到 UGCPlayerPawnSystem
尝试进入跳伞状态
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| CheckPawnState | EPawnState[] | 不允许进入跳伞的角色状态 |  |
| CanOpenParachuteHeight | float | 允许开伞高度 |  |
| ForceOpenParachuteHeight | float | 强制开伞高度 |  |
| CloseParachuteHeight | float | 关伞高度 |  |
| bParachuteAvatarNotShown | bool | 是否不显示伞包 |  |

### ExitParachuteState

【废弃】已迁移到 UGCPlayerPawnSystem
退出跳伞状态
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

### HideBoneByBoneName

【废弃】已迁移到 UGCPlayerPawnSystem
根据玩家角色的骨骼名称修改骨骼的显隐性
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| BoneName | FName | 骨骼名称 |  |
| bHide | bool | true隐藏，false显示 |  |

### ChangeAvatarMesh

【废弃】已迁移到 UGCPlayerPawnSystem
切换玩家角色使用的全身骨骼体
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| SkeletalMeshPath | string | 全身骨骼体路径 |  |

### RecoverAvatarMesh

【废弃】已迁移到 UGCPlayerPawnSystem
恢复玩家角色使用的全身骨骼体
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

### SkipSpawnDeadTombBox

【废弃】已迁移到 UGCPlayerPawnSystem
玩家死亡取消生成盒子
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| bIsSkip | bool | 玩家是否取消生成死亡盒子 |  |

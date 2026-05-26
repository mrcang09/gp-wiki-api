# UGCLevelFlowSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 场景与环境 / UGCLevelFlowSystem
- Source JSON Path: class/detail/和平全局接口/场景与环境/UGCLevelFlowSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9C%BA%E6%99%AF%E4%B8%8E%E7%8E%AF%E5%A2%83/UGCLevelFlowSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

关卡流程系统接口库

## Functions

### EnableLevelFlow

启用关卡流程
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMgrPath | string | 需要注册的 GameModeActorMgr 的路径 |  |

### GoToNextLevelForAllPlayers

当前关卡所有玩家直接跳转到下个关卡，需所有玩家都已达到通关条件
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 所有玩家跳转到下个关卡是否成功 |  |

### GoToNextLevelForOnePlayer

单个玩家直接跳转到下个关卡，需当前玩家已达到通关条件，当前队伍其他玩家仍停留在当前关卡
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | ASTExtraPlayerController | 玩家 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 当前玩家跳转到下个关卡是否成功 |  |

### LevelAddScore

给指定队伍关卡加分
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TeamID | number | 队伍 ID |  |
| Score | number | 加分的分数 |  |

### LevelSettle

队伍所在关卡立即结算
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TeamID | number | 结算的队伍 |  |
| IsFinish | boolean | 是否通关 |  |

### GetCurrentLevelStage

获取当前玩家处于第几关
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | ASTExtraPlayerController | 玩家 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 当前玩家处于第几关 |  |

### GetTotalLevelCount

获取总关卡数，随机切换关卡暂时不支持获取总关卡数，需要自定义逻辑
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 总关卡数 |  |

### GameAddScore

给指定队伍游戏加分
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TeamID | number | 队伍 ID |  |
| Score | number | 加分的分数 |  |

### GameSettle

游戏立即结算
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsFinish | boolean | 是否通关 |  |

### GetAllPlayerControllerInCurrentLevel

获取关卡里的所有玩家
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController[] | 玩家列表 |  |

### GetCurrentLevelActor

获取当前副本
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCLevelActor | 关卡Actor |  |

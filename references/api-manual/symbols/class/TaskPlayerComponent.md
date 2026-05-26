# TaskPlayerComponent

- Symbol Type: class
- Symbol Path: 和平全局接口 / 商业化与功能模板 / TaskPlayerComponent
- Source JSON Path: class/detail/和平全局接口/商业化与功能模板/TaskPlayerComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/TaskPlayerComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

UGC任务系统玩家组件

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskPlayerComponent.OnTaskLineAwardInfoChangeDelegate |  | 生效范围：客户端<br>任务线奖励状态变更回调<br>@param TaskLineName string @任务线名称<br>@param Index number @奖励索引 |  |
| TaskPlayerComponent.OnTaskInfoChangeDelegate |  | 生效范围：客户端<br>任务数据变更回调<br>@param Index UGCTaskIndex @榜单周期 |  |
| TaskPlayerComponent.OnTaskLineProgressChangeDelegate |  | 生效范围：客户端&服务端<br>任务线进度变更回调<br>@param TaskLineName string @任务线名称 |  |

## Functions

### ResetPercentTaskLine

重置活跃任务线
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

### ClaimLevelTaskAward

领取成长任务奖励
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| LevelIndex | number |  |  |
| TaskIndex | number |  |  |

### ClaimPercentTaskAward

领取活跃任务奖励
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| TaskIndex | number |  |  |

### GetTaskLineProgress

获取任务线进度
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetLevelTaskInfoList

获取成长任务线的任务信息列表
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FUGCLevelTaskPlayerData[] |  |  |

### GetPercentTaskInfoList

获取活跃任务线的任务信息列表
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FUGCTaskInfo[] |  |  |

### GetPercentTaskLineAwardStateList

获取活跃任务线的奖励状态列表
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### GetTaskLineAwardState

获取任务线奖励状态
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| Index | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EUGCTaskLineAwardState |  |  |

### ClaimAllAward

领取任务线的全部奖励
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |

### ClaimTaskLineAward

领取任务线奖励
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| Index | number |  |  |

### SetTaskLineProgress

设置任务线进度
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| Progress | number |  |  |

### GetPercentTaskProgress

获取活跃任务进度
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| Index | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetPercentTaskState

获取活跃任务状态
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| Index | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EUGCTaskState |  |  |

### GetLevelTaskProgress

获取成长任务进度
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| LevelIndex | number |  |  |
| TaskIndex | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetLevelTaskState

获取成长任务状态
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| LevelIndex | number |  |  |
| TaskIndex | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EUGCTaskState |  |  |

### GetTaskManager

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TaskManager |  |  |

### SetTaskLineTime

设置任务线和任务线下所有任务的开始/结束时间
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskLineName | string |  |  |
| BeginTime | number |  |  |
| EndTime | number |  |  |

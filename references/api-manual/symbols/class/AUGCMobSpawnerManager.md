# AUGCMobSpawnerManager

- Symbol Type: class
- Symbol Path: 和平全局接口 / 怪物系统 / AUGCMobSpawnerManager
- Source JSON Path: class/detail/和平全局接口/怪物系统/AUGCMobSpawnerManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/AUGCMobSpawnerManager.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

刷怪系统：刷怪管理器

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartCondition | EUGCMobSpawnerManagerStartCondition | 配置刷怪管理器的启动方式 |  |
| EventName | FString | 启动方式使用事件触发时，监听的GMP名 |  |
| MaxSpawnPerFrame | int32 | 配置刷怪管理器每帧刷怪的上限 |  |
| AliveMobsCheckDeltaTime | float | 配置刷怪管理器检查当前怪物存活情况的间隔 |  |
| SpawnWaves | TArray < FUGCSpawnWave > | 配置刷怪的波次 |  |

## Functions

### StartSpawnerManager

生效范围 服务器
	  启动刷怪管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetSpawnerManager

生效范围 服务器
	  重置刷怪管理器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bDeleteAllMobs | bool | 是否清除所有刷出的怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CleanAllMobs

生效范围 服务器
	  清理对刷出怪物的引用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bDelete | bool | 是否清除怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PauseSpawnerManager

生效范围 服务器
	  暂停刷怪管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResumeSpawnerManager

生效范围 服务器
	  恢复刷怪管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetSpawner

生效范围 服务器
	  获取波次中特定编号的刷怪点

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WaveIndex | int32  | 波次编号 |  |
| SpawnerIndex | int32 | 刷新点编号 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AUGCMobSpawner *  | 怪物刷新点 |  |

### GetCurrentWaveIndex

生效范围 服务器
	  获取当前波的波次编号

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | 当前波次编号 |  |

### GetWaveSpawnerNum

生效范围 服务器
	  获取对应波次的刷新点数量

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WaveIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | 刷新点数量 |  |

### GetWaveNum

生效范围 服务器
	  获取波次的数量

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | 波次数量 |  |

### SetMobConfigOverrideForSpawner

生效范围 服务器
	  修改特定波次中特定刷新点的怪物配置覆盖

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMobConfig | FUGCMobSpawnerMobConfig  | 新的怪物配置 | cppstruct/detail/FUGCMobSpawnerMobConfig.json |
| WaveIndex | int32  | 波次编号 |  |
| SpawnerIndex | int32 | 刷新点编号 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMobConfigOverrideForWave

生效范围 服务器
	  修改特定波次中所有刷新点的怪物配置覆盖

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMobConfig | FUGCMobSpawnerMobConfig  | 新的怪物配置 | cppstruct/detail/FUGCMobSpawnerMobConfig.json |
| WaveIndex | int32 | 波次编号 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMobConfigOverride

生效范围 服务器
	  修改所有波次的怪物配置覆盖

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMobConfig | FUGCMobSpawnerMobConfig | 新的怪物配置 | cppstruct/detail/FUGCMobSpawnerMobConfig.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CleanAllMobConfigOverride

生效范围 服务器
	  清除管理器所有的怪物配置覆盖

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### JumpToWave

生效范围 服务器
	  跳转到指定波次

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WaveIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

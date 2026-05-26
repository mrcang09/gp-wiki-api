# AUGCItemSpawnerManager

- Symbol Type: class
- Symbol Path: 和平全局接口 / 物品与背包 / AUGCItemSpawnerManager
- Source JSON Path: class/detail/和平全局接口/物品与背包/AUGCItemSpawnerManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/AUGCItemSpawnerManager.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

生成系统：物资生成管理器

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartCondition | EUGCItemSpawnerManagerStartCondition | 管理器的启动方式 |  |
| EventName | FString | 启动方式选择事件触发时，监听的GMP事件名 |  |
| ItemSpawners | TArray < FUGCItemSpawnerInfo > | 配置刷新点 |  |
| MaxWaveInternalTime | float | 配置两次刷新之间的最大时间间隔 |  |
| MinWaveInternalTime | float | 配置两次刷新之间的最小时间间隔 |  |
| MaxSpawnerNumPerWave | int32 | 配置同一时间有物资刷出的刷新点的最大数量 |  |
| MinSpawnerNumPerWave | int32 | 配置同一时间有物资刷出的刷新点的最小数量 |  |
| TotalSpawnWaveCount | int32 | 物资刷新的总轮数，设为-1则无限刷新 |  |
| bOverrideItemConfig | bool | 是否覆盖所有刷新点上的物资配置 |  |
| ItemConfig | FUGCItemSpawnerItemConfig | 配置所有刷新点上的物资配置 |  |

## Functions

### StartSpawnerManager

生效范围 服务器
	  启动管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetSpawnerManager

生效范围 服务器
	  重置管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CleanAllItem

生效范围 服务器
	  清理刷出的物资

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PauseSpawnerManager

生效范围 服务器
	  暂停物资刷新管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResumeSpawnerManager

生效范围 服务器
	  恢复物资刷新管理器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetItemConfigOverrideForSpawner

生效范围 服务器
	  修改特定刷新点的物资配置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InItemConfig | FUGCItemSpawnerItemConfig  | 新的物资刷新配置 | cppstruct/detail/FUGCItemSpawnerItemConfig.json |
| SpawnerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetItemConfigOverride

生效范围 服务器
	  修改所有刷新点的物资配置

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InItemConfig | FUGCItemSpawnerItemConfig | 新的物资刷新配置 | cppstruct/detail/FUGCItemSpawnerItemConfig.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CleanAllItemConfigOverride

生效范围 服务器
	  清除刷新点的物资配置设置，调用后将使用刷新点本身的配置

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

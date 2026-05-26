# UGCEMPZoneManager

- Symbol Type: class
- Symbol Path: Others / UGCEMPZoneManager
- Source JSON Path: class/detail/Others/UGCEMPZoneManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneManager.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

电磁干扰区管理器

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UGCEMPZoneManager.SuccessfullyGeneratedElectromagnetic |  | param InstanceID number<br>@param CenterLocation FVector |  |
| UGCEMPZoneManager.SuccessfullyStopElectromagnetic |  | param InstanceID number |  |
| UGCEMPZoneManager.NormalEndElectromagnetic |  | param InstanceID number |  |
| UGCEMPZoneManager.SuccessfullyStartElectromagnetic |  | param InstanceID number |  |
| UGCEMPZoneManager.AffectedElectromagneticPlayers |  | param AffectedPlayerKeys number |  |
| UGCEMPZoneManager.__EMPZoneMarkTypeID |  |  |  |
| UGCEMPZoneManager.__EMPZoneMarkInstIDs |  |  |  |

## Functions

### _ValidateAndClampConfig

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Config | UGCEMPZoneConfig |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCEMPZoneConfig |  |  |

### _GetInstanceDetailData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table|nil |  |  |

### _GetConfigByIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table|nil |  |  |

### _ModifyConfigByIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | number |  |  |
| NewConfig | table |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### _GetElectromagneticAreaConfigs

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number|nil |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table|nil |  |  |

### _ConvertToLuaConfigs

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElectromagneticInstances | table |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### _GenerateNextInstanceID

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### _MapLuaConfigToComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LuaConfig | UGCEMPZoneConfig |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEMPZoneCfg |  |  |

### _SyncCapsuleRadius

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EMPZoneActor | AEMPZoneActor |  |  |
| InstanceData | table |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### _WriteConfigToComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Comp | UEMPZoneControlComponent |  |  |
| ComponentConfig | FEMPZoneCfg |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### CreateEMPZone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConfigID | string |  |  |
| CenterLocation | FVector |  |  |

### _CreateEMPZoneActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### DestroyElectromagneticArea

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### _DestroyAllElectromagneticAreas

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### ModifyConfigElectromagneticArea

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConfigIndex | number |  |  |
| ParameterName | string |  |  |
| NewValue | any |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetAllConfigElectromagneticArea

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### GetSpecifyElectromagneticAreaList

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### _NotifyClientHideMapMark

当 EMPZone 销毁时隐藏小地图标记

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number |  |  |

### Client_OnEMPZoneMapMarkShow

[Client RPC] 显示 EMPZone 小地图标记

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number | 实例ID |  |
| LocX | number | 位置X坐标 |  |
| LocY | number | 位置Y坐标 |  |
| LocZ | number | 位置Z坐标 |  |
| EffectRadius | number | 影响半径 |  |
| ZoneState | number | 区域状态 |  |

### Client_OnEMPZoneMapMarkHide

[Client RPC] 隐藏 EMPZone 小地图标记

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number | 实例ID |  |

# UGCActivitySystem

- Symbol Type: class
- Symbol Path: Others / UGCActivitySystem
- Source JSON Path: class/detail/Others/UGCActivitySystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGCActivitySystem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

活动系统库（需要启用活动GamePart）

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UGCActivitySystem.OnActivityInfoReadyDelegate |  | 活动信息准备好时触发的委托<br>生效范围：客户端&&服务器 |  |
| UGCActivitySystem.OnUpdateValidActivityIDsDelegate |  | 更新有效活动时触发的委托<br>活动系统会按照每个活动配置的生效周期来定期更新有效活动<br>生效范围：客户端&&服务器 |  |

## Functions

### IsActivityInfoReady

活动信息是否已准备好
生效范围：客户端&&服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 活动信息是否已准备好 |  |

### GetAllActivityInfos

获取所有活动的信息
生效范围：客户端&&服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCActivityInfo[] | 所有活动信息 |  |

### GetActivityInfo

获取指定活动ID的活动信息
生效范围：客户端&&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActivityID | int | 活动ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCActivityInfo | 活动信息 |  |

### GetValidActivityIDs

获取所有有效的活动ID
生效范围：客户端&&服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int[] |  |  |

### GetNearestPeriodIndex

获取指定活动距当前时间最近的生效周期序号，
如果已经没有符合条件的开启周期，则返回最后一个生效周期的序号
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActivityID | int | 活动ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int | 活动开启周期序号, 0表示永久时间，-1表示活动不存在或未开启 |  |

# UBackpackComponentV2

- Symbol Type: class
- Symbol Path: Others / UBackpackComponentV2
- Source JSON Path: class/detail/Others/UBackpackComponentV2.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBackpackComponentV2.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

V2背包内核组件

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Warehouse | UUGCItemWarehouse_Backpack * | 仓库对象<br>	  基类：UUGCItemWarehouseBase |  |

## Functions

### RemoveItemNewFlag

移除物品新标记
	  DS、Client 可调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefineID | FItemDefineID & | 物品实例ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableItemNewFlag

激活物品新标记
	  DS、Client 可调用

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DisableItemNewFlag

失效物品新标记
	  DS、Client 可调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bForever | bool | 是否永久失效 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetItemIsNew

获取物品是否新标记
	  Client 可调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefineID | FItemDefineID & | 物品实例ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 物品是否有新标记 |  |

### CheckInitPersistCompleted

查询背包是否初始化完成，完成后才可以进行背包操作

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

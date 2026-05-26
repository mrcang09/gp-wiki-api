# BackpackUIComponent

- Symbol Type: class
- Symbol Path: Others / BackpackUIComponent
- Source JSON Path: class/detail/Others/BackpackUIComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/BackpackUIComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

UGC V2背包UI组件

需启用及配合新背包系统使用，具体参见https://developer.gp.qq.com/wikieditor/#/catalog/20104

## Functions

### GetHUDBtn

获取背包按钮控件
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget | 背包按钮控件 |  |

### GetDefaultMode

获取默认背包模式
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 背包模式 |  |

### ShowHUDBtn

显示背包按钮逻辑
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bVisible | bool | 是否显示 |  |

### CloseBattleMainPanel

关闭战斗背包界面
生效范围：客户端

### CloseLobbyPanel

关闭大厅背包界面
生效范围：客户端

### OpenLobbyBackpackMainUI

打开大厅背包界面
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Mode | number | 1:背包+装备栏 2:背包+仓库 3:背包+装备栏+仓库 |  |

### OpenBattleMainPanel

打开战斗背包界面
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Style | number | 0全屏，1半屏 |  |
| Mode | number | 1:背包+装备栏 2:背包+仓库 3:背包+装备栏+仓库 |  |

### OnOpenBattleMainPanel

背包UI打开后执行

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 背包主界面控件 |  |

### OnCloseBattleMainPanel

背包UI关闭后执行

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 背包主界面控件 |  |

### OnOpenDeletePanel

当打开删除弹窗时调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 面板控件 |  |

### ClickLockBackpackItem

点击上锁格子的响应函数（使用开放化控件UGC_ItemPurchasePopup_Open_UIBP）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| type | number | 类型 [0:背包数据, 1:仓库数据] |  |

### OnClickLockBackpackItem

当打开解锁弹窗时调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 面板控件 |  |

### IsDiscardAreaVisible

是否显示丢弃区域
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否显示丢弃区域 |  |

### OnOpenSaveOrWithDrawPanel

当打开存入取出代币时调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 面板控件 |  |

### OpenDropItemPanel

打开丢弃物品数量选择面板
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | FItemDefineID | 物品定义ID |  |
| Count | number | 物品最大数量 |  |

### OnOpenDropItemPanel

当打开丢弃物品弹窗时调用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Panel | UUserWidget | 面板控件 |  |

### CompareQuality

默认排序函数
生效范围: 客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data1 | table | 物品数据1 {DefineID:物品DefineID, Idx:格子索引} |  |
| Data2 | table | 物品数据2 {DefineID:物品DefineID, Idx:格子索引} |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | true:物品1在前, false:物品2在前 |  |

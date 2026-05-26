# UGCWeaponManagerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 物品与背包 / UGCWeaponManagerSystem
- Source JSON Path: class/detail/和平全局接口/物品与背包/UGCWeaponManagerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCWeaponManagerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

武器管理系统接口库

## Functions

### GetWeaponManagerComponent

获取武器管理组件
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWeaponManagerComponent | 武器管理组件 |  |

### GetWeaponBySlot

获取对应插槽的武器实例
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| Slot | ESurviveWeaponPropSlot | 武器槽位 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraWeapon | 武器 |  |

### GetCurrentWeapon

获取当前使用的武器实例
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraWeapon | 武器 |  |

### GetLastUsedWeapon

获取上一把武器
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraWeapon | 武器 |  |

### GetCurrentWeaponSlot

获取当前使用武器插槽
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESurviveWeaponPropSlot | 武器槽位 |  |

### SwitchWeaponBySlot

切换对应槽位的武器
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| Slot | ESurviveWeaponPropSlot | 武器槽位 |  |
| IsUseAnimation | boolean | 是否播放使用动画 |  |

### CurrentWeaponAttachToBack

收起武器
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

### GetWeaponItemID

获取武器ItemID
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Weapon | ASTExtraWeapon | 武器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品ID,对应物品表中ID |  |

### GetWeaponName

获取武器名
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Weapon | ASTExtraWeapon | 武器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 武器名称 |  |

### GetCurrentUsingAmmoID

获取当前消耗弹药
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 弹药ID |  |

### SetWeaponSlotVisible

设置武器的可见性
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| WeaponSlot | ESurviveWeaponPropSlot | 武器槽位 |  |
| bVisible | boolean | 是否可见 |  |

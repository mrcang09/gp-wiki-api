# UGCVehicleCommonSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 载具 / UGCVehicleCommonSystem
- Source JSON Path: class/detail/和平全局接口/载具/UGCVehicleCommonSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleCommonSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

载具系统通用功能接口库

## Functions

### SetVehicleHPMax

设置载具最大血量
本接口不会自动改变载具血量，游戏逻辑中改变载具血量时（比如收到伤害、载具维修等）会考虑载具最大血量
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| MaxHP | number | 最大血量 |  |

### SetVehicleHP

设置载具血量
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| HP | number | 血量 |  |

### SetVehicleFuelPercent

设置载具油量（按照百分比设置）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| FuelPercent | number | 油量百分比 |  |

### GetVehicleHPMax

获得载具最大血量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 载具最大血量 |  |

### GetVehicleHP

获得载具当前血量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 载具当前血量 |  |

### GetVehicleFuelMax

获得载具最大油量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 载具最大油量 |  |

### GetVehicleFuelConsumeFactor

获得当前油耗系数
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 当前油耗系数 |  |

### GetVehicleFuel

获得当前油量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 当前油量 |  |

### IsDontConsumeFuel

获得当前是否不耗油
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 当前是否不耗油 |  |

### IsDontDamage

获得当前是否不受到伤害
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 当前是否不受到伤害 |  |

### GetWheelHP

获得轮胎血量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| WheelIndex | number | 轮胎 ID（从 1 开始） |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 载具轮子血量 |  |

### SetWheelHP

设置轮胎血量
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| WheelIndex | number | 轮胎 ID（从 1 开始） |  |
| HP | number | 载具轮子血量 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 设置是否成功 |  |

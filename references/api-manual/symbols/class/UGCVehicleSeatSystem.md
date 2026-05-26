# UGCVehicleSeatSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 载具 / UGCVehicleSeatSystem
- Source JSON Path: class/detail/和平全局接口/载具/UGCVehicleSeatSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleSeatSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

载具系统座位系统接口库

## Functions

### ChangePassengerSeat

在目标座位上没有乘客时更换乘客座位
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| Passenger | ASTExtraBaseCharacter | 乘客 |  |
| SeatIndex | number | 座位 ID |  |

### ForceChangePassengerSeat

在目标座位上有乘客时更换乘客座位
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| Passenger | ASTExtraBaseCharacter | 乘客 |  |
| SeatIndex | number | 座位 ID |  |

### GetSeatNum

获得载具座位个数
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 载具座位个数 |  |

### GetAvailableSeatNum

获得空闲的载具座位个数
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 空闲的载具座位个数 |  |

### GetPassenger

获得对应座位的乘客
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraBaseCharacter | 对应座位的乘客 |  |

### IsSeatIndexAvailable

获得对应座位是否空着
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 对应座位是否空着 |  |

### GetCharacterSeatIndex

获得指定乘客的座位 ID
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| Passenger | ASTExtraBaseCharacter | 乘客 |  |
| GetBySocket | boolean | BySocket |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 指定乘客的座位 ID |  |

### GetDriver

获得司机
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraBaseCharacter | 司机 |  |

### GetPassengers

获得所有乘客
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASTExtraBaseCharacter[] | 所有乘客 |  |

### GetAvailableSeatIndexes

获得所有空闲座位的 Index
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32[] | 所有空闲座位的索引 |  |

### CanLeanOut

座位上是否可以探头
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否可以探头 |  |

### RemoveVehicleWeapon

移除指定座位上对应 ID 的车载武器
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |
| WeaponIndex | number | 车载武器 ID |  |

### AddVehicleWeaponFromSupportKit

将座位武器库中的武器装备到座位武器孔上
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |
| WeaponIndex | number | 车载武器 ID |  |
| WeaponIndexSupport | number | 武器库武器 ID |  |

### SetPassengerVehicleWeapon

设置当前座位上的车载武器是否能使用
需要这个座位原来也配置了载具武器，且乘客正在该座位上
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vehicle | ASTExtraVehicleBase | 载具 |  |
| SeatIndex | number | 座位 ID |  |
| bControlVehicleWeapon | boolean | 是否能控制车载武器 |  |

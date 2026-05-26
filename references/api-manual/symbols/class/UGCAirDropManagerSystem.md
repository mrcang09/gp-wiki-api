# UGCAirDropManagerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 玩法规则 / UGCAirDropManagerSystem
- Source JSON Path: class/detail/和平全局接口/玩法规则/UGCAirDropManagerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCAirDropManagerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

空投系统接口库

## Functions

### GenerateAirDrop

生成指定ID空投
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ID | number | 空投配置ID |  |
| DroppingLocation | FVector | 掉落位置 结构Vector={X=0,Y=0,Z=0} | cppstruct/detail/FVector.json |
| DroppingSpeed | number | 掉落速度 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bool, | int32 | 是否生成成功, 实例ID |  |

### GetAllAirDropConfigs

获得所有空投配置
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ID | number | 空投配置ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | OneAirDrop[] | 空投配置 |  |

### DestroyAirDrop

销毁指定实例ID空投
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InsID | number | 指定实例ID的空投 0.1s 后销毁 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否销毁成功 |  |

### GetAirDropItemList

获取指定实例ID空投的物品列表
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InsID | number | 空投实例InsID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPickUpItemData[] | 空投的物品列表 |  |

### GetAllAirDropInstanceIDs

获取当前场景内所有的实例ID
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32[] | 空投实例ID列表 |  |

# UGCGunSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 物品与背包 / UGCGunSystem
- Source JSON Path: class/detail/和平全局接口/物品与背包/UGCGunSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCGunSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

枪械系统接口库

## Functions

### StartFire

开火
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

### StopFire

停止开火
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

### EnableInfiniteBullets

启用/停用无限子弹（无需换弹）
启用后，弹夹容量无限，一直开火也无需换弹
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| IsEnable | boolean | 启用/停用 |  |

### EnableClipInfiniteBullets

启用/停用弹夹无限子弹（需要换弹一次）
启用后，子弹容量无限，开火会打空弹夹触发换弹
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| IsEnable | boolean | 启用/停用 |  |

### ForceReloadAndEnableInfiniteBullets

启用/停用无限子弹（无需换弹）并且强制换弹
启用后，强制换弹弹夹容量无限，一直开火也无需换弹，避免弹夹内子弹为0时触发检查
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| IsEnable | boolean | 启用/停用 |  |

### SetMaxBulletNumInOneClip

设置弹夹容量
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| MaxBulletNumInOneClip | number | 弹夹容量 |  |

### GetMaxBulletNumInOneClip

获取弹夹容量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 弹夹容量 |  |

### SetBulletFireSpeed

设置子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| BulletFireSpeed | number | 飞行速度 |  |

### GetBulletFireSpeed

获取子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 当前飞行速度 |  |

### SetShootIntervalTime

设置射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| ShootIntervalTime | number | 射击间隔时间 |  |

### GetShootIntervalTime

获取射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 射击间隔时间 |  |

### SetBulletRange

设置子弹射程
例：60000射程为600米
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| BulletRange | number | 子弹射程 |  |

### GetBulletRange

获取子弹射程
例：60000射程为600米
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 子弹射程 |  |

### SetBulletBaseDamage

设置子弹基础伤害
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| BulletBaseDamage | number | 基础伤害 |  |

### GetBulletBaseDamage

获取子弹基础伤害
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 基础伤害 |  |

### SetBulletMinimumDamage

设置子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| BulletMinimumDamage | number | 最低伤害 |  |

### GetBulletMinimumDamage

获取子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 最低伤害 |  |

### SetBulletImpulse

设置子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| BulletImpulse | number | 冲量 |  |

### GetBulletImpulse

获取子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 冲量 |  |

### SetReloadTime

设置换弹时间
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| ReloadTime | number | 换弹时间 |  |

### GetReloadTime

获取换弹时间                 
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 换弹时间 |  |

### SetTacticalReloadTime

设置战术换弹时间（弹夹子弹数不为0）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| TacticalReloadTime | number | 换弹时间 |  |

### GetTacticalReloadTime

获取战术换弹时间（弹夹子弹数不为0）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 换弹时间 |  |

### SetVerticalRecoilScale

设置垂直后坐力倍率
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| VerticalRecoilScale | number | 倍率 |  |

### GetVerticalRecoilScale

获取垂直后坐力倍率
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 倍率 |  |

### SetHorizontalRecoilScale

设置水平后坐力倍率
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| HorizontalRecoilScale | number | 倍率 |  |

### GetHorizontalRecoilScale

获取水平后坐力倍率
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 倍率 |  |

### SetDeviationScale

设置扩散值倍率
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| DeviationScale | number | 倍率 |  |

### GetDeviationScale

获取扩散值倍率
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 倍率 |  |

### Reload

玩家当前武器换弹
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

### OpenScope

玩家当前武器开镜/关镜
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| IsOpenScope | boolean | 开镜/关镜 |  |

### GetIsAutoAimEnabled

获取辅助瞄准是否启用 
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 启用/关闭 |  |

### SetIsAutoAimEnabled

设置自动瞄准是否启用 
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| IsAutoAimEnabled | boolean | 启用/关闭 |  |

### AddGunAttachment

武器添加指定配件
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| ItemDefineID | ItemDefineID | 物品DefineID |  |

### CreateAndAddGunAttachment

创建新配件并且直接添加到武器
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| ItemID | number | 物品ID |  |

### RemoveGunAttachmentBySocketType

卸载武器指定部位配件
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| SocketType | WeaponAttachmentSocketType | 配件槽位 |  |

### GetWeaponAttachmentIDBySocketType

获取特定槽位的配件ItemDefineID
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| SocketType | WeaponAttachmentSocketType | 配件槽位 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ItemDefineID |  |  |

### GetAvailableWeaponAttachmentSocketTypeList

获取枪械可用的配件槽位
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| uint8[] | @AttachmentSocketType | 列表 |  |

### GetAvailableWeaponAttachment

获取武器可用配件(需要武器加载出来才能使用，不能在武器初始化时调用)
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| int32[] | @AvailableWeaponAttachment | 列表 |  |

### DisuseAllWeaponAttachmentsOnServer

卸载武器所有配件
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

### GetWeaponAllAttachmentIDList

获取武器上的所有配件
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID[] | @AttachmentDefineID | 列表 |  |

### SetCurrentBulletNumInClip

设置武器弹匣内弹药
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Gun | STExtraShootWeapon | 枪械 |  |
| Count | int | 枪械 |  |

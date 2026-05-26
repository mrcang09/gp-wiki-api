# UGCProjectileSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 技能系统 / UGCProjectileSystem
- Source JSON Path: class/detail/和平全局接口/技能系统/UGCProjectileSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCProjectileSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

抛体系统接口库

## Functions

### SpawnProjectile

生成抛体
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProjectileSpawnInfo | ProjectileSpawnInfo | 抛体生成参数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APVEProjectileBase | 抛体对象实例 |  |

### GetDestroyAfterHit

获取抛体命中之后是否销毁
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Projectile | APVEProjectileBase | 抛体 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否命中后销毁 |  |

### SetDestroyAfterHit

设置抛体命中之后是否销毁
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Projectile | APVEProjectileBase | 抛体 |  |
| bNewDestroyAfterHit | boolean | 是否销毁 |  |

### GetPMComp

获取抛体运动组件
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Projectile | APVEProjectileBase | 抛体 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 抛体运动组件 |  |

### SetMoveAfterImpactWithNoLost

设置抛体命中之后是否继续移动
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Projectile | APVEProjectileBase | 抛体 |  |
| bNeedUpdateImmide | boolean | 是否更新组件速度 |  |

### GetLastUpdateCompBeforeStop

停止前最后更新的组件
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Projectile | APVEProjectileBase | 抛体 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 最后更新的组件 |  |

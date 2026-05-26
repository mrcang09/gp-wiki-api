# AEliteProjectile

- Symbol Type: class
- Symbol Path: Others / AEliteProjectile
- Source JSON Path: class/detail/Others/AEliteProjectile.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AEliteProjectile.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

投掷物

## Functions

### AddOnProjectileDestroyedHandler

生效范围SC
	  添加销毁事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDelegate | FSimpleProjectileDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveOnProjectileDestroyedHandler

生效范围SC
	  移除销毁事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDelegate | FSimpleProjectileDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveProjectileExplodedEvent

生效范围SC
	  爆炸事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impact | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveProjectileHit

生效范围SC
	  击中事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hit | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveProjectileBouncedEvent

生效范围SC
	  弹射事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ImpactResult | FHitResult &  |  |  |
| ImpactVelocity | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveProjectileStoppedEvent

生效范围SC
	  停止事件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# AUniversalProjectileBase

- Symbol Type: class
- Symbol Path: Others / AUniversalProjectileBase
- Source JSON Path: class/detail/Others/AUniversalProjectileBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AUniversalProjectileBase.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

通用抛体

## Functions

### ReceiveCustomFilter

自定义的过滤器接口
	 生效范围：SC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ReceivePlayExplosionEffectToAllTarget

自定义爆炸范围内筛选过后所有碰撞结果接口
	 生效范围：S

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FoundTargets | TArray < FHitResult > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceivePlayExplosionEffect

自定义爆炸范围内筛选过后碰撞接口
	 生效范围：S

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ExplosionTarget | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveBeginExplodeTimer

爆炸开始计时的额外接口（如果有延时爆炸）
	 生效范围：S

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveEndExplodeTimer

爆炸停止计时的额外接口（如果有延时爆炸）
	 生效范围：S

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

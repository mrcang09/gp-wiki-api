# UCustomActorMoveComponent

- Symbol Type: class
- Symbol Path: Others / UCustomActorMoveComponent
- Source JSON Path: class/detail/Others/UCustomActorMoveComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCustomActorMoveComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

一个给ActivityBaseActor移动功能的组件，用于移动所挂载的ActivityBaseActor

## Functions

### StartMove

生效范围：S
	  开始移动

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopMove

生效范围：S
	  结束移动

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMoveSpeed

生效范围：S
	  设置移动速度

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSpeed | float | 速度 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetGlideTime

生效范围：S
	  设置固定的滑行时间, 而不是使用起始点到终点位置除以速度得到这个数值

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GlideTime | float | 滑行时间 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPosition

生效范围：S
	  设置移动的起始点和终点

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InStart | FVector  | 起点 |  |
| InEnd | FVector | 终点 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsMoving

生效范围：SC
	  获取Actor是否在移动
	  return 是否在移动

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

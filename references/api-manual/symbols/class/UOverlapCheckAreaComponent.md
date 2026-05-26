# UOverlapCheckAreaComponent

- Symbol Type: class
- Symbol Path: Others / UOverlapCheckAreaComponent
- Source JSON Path: class/detail/Others/UOverlapCheckAreaComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UOverlapCheckAreaComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

区域重叠检测组件，能够检测到某个范围内开启重叠检测的Actor

## Functions

### CheckOverlapActor

生效范围：S
	  触发一次区域重叠检测

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StartCheck

生效范围：S
	  开始检测

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIgnoreActorList | TArray < AActor * >  |  |  |
| bStopIfStarted | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopCheck

生效范围：S
	  停止检测

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddIgnoreActors

生效范围：S
	  添加要忽略的Actor列表

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Ignores | TArray < AActor * > | 要添加的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveIgnoreActor

生效范围：S
	  移除忽略的Actor列表

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Ignore | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

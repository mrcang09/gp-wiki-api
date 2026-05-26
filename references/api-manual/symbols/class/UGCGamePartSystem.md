# UGCGamePartSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 商业化与功能模板 / UGCGamePartSystem
- Source JSON Path: class/detail/和平全局接口/商业化与功能模板/UGCGamePartSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGCGamePartSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

GamePart系统接口库

## Functions

### GetGamePartConfig

获取指定GamePart的Config
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GamePartName | string | GamePart名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUGCGamePartConfig | 指定GamePart的Config |  |

### GetGamePartGlobalActor

获取指定GamePart的GlobalActor
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GamePartName | string | GamePart名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor | 指定GamePart的GlobalActor |  |

### GetGamePartPlayerComponent

获取指定GamePart的指定玩家的指定PlayerComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GamePartName | string | GamePart名称 |  |
| PC | PlayerController | 玩家控制器 |  |
| PlayerComponentName | string | PlayerComponent名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent | 指定的PlayerComponent |  |

### IsGamePartLoaded

获取指定GamePart是否已加载

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GamePartName | string | GamePart名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | GamePart是否已加载 |  |

### GetAllLoadedGameParts

获取所有已加载的GamePart

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string[] | 所有已加载的GamePart列表 |  |

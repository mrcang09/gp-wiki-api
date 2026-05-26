# UGCMultiMode

- Symbol Type: class
- Symbol Path: 和平全局接口 / 玩法规则 / UGCMultiMode
- Source JSON Path: class/detail/和平全局接口/玩法规则/UGCMultiMode.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCMultiMode.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

多模式匹配通用接口库

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UGCMultiMode.NotifyMatchResponseDelegate |  | 通知“开始匹配”的结果。通常会立即通知，然后进入“匹配中”的状态<br>生效范围：客户端<br>@param bSuccess boolean @是否匹配成功。通常来说 true 则把匹配界面切换到匹配中的状态，false 则把匹配界面切换到尚未开始匹配的状态 |  |
| UGCMultiMode.NotifyMatchSucceededDelegate |  | 通知在“匹配中”的玩家，匹配成功，即将进入新的对局游戏<br>生效范围：客户端 |  |
| UGCMultiMode.NotifyStatusOfReadyMatchChangedDelegate |  | 通知准备匹配的状态变化<br>生效范围：客户端<br>@param UID number @玩家 UID<br>@param NewStatus EStatusOfReadyMatch @新的准备匹配的状态<br>@param OldStatus EStatusOfReadyMatch @老的准备匹配的状态 |  |

## Functions

### SetModeChooseUIVisible

设置模式选择 UI 的显示/隐藏
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Visible | boolean | 设置为显示/隐藏 |  |

### SetModeState

设置模式选择 UI 的子模式可选择状态
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModeID | number | 模式 ID |  |
| ModeAvailability | boolean | 设置为可用/不可用 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 操作是否成功 |  |

### GetModeID

获取当前模式 ID
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 当前模式 ID，若不存在则返回 0 |  |

### SetModeChooseButtonVisible

设置模式选择打开按钮的显示/隐藏
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Visible | boolean | 设置为显示/隐藏 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 操作是否成功 |  |

### SetPlayerFill

开启/关闭补人
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bPlayerFill | boolean | 目标状态 |  |

### RequestMatch

开始匹配
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubModeID | number | 子模式 ID |  |
| ResCallBack | function | 一个接受 bool 入参的回调函数，发起匹配的结果返回后会调用该函数 |  |
| Obj | UObject | 回调函数所属的对象 |  |
| IsTeamUnfill | boolean | 是否允许不匹配队友开始匹配 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否请求匹配成功 |  |

### RequestCancelMatch

请求取消匹配
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 请求是否发送成功 |  |

### RequestReadyMatch

请求进入准备匹配状态
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bReady | boolean | 是否准备匹配 |  |

### QueryStatusOfReadyMatch

查询准备匹配的状态
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UID | number | 玩家 UID，可选，如果传入 nil 或者不传入，那么获取自己的准备匹配状态 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EStatusOfReadyMatch | 准备匹配的状态 |  |

### GetModeSetting

获取指定ModeID的配置
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModeID | number | ModeID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ModeSetting | ModeID对应的设置 |  |

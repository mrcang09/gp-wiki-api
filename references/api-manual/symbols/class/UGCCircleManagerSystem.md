# UGCCircleManagerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 玩法规则 / UGCCircleManagerSystem
- Source JSON Path: class/detail/和平全局接口/玩法规则/UGCCircleManagerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCCircleManagerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

信号圈系统接口库

## Functions

### GetBlueCircleCenter

获取当前蓝圈中心
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | Vector2D | 蓝圈中心 {X，Y} |  |

### GetWhiteCircleCenter

获取当前白圈中心
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | Vector2D | 白圈中心 {X，Y} |  |

### GetBlueCircleRadius

获取当前蓝圈半径
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 半径 |  |

### GetWhiteCircleRadius

获取当前白圈半径
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 半径 |  |

### GetCurrentCircleIndex

获得当前运行到的信号圈序号
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 信号圈序号 缩圈结束时，返回最后一个信号圈序号 |  |

### GetAllCircleConfig

获得所有信号圈配置
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FCirCleCfg[] | 所有信号圈配置 |  |

### GetCurrentConfigCircle

获取当前信号圈配置
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FCirCleCfg | 当前信号圈配置 |  |

### GetNextConfigCircle

获取下一信号圈配置
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FCirCleCfg | 下一信号圈配置 |  |

### TogglePoisonCircle

开启或者关闭信号圈（关闭状态则开启，开启状态则关闭）
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 调用后状态为开启或者关闭 |  |

### StartCircle

启用信号圈
生效范围：服务器

### StopCircle

关闭信号圈
生效范围：服务器

### PauseCircle

暂停信号圈
生效范围：服务器

### ResumeCircle

恢复暂停信号圈
生效范围：服务器

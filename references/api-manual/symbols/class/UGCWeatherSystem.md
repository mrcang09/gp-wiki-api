# UGCWeatherSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 场景与环境 / UGCWeatherSystem
- Source JSON Path: class/detail/和平全局接口/场景与环境/UGCWeatherSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9C%BA%E6%99%AF%E4%B8%8E%E7%8E%AF%E5%A2%83/UGCWeatherSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

天气系统接口库

## Functions

### LoadWeatherSequence

加载天气序列
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |
| WeatherSequence | WeatherSequence | 天气序列资源 |  |
| BlendTime | number | 过渡时间 |  |

### UnloadWeatherSequence

卸载天气序列
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |
| WeatherSequence | WeatherSequence | 天气序列资源 |  |

### SeekWeatherSequence

设置天气序列播放进度
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |
| WeatherSequence | WeatherSequence | 天气序列资源 |  |
| Time | number | 目标时间 |  |

### PauseWeatherSequence

暂停天气序列
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |
| WeatherSequence | WeatherSequence | 天气序列资源 |  |

### ResumeWeatherSequence

继续天气序列
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |
| WeatherSequence | WeatherSequence | 天气序列资源 |  |

### GetCurrentWeatherSequence

获取当前天气序列
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | WeatherSequence | 天气序列资源 |  |

### GetCurrentWeatherPlayPercentage

获取当前天气播放进度
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 播放进度（0~1） |  |

### GetCurrentWeatherTime

获取当前天气时间
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | PlayerController | 玩家控制器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 天气时间（0~24） |  |

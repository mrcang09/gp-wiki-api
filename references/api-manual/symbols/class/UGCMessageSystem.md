# UGCMessageSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 社交系统 / UGCMessageSystem
- Source JSON Path: class/detail/和平全局接口/社交系统/UGCMessageSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCMessageSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

游戏聊天通用接口库

## Functions

### JoinCampMessageChannel

阵营聊天 开局分阵营或阵营变更时同步阵营信息，创建阵营的聊天室
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number | 玩家的 PlayerKey |  |
| CampID | number | 阵营 ID（传入0为无阵营） |  |

### SendSystemMessageToPlayer

给单独玩家发送系统消息
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number | 玩家 PlayerKey |  |
| MessageTag | string | 消息标题 |  |
| MessageContent | string | 消息内容 |  |
| Level | number | 消息等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否发送成功 |  |

### SendSystemMessageToAll

给所有玩家发送系统消息
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MessageTag | string | 消息标题 |  |
| MessageContent | string | 消息内容 |  |
| Level | number | 消息等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否发送成功 |  |

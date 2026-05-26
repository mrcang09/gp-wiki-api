# UGCFakePlayerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 怪物系统 / UGCFakePlayerSystem
- Source JSON Path: class/detail/和平全局接口/怪物系统/UGCFakePlayerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCFakePlayerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

假人玩家系统

## Functions

### SpawnFakePlayer

生成假人玩家， GameMode 中 DataManager，AIProbe 数据中配置 AIController
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIPlayerKey | number | AIPlayerKey，建议使用 UGCFakePlayerSystem.GetRandomAIPlayerKey 生成 |  |
| TeamID | number | 队伍 ID |  |

### GetRandomAIPlayerKey

生成随机AIPlayerKey，用于UGCFakePlayerSystem.SpawnFakePlayer接口参数
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | AIPlayerKey |  |

### DestroyFakePlayer

销毁假人玩家
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIPlayerKey | number | AIPlayerKey |  |

# UGCPrivilegeSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 商业化与功能模板 / UGCPrivilegeSystem
- Source JSON Path: class/detail/和平全局接口/商业化与功能模板/UGCPrivilegeSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGCPrivilegeSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

特权系统接口库

## Functions

### GetPlayerPrivilegesInformation

获取玩家特权 ID 信息列表，如果玩家没有特权 ID 信息或者在 PIE 环境下返回 nil
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UID | number | 玩家UID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table | 玩家特权ID信息列表，table = { [id1] = { Description = "" }, [id2] = { Description = "" }, [id3] = { Description = "" }, ... } |  |

### DoesPlayerHavePrivileges

判断玩家是否拥有特权，没有特权或者在 PIE 环境下返回 false
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UID | number | 玩家UID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 玩家是否拥有特权 |  |

### AddPrivilegeEmblemFlagUI

给指定队友（不包含主控玩家自己）添加绿洲特权徽章UI标记
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerState | PlayerState | 队友PlayerState |  |
| NameColorHexStr | string | 玩家名字颜色 |  |
| bHideTeammatePositionItemName | boolean | 是否隐藏队友标记名 |  |

### RemovePrivilegeEmblemFlagUI

给指定队友（不包含主控玩家自己）移除绿洲特权徽章UI标记
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerState | PlayerState | 队友PlayerState |  |

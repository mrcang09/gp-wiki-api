# UGCDelegateUtility

- Symbol Type: class
- Symbol Path: 和平全局接口 / 基础功能 / UGCDelegateUtility
- Source JSON Path: class/detail/和平全局接口/基础功能/UGCDelegateUtility.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCDelegateUtility.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

UGC 委托工具库

Lua 委托工具
- 使用 New() 创建委托
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Functions

### CreateLuaDelegate

创建 Lua 委托（纯 Lua 实现）

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UGCLuaDelegate | @Lua | 委托 |  |

### CopyLuaDelegate

复制 Lua 委托

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | UGCLuaDelegate | 被复制的 Lua 委托 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCLuaDelegate | 复制出来的新 Lua 委托 |  |

### CreateUEDelegate

创建虚幻兼容单播委托

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Outer | UObject | Outer 对象（GC 相关） |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULuaSingleDelegate | 虚幻兼容单播委托 |  |

### DestroyUEDelegate

销毁虚幻兼容单播委托

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UEDelegate | ULuaSingleDelegate | 虚幻兼容单播委托 |  |

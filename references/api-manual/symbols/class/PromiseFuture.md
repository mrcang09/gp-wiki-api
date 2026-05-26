# PromiseFuture

- Symbol Type: class
- Symbol Path: 和平全局接口 / 工具库 / PromiseFuture
- Source JSON Path: class/detail/和平全局接口/工具库/PromiseFuture.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/PromiseFuture.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

提供处理异步操作的类，支持链式调用和状态管理

说明：
- 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
- 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
- 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
- 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
- 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

## Functions

### Resume

手动恢复 PromiseFuture 的执行

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ... | any | 可选的参数，将传递给恢复的协程 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 当 IsPrerequisitesEstablished() && IsEstablished() 时返回 true，否则返回 false |  |

### IsPrerequisitesEstablished

检查所有先决条件是否已建立

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 如果所有先决条件都已建立则返回 true，否则返回 false |  |

### IsAnyPrerequisiteCancellationRequested

检查任意先决条件是否已被取消

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 如果任意先决条件已被取消则返回 true，否则返回 false |  |

### IsEstablished

检查当前 PromiseFuture 是否已建立

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 如果已建立则返回 true，否则返回 false |  |

### WaitForPrerequisites

等待所有前置条件变为已建立状态
如果前置条件未完成，则会自动 Yield
只能在 Set 回调函数中使用

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### AddPrerequisites

添加前置条件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Prerequisite | PromiseFuture | 前置条件 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### IsCancellationRequested

检查当前 PromiseFuture 是否已被取消

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 如果已被取消则返回 true，否则返回 false |  |

### Cancel

取消当前 PromiseFuture 的执行

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### CancelAll

取消当前 PromiseFuture 及其所有前置条件的执行

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### Get

获取 Set 回调函数的返回值
只能在 Set、Then 回调函数中使用

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | any | 返回 Set 回调函数的所有返回值 |  |

### Then

设置成功回调函数

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Callable | function | 回调函数 |  |
| ... | any | 可选的参数，将传递给回调函数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### Else

设置失败回调函数

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Callable | function | 回调函数 |  |
| ... | any | 可选的参数，将传递给回调函数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### Set

设置执行逻辑

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Setter | function | 回调函数 |  |
| SetterValue | any |  |  |
| ... | any | 其他可选参数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### Yield

暂停当前 PromiseFuture 的执行
只能在 Set 回调函数中使用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ... | any | 可选的参数，将传递给 yield(...) 方法 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

### AutoResume

设置自动恢复功能

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WatchedObject | UObject | 监控的对象，如果对象被销毁则停止自动恢复 |  |
| Interval | number | 自动恢复的间隔，单位为秒 |  |
| Timeout | number | 自动恢复的超时时间，单位为秒 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 当前 PromiseFuture 实例，以支持链式调用 |  |

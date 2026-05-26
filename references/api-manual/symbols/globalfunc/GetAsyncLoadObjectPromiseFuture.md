# GetAsyncLoadObjectPromiseFuture

- Symbol Type: globalfunc
- Symbol Path: GetAsyncLoadObjectPromiseFuture
- Source JSON Path: globalfunc/detail/GetAsyncLoadObjectPromiseFuture.json
- Source JSON URL: https://developer.gp.qq.com/api/globalfunc/detail/GetAsyncLoadObjectPromiseFuture.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

使用 PromiseFuture 异步加载资源并创建对象实例
用法：GetAsyncLoadObjectPromiseFuture(PlayerController, ObjectPath):Then(function (PromiseFuture) local Obj = PromiseFuture:Get() end):AutoResume()
生效范围：服务器&客户端

## Parameters

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Outer | UObject | Outer 对象，一般为 PlayerController |  |
| FullPath | string | 资源路径 |  |

## Returns

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PromiseFuture | @PromiseFuture | 对象 |  |

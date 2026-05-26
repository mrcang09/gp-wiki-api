# UnrealNetwork

- Symbol Type: class
- Symbol Path: 和平全局接口 / 基础功能 / UnrealNetwork
- Source JSON Path: class/detail/和平全局接口/基础功能/UnrealNetwork.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UnrealNetwork.json
- Mirrored At (UTC): 2026-05-19 08:23:43Z

---

## Description

虚幻网络库

## Functions

### RepLazyProperty

对声明为复制的Lazy属性执行复制

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetObject | AActor | UActorComponent @属性所在的Actor或Component | 属性所在的Actor或Component |  |
| PropertyName | string | 属性名或路径 |  |

### CallUnrealRPC

发送可靠单播RPC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetPlayerController | APlayerController | 目标玩家 |  |
| TargetObject | AActor | UActorComponent @目标Actor或Component | 目标Actor或Component |  |
| FunctionName | string | RPC函数名 |  |

### CallUnrealRPC_Unreliable

发送不可靠单播RPC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetPlayerController | APlayerController | 目标玩家 |  |
| TargetObject | AActor | UActorComponent @目标Actor或Component | 目标Actor或Component |  |
| FunctionName | string | RPC函数名 |  |

### CallUnrealRPC_Multicast

发送可靠广播RPC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetObject | AActor | UActorComponent @目标Actor或Component | 目标Actor或Component |  |
| FunctionName | string | RPC函数名 |  |

### CallUnrealRPC_Multicast_Unreliable

发送不可靠广播RPC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetObject | AActor | UActorComponent @目标Actor或Component | 目标Actor或Component |  |
| FunctionName | string | RPC函数名 |  |

# UPersistEffectBuff

- Symbol Type: class
- Symbol Path: Others / UPersistEffectBuff
- Source JSON Path: class/detail/Others/UPersistEffectBuff.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBuff.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

Buff系统归属与和平精英的技能系统，用于帮助开发者更方便快捷地实现Buff效果
  通过与Tag、Attribute等系统的配合能够通过配置就实现大部分所需的效果
  对于更细致的Buff效果也可以通过重写BP结尾的函数来实现定制化效果。

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BuffInfo | FPEBuffInfo | 生效范围：服务器&客户端<br>      Buff蓝图的配置信息 |  |

## Functions

### AddStackNum

生效范围：服务器
	  修改堆叠层数，修改后的层数大于等于0且小于等于最大堆叠层数(MaxStackNum)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Num | int32 | 新增的层数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStackNum

生效范围：服务器&客户端
	 获取当前层数

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | 当前层数 |  |

### GetCauser

生效范围：服务器&客户端
      获取Buff的施加者

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * | 施加者 |  |

### SetCauser

生效范围：服务器
	 设置Buff的施加者

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Causer | AActor * | 施加者 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### TriggerAllLayer

生效范围：服务器
      触发当前所有层的Buff的效果

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### TriggerSingleLayer

生效范围：服务器
	  触发单层的Buff的效果

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RefreshBuff

生效范围：服务器
	  重置Buff持续时间

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetBuffEnable

生效范围：服务器
	  设置Buff是否生效

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsEnable | bool | 是否生效 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBuffEnable

生效范围：服务器&客户端
	  获取Buff当前是否生效

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否生效 |  |

### Pause

生效范围：服务器
	  暂停Buff持续减少剩余时间

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Resume

生效范围：服务器
	  恢复Buff持续减少剩余时间

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OverwriteBuffUIInfo

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BuffName | FName &  | Buff名字 |  |
| BuffDetail | FString &  | Buff描述 |  |
| BuffIconPath | FString & | Buff图标路径 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBuffName

生效范围：服务器&客户端
	  获取Buff名字

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName | Buff名字 |  |

### GetBuffDetail

生效范围：服务器&客户端
	  获取Buff描述

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | Buff描述 |  |

### GetBuffIconPath

生效范围：服务器&客户端
	  获取Buff图标路径

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | Buff图标路径 |  |

# UGCGameplayTagSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 工具库 / UGCGameplayTagSystem
- Source JSON Path: class/detail/和平全局接口/工具库/UGCGameplayTagSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCGameplayTagSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

GameplayTag接口库

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UGCGameplayTagSystem.Tags.PawnState |  |  |  |

## Functions

### RequestGameplayTag

根据字符串获取FGameplayTag
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagString | string | Tag的字符串 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTag | 是否为合法的Tag | cppstruct/detail/FGameplayTag.json |

### IsValidTag

检查一个Tag是否合法
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | UGCGameplayTag|string|FGameplayTag | Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否为合法的Tag |  |

### IsUGCGameplayTag

检查一个Tag是否是UGCGameplayTag
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tag | UGCGameplayTag | UGCGameplayTag的lua对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否为UGCGameplayTag |  |

### MatchesTag

检查TagA是否与TagB匹配
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagA | UGCGameplayTag|string|FGameplayTag | Tag |  |
| TagB | UGCGameplayTag|string|FGameplayTag | Tag |  |
| bExactMatch | boolean | 是否精确匹配 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否匹配 |  |

### EqualsTag

检查TagA是否与TagB相等
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagA | UGCGameplayTag|string|FGameplayTag | Tag |  |
| TagB | UGCGameplayTag|string|FGameplayTag | Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否相等 |  |

### CreateGameplayTagContainer

创建一个空的FFGameplayTagContainer
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer | 空的FGameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |

### CreateGameplayTagContainerFromTag

创建一个包含指定FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SingleTag | UGCGameplayTag|string|FGameplayTag | 传入FGameplayTagContainer中的FGameplayTag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer | 包含传入FGameplayTag的GameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |

### CreateGameplayTagContainerFromArray

创建一个包含一组FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTags | FGameplayTag[] | 传入FGameplayTagContainer中的FGameplayTags |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer | 包含传入FGameplayTags的GameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |

### AddGameplayTagToContainer

将单个FGameplayTag添加到传入的FGameplayTagContainer中
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer | 要追加到的FGameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |
| Tag | FGameplayTag | 要添加到FGameplayTagContainer中的FGameplayTag | cppstruct/detail/FGameplayTag.json |

### RemoveGameplayTagFromContainer

从传入的FGameplayTagContainer中移除单个FGameplayTag，若找到并移除则返回 true ，否则返回 false
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer | 要从中移除的FGameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |
| Tag | FGameplayTag | 要从FGameplayTagContainer中移除的FGameplayTag | cppstruct/detail/FGameplayTag.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否成功移除 |  |

### HasTag

检查FGameplayTagContainer是否包含特定的FGameplayTag
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer | 要从中查找指定FGameplayTag的FGameplayTagContainer | cppstruct/detail/FGameplayTagContainer.json |
| Tag | FGameplayTag | 要从FGameplayTagContainer中检查的FGameplayTag | cppstruct/detail/FGameplayTag.json |
| bExactMatch | boolean | 是否精确匹配 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否包含Tag |  |

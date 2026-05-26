# UGCItemSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 物品与背包 / UGCItemSystem
- Source JSON Path: class/detail/和平全局接口/物品与背包/UGCItemSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

道具系统接口库

## Functions

### GetItemType

获取物品ItemType
对应表格数据：和平精英\表格\物品表中ItemType列
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品类型 |  |

### GetItemSubType

获取ItemSubType
对应表格数据：和平精英\表格\物品表中ItemSubType列
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品子类型 |  |

### GetItemData

获取道具数据
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FBattleItem_TabRes | 物品数据 |  |

### IsUGCItem

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否为绿洲物品 |  |

### IsCanUseInBackpack

返回道具在背包中是否可以使用
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否可以使用 |  |

### GetPickupWrapperClassPath

通过ItemID获取Wrapper路径
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | Wrapper路径 |  |

### SetWrapperToGround

将Wrapper设置贴在地面
Wrapper.bDropedByPlayer为True时，贴地功能生效
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetWrapperItemID

获取Wrapper关联的ItemID
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品ID |  |

### ModifyWrapperItemCount

修改Wrpaaer中物品的数量
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |
| Count | number | 修改后的数量 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### DoPickWrapper

拾取Wrapper
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn |  |  |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### IsWrapperDropedByPlayer

Wrapper是否是由玩家丢弃生成
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### SetWrapperPickUpRadius

设置Wrapper的可拾取范围
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WrapperActor | APickUpWrapperActor | 可拾取物 |  |
| Radius | number | 可拾取范围，单位厘米 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetQualityTexturePath

获取品质色的128*128纹理路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QualityRank | number | 品质等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 品质纹理路径 |  |

### GetBigQualityTexturePath

获取品质色的128*256纹理路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QualityRank | number | 品质等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 品质纹理路径string |  |

### GetQualityBarTexturePath

获取品质色条纹理路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QualityRank | number | 品质等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 品质纹理路径string |  |

# UGCItemSystemV2

- Symbol Type: class
- Symbol Path: 和平全局接口 / 物品与背包 / UGCItemSystemV2
- Source JSON Path: class/detail/和平全局接口/物品与背包/UGCItemSystemV2.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystemV2.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

V2道具系统接口库

## Functions

### GetConfigItemHandle

获取物品 ItemHandle 配置
可以通过它取得所有物品中配置的数据（只读）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UBattleItemHandleBase | 配置数据 |  |

### GetItemInstanceDataManager

获取物品实例数据管理器
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUGCBattleItemInstanceDataManager | 实例数据管理器 |  |

### IsUGCItemV2

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否为绿洲物品 |  |

### IsShouldPersist

是否持久化
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否持久化 |  |

### IsObjEditorItemV2

是否为V2版本物编创建的物品
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否为V2版本物编创建的物品 |  |

### GetItemNameV2

返回物品名称
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品名称 |  |

### GetItemSubTypeV2

返回物品子类型SubType，(比如武器类别为1，M146子类型为101)
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品子类型 |  |

### GetItemIconTextureV2

返回物品图标路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 物品图标路径 | cppstruct/detail/FSoftObjectPath.json |

### GetOwnBackpackComponent

读取物品所在背包
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemHandle | UBattleItemHandleBase | 物品 Handle |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | BackpackComponentV2 | V2背包组件 |  |

### GetItemIconWithPlayerSkinV2

返回物品图标路径(带玩家皮肤)
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |
| PlayerController | PlayerController | 玩家 PlayerController |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 物品图标路径 | cppstruct/detail/FSoftObjectPath.json |

### GetWhiteIconTextureV2

返回物品剪影图标路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 剪影图标路径 | cppstruct/detail/FSoftObjectPath.json |

### GetBigIconTextureV2

返回物品装备栏图标路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 装备栏图标路径 | cppstruct/detail/FSoftObjectPath.json |

### GetBigIconTextureWithPlayerSkinV2

返回物品装备栏图标路径(带玩家皮肤)
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |
| PlayerController | PlayerController | 玩家 PlayerController |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 装备栏图标路径 | cppstruct/detail/FSoftObjectPath.json |

### GetItemDetailV2

返回物品详情
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品详情 |  |

### GetItemPickupDetailV2

返回物品拾取描述
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品拾取描述 |  |

### ItemHasTagV2

是否含有某个 Tag
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |
| Tag | string | 物品 Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否含有 Tag |  |

### GetItemTagsV2

返回物品所有 Tag
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string[] | 物品所有 Tag |  |

### ItemCanDropV2

返回物品是否可丢弃
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 物品是否可丢弃 |  |

### ItemCanRemoveV2

返回物品是否可销毁
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 物品是否可销毁 |  |

### IsCanUseV2

返回物品在背包中是否可以使用
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否可以使用 |  |

### GetItemMaxNumberOfStacksV2

返回物品最大堆叠数量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品最大堆叠数量 |  |

### GetItemQualityV2

返回物品品质
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 物品品质 |  |

### GetItemCustomizedTypeV2

返回物品自定义类型
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品自定义类型 |  |

### LoadItemCustomData

获取物品自定义实例化数据
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | FItemDefineID | 物品DefineID | cppstruct/detail/FItemDefineID.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table | 物品自定义实例化数据table |  |

### SaveItemCustomData

保存物品自定义实例化数据
注意: 实例数据也包含了和平内置数据，应避免直接覆盖，采用下述方式添加数据
local CustomData = UGCItemSystemV2.LoadItemCustomData(ItemDefineID)
CustomData.NewKey = NewTableData -- 填充新的数据
UGCItemSystemV2.SaveItemCustomData(ItemDefineID, CustomData)
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | FItemDefineID | 物品DefineID | cppstruct/detail/FItemDefineID.json |
| ItemCustomData | table | 物品自定义实例化数据table |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 保存成功or失败 |  |

### GetItemDefineID

通过物品ID创建一个全新的物品实例，并返回 DefineID
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FItemDefineID | 物品 DefineID | cppstruct/detail/FItemDefineID.json |

### SetItemCommonReason

设置物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | FItemDefineID | 物品 DefineID | cppstruct/detail/FItemDefineID.json |
| Reason | number | Reason |  |

### GetItemCommonReason

获取物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | FItemDefineID | 物品 DefineID | cppstruct/detail/FItemDefineID.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | Reason |  |

### GetEquipTargetSlots

获取装备物品拥有的槽位列表
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string[] | 物品拥有的所有槽位 |  |

### GetDisplayNameBySlotName

获取槽位对应的展示名
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |
| SlotName | string | 槽位名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品槽位的展示名称 |  |

### GetAttachTargetItem

获取物品附加在哪个物品上
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemDefineID | ItemDefineID | 物品 DefineID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool,ItemDefineID,FName | 物品是否正附加在另一个物品上,物品附加的目标物品 DefineID,物品附加的目标物品槽位 |  |

### GetAttachChildItem

获取附加在物品上的子物品
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AttachParentID | ItemDefineID | 父物品的 DefineID |  |
| AttachSlot | string | 父物品的槽位名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ItemDefineID | 附加在此槽位上的子物品 DefineID |  |

### GetAttachChildrenItem

获取所有附加在物品上的子物品
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AttachParentID | ItemDefineID | 父物品的 DefineID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ItemDefineID[] | 所有子物品 DefineID, 数组元素与父物品槽位一一对应，可能存在无效的 ItemDefineID |  |

### GetAttachAllowSlots

获取子物品可以 Attach 到父物品的哪些 Slot(不考虑槽位启用状态)
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AttachParentID | number | 父物品的 ItemID |  |
| AttachChildID | number | 子物品的 ItemID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string[] | 所有可装备槽位 FName |  |

### GetAttachAllowSlotsByDefineID

获取子物品可以 Attach 到父物品`实例` 的哪些 Slot(考虑槽位启用状态)
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | PlayerPawn | 玩家 |  |
| AttachParentDefineID | ItemDefineID | 父物品的 ItemDefineID |  |
| AttachChildID | number | 子物品的 ItemID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string[] | 所有可装备槽位 FName |  |

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

### GetBackpackSimpleNameV2

返回物品背包简述
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 物品背包简写 |  |

### GetBigQualityTexturePath

获取品质色的128*256纹理路径(废弃，结果同GetQualityTexturePath)
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

### GetEquipmentQualityTexturePath

获取装备品质色条纹理路径
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QualityRank | number | 品质等级 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 品质纹理路径string |  |

### GetWeaponSlotAttachItemIDs

获取武器配件槽位可用配件的物品ID
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 武器的物品ID |  |
| SlotName | string | 武器槽位名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number[] | 可用的配件物品ID |  |

### GetPickupWrapperListByItemID

根据物品ID查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AUGCPickUpWrapperActor[] | 拾取物列表 |  |

### GetPickupWrapperListByCustomType

根据自定义类型查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CustomType | string | 自定义类型 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AUGCPickUpWrapperActor[] | 拾取物列表 |  |

### GetPickupWrapperListByItemTag

根据物品Tag查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemTag | string | 物品Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AUGCPickUpWrapperActor[] | 拾取物列表 |  |

### SetEquipSlotEnable

启用物品槽位
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefineID | FItemDefineID | 物品DefineID | cppstruct/detail/FItemDefineID.json |
| SlotName | string | 槽位名 |  |

### GetEquipSlotEnable

获取物品槽位是否启用
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefineID | FItemDefineID | 物品DefineID | cppstruct/detail/FItemDefineID.json |
| SlotName | string | 槽位名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否启用 |  |

### StartCustomizeDrop

指定掉落方案进行一次 Wrapper 掉落
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DropLocation | FVector | 掉落中心点 | cppstruct/detail/FVector.json |
| ProduceID | number | 掉落方案ID |  |
| ProduceGroupID | number | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |  |
| EntityType | EUGCGenerateItemEntityType | 掉落物类型(可缺省，默认为Wrapper) |  |
| RelatedPlayer | PlayerPawn | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为nil |  |
| DropActorClass | UClass | 掉落主体Actor类型，应继承自 UGCDropActor_BP, 可以为nil。通过创建自定义蓝图，配置掉落详细参数（掉落间隔、随机掉落范围等等）。 |  |

### FindAllNearPickupItemData

找到所有玩家角色附近的地面拾取物
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FUGCPickupItemData[] | 地面拾取物信息 |  |

### FindPickupWrapperActorByRange

查找指定距离范围内的地面拾取物
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Center | FVector | 中心点坐标 | cppstruct/detail/FVector.json |
| DistanceRange | number | 查找距离 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APickUpWrapperActor[] | 地面拾取物Actor |  |

### TryPickupWrapperItem

玩家角色尝试拾取地面物品（不播拾取动作）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerPawn | PlayerPawn | 玩家角色 |  |
| TargetWrapper | AActor | 目标地面拾取物 |  |
| ItemDefineID | FItemDefineID | 要拾取的物品 DefineID，可缺省，默认取 TargetWrapper 中的物品实例数据 | cppstruct/detail/FItemDefineID.json |
| PickupCount | number | 拾取数量，可缺省，默认拾取1个 |  |
| CheckPickupCondition | boolean | 是否检查拾取条件(距离、是否穿墙等)，可缺省，默认为 true |  |

### SpawnPickupWrapper

创建地面拾取物
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Location | FVector | 创建位置 | cppstruct/detail/FVector.json |
| ItemID | number | 拾取物物品ID |  |
| Count | number | 拾取物物品数量 |  |
| CustomData | table | 物品自定义实例化数据(可缺省，默认无自定义实例化数据) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APickUpWrapperActor | 地面拾取物Actor |  |

### GetUGCPickUpListComponent

获取拾取组件(客户端）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | PlayerPawn | PlayerController @玩家角色或者玩家控制器 | 玩家角色或者玩家控制器 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | @UUGCPickUpListComponent | UGC拾取组件组件 |  |

### PauseAutoPick

暂停指定物品的自动拾取
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemID | number | 物品 ID |  |
| InPlayer | PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取 | 可选，玩家角色或控制器，不传则自动获取 |  |

### StopPick

停止拾取（清空拾取列表，关闭数据更新）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPlayer | PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取 | 可选，玩家角色或控制器，不传则自动获取 |  |

### StartPick

开始拾取（开启数据更新）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPlayer | PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取 | 可选，玩家角色或控制器，不传则自动获取 |  |

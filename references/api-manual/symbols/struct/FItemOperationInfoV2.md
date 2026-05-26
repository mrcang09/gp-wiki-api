# FItemOperationInfoV2

- Symbol Type: struct
- Symbol Path: FItemOperationInfoV2
- Source JSON Path: cppstruct/detail/FItemOperationInfoV2.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FItemOperationInfoV2.json
- Mirrored At (UTC): 2026-05-19 08:24:41Z

---

## Description

V2背包操作事件信息

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefineID | FItemDefineID | 触发操作的物品 DefineID |  |
| ItemOperationType | EItemOperationTypeV2 | 触发的操作类型<br>	  <br>	  (SwapEquip 类型的操作将触发2次事件，分别对应两个物品) |  |
| CommonReason | uint8 | 触发操作时物品携带的通用 Reason |  |
| Count | int32 | 被操作的物品数量<br>	  添加、丢弃、移除时表示对应的数量<br>	  其它操作 Count 数量为 1 |  |
| TargetDefineID | FItemDefineID | Attach: 附加的物品 DefineID<br>	  Detach: 解除附加的物品 DefineID<br>	  SwapEquip: 与此物品交换的物品 DefineID<br>	  <br>	  其它操作类型此变量无意义 |  |
| TargetSlot | FName | Equip: 装备的目标槽位<br>	  UnEquip: 从哪个槽位卸下<br>	  Attach: 附加物品的槽位<br>	  Detach: 解除附加物品的槽位<br>	  SwapEquip: 交换装备后物品的新槽位<br>	  <br>	  其它操作类型此变量无意义 |  |

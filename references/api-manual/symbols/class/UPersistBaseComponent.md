# UPersistBaseComponent

- Symbol Type: class
- Symbol Path: Others / UPersistBaseComponent
- Source JSON Path: class/detail/Others/UPersistBaseComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPersistBaseComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

技能Buff组件

## Functions

### RegisterPersistEffectWithSlot

生效范围：服务器
	  将PersistEffect注册到目标槽位中

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Slot | FGameplayTag  | 槽位 |  |
| InPE | UPersistEffectBase *  | 注册到槽位的PersistEffect |  |
| bShouldUnapply | bool | 是否将原来槽位上的PersistEffect进行Unapply |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 注册是否成功 |  |

### UnRegisterPersistEffectWithSlot

生效范围：服务器
	  将目标槽位中的PersistEffect解除注册

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Slot | FGameplayTag  | 槽位 |  |
| bShouldUnapply | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 解除注册是否成功 |  |

### GetPersistEffectBySlot

生效范围：服务器&客户端
	  获取目标槽位中的PersistEffect

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Slot | FGameplayTag | 槽位 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPersistEffectBase *  | 槽位上的PersistEffect |  |

# UGCSimpleCharacterSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 怪物系统 / UGCSimpleCharacterSystem
- Source JSON Path: class/detail/和平全局接口/怪物系统/UGCSimpleCharacterSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCSimpleCharacterSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

怪物小动物系统接口库

## Functions

### GetHealth

获取当前血量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 血量 |  |

### SetHealth

设置当前血量（不会超过血量最大值）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |
| Health | number | 血量 |  |

### GetHealthMax

获取当前最大血量
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 血量 |  |

### SetHealthMax

设置当前最大血量（当前血量不会随之变大，但如果超过最大血量，则会变小）
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |
| HealthMax | number | 最大血量 |  |

### GetSpeedScale

获取移动速度系数
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 移动系数 |  |

### SetSpeedScale

设置移动速度系数
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |
| SpeedScale | number | 移动系数 |  |

### IsInvincible

获取是否无敌
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否无敌 |  |

### SetInvincible

设置是否无敌
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |
| IsInvincible | boolean | 是否无敌 |  |

### IsAlive

获取是否存活
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimpleCharacter | ASTExtraSimpleCharacterBase | 小动物/ ASTExtraSimpleCharacter @怪物 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否存活 |  |

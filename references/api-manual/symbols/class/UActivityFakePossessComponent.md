# UActivityFakePossessComponent

- Symbol Type: class
- Symbol Path: Others / UActivityFakePossessComponent
- Source JSON Path: class/detail/Others/UActivityFakePossessComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UActivityFakePossessComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

能够将这个Actor的控制权传递给玩家的组件

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OnPossess | FFakePossesserChangeDelegate | 获取控制权事件事件委托<br>	 @param PC 获取到这个Actor控制权的PC |  |
| OnUnPossess | FFakePossesserChangeDelegate | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC |  |
| OnUnPossessWithReason | FFakeUnPossessDelegate | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC<br>	 @param Reason 解除控制权的原因 |  |

## Functions

### FakePossess

生效范围：S
	  让一个PlayerController控制这个Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PC | AController * | 获得控制权的PlayerController |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FakeUnPossess

生效范围：S
	  解除这个Actor上的PC的控制权

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reason | EUnPossessReason | 解除控制权的原因 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FakePossessWithAttach

生效范围：S
	  让一个PlayerController控制这个Actor，并将当前控制的角色Attach到这个Actor上

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PC | AController *  | 获得控制权的PlayerController |  |
| AttachScene | USceneComponent *  | Attach到的组件 |  |
| SocketName | FName  | Attach到的Socket |  |
| bMulticastToClient | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FakeUnPossessWithDettach

生效范围：S
	  解除这个Actor上的PC的控制权，并将角色从这个Actor上Detach

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reason | EUnPossessReason | 解除控制权的原因 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CanBePossess

生效范围：S
	  获取是否可以由这个Character控制当前Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Character | ASTExtraBaseCharacter * | 要检查的Character |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

# UPawnActionsComponent

- Symbol Type: class
- Symbol Path: Others / UPawnActionsComponent
- Source JSON Path: class/detail/Others/UPawnActionsComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPawnActionsComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControlledPawn | APawn * |  |  |
| ActionStacks | TArray < FPawnActionStack > |  |  |
| ActionEvents | TArray < FPawnActionEvent > |  |  |
| CurrentAction | UPawnAction * |  |  |

## Functions

### K2_PerformAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pawn | APawn *  |  |  |
| Action | UPawnAction *  |  |  |
| Priority | TEnumAsByte < EAIRequestPriority :: Type > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### K2_PushAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAction | UPawnAction *  |  |  |
| Priority | EAIRequestPriority :: Type  |  |  |
| Instigator | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### K2_AbortAction

Aborts given action instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionToAbort | UPawnAction * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPawnActionAbortState :: Type  |  |  |

### K2_ForceAbortAction

Aborts given action instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionToAbort | UPawnAction * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPawnActionAbortState :: Type  |  |  |

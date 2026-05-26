# UBehaviorTreeComponent

- Symbol Type: class
- Symbol Path: Others / UBehaviorTreeComponent
- Source JSON Path: class/detail/Others/UBehaviorTreeComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTreeComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NodeInstances | TArray < UBTNode * > | instanced nodes |  |

## Functions

### GetTagCooldownEndTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CooldownTag | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | the cooldown tag end time, 0.0f if CooldownTag is not found |  |

### AddCooldownTagDuration

add to the cooldown tag's duration

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CooldownTag | FGameplayTag  |  |  |
| CooldownDuration | float  |  |  |
| bAddToExistingDuration | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDynamicSubtree

assign subtree to RunBehaviorDynamic task specified by tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InjectTag | FGameplayTag  |  |  |
| BehaviorAsset | UBehaviorTree * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetUGCMobBTDebugInfo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutTreeInfo | FUGCMobBTDebugInfo &  |  |  |
| OutBlackBoardInfo | TArray < FUGCMobBTBlackBoardInfo > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

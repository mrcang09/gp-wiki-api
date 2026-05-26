# UBTCondition_LuaBase

- Symbol Type: class
- Symbol Path: Others / UBTCondition_LuaBase
- Source JSON Path: class/detail/Others/UBTCondition_LuaBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTCondition_LuaBase.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Base class for lua based condition nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and attachments, condition have two execution chains:
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsConditionExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsConditionObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIOwner | AAIController * | Cached AIController owner of BehaviorTreeComponent. |  |
| ObservedKeyNames | TArray < FName > | blackboard key names that should be observed |  |
| bCheckConditionOnlyBlackBoardChanges | uint32 | Applies only if Condition has any FBlackboardKeySelector property and if condition is<br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes<br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |  |
| bIsObservingBB | uint32 | gets set to true if condition declared BB keys it can potentially observe |  |

## Functions

### ReceiveTickAI

tick function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn *  |  |  |
| DeltaSeconds | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveExecutionStartAI

called on execution of underlying node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveExecutionFinishAI

called when execution of underlying node is finished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn *  |  |  |
| NodeResult | EBTNodeResult :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveObserverActivatedAI

called when observer is activated (flow controller)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveObserverDeactivatedAI

called when observer is deactivated (flow controller)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PerformConditionCheckAI

called when testing if underlying node can be executed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsConditionExecutionActive

check if condition is part of currently active branch

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsConditionObserverActive

check if condition's observer is currently active

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

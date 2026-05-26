# UBTDecorator_BlueprintBase

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_BlueprintBase
- Source JSON Path: class/detail/Others/UBTDecorator_BlueprintBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_BlueprintBase.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and services, decorator have two execution chains: 
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIOwner | AAIController * | Cached AIController owner of BehaviorTreeComponent. |  |
| ActorOwner | AActor * | Cached AIController owner of BehaviorTreeComponent. |  |
| ObservedKeyNames | TArray < FName > | blackboard key names that should be observed |  |
| bShowPropertyDetails | uint32 | show detailed information about properties |  |
| bCheckConditionOnlyBlackBoardChanges | uint32 | Applies only if Decorator has any FBlackboardKeySelector property and if decorator is <br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes <br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |  |
| bIsObservingBB | uint32 | gets set to true if decorator declared BB keys it can potentially observe |  |

## Functions

### ReceiveTick

tick function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor *  |  |  |
| DeltaSeconds | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveExecutionStart

called on execution of underlying node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveExecutionFinish

called when execution of underlying node is finished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor *  |  |  |
| NodeResult | EBTNodeResult :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveObserverActivated

called when observer is activated (flow controller)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveObserverDeactivated

called when observer is deactivated (flow controller)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PerformConditionCheck

called when testing if underlying node can be executed, must call FinishConditionCheck

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ReceiveTickAI

Alternative AI version of ReceiveTick

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

Alternative AI version of ReceiveExecutionStart

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

Alternative AI version of ReceiveExecutionFinish

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

Alternative AI version of ReceiveObserverActivated

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

Alternative AI version of ReceiveObserverDeactivated

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

Alternative AI version of ReceiveConditionCheck

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsDecoratorExecutionActive

check if decorator is part of currently active branch

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsDecoratorObserverActive

check if decorator's observer is currently active

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

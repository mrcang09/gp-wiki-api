# UBTService_BlueprintBase

- Symbol Type: class
- Symbol Path: Others / UBTService_BlueprintBase
- Source JSON Path: class/detail/Others/UBTService_BlueprintBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTService_BlueprintBase.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!
 
   When service receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIOwner | AAIController * | Cached AIController owner of BehaviorTreeComponent. |  |
| ActorOwner | AActor * | Cached actor owner of BehaviorTreeComponent. |  |
| bShowPropertyDetails | uint32 | show detailed information about properties |  |
| bShowEventDetails | uint32 | show detailed information about implemented events |  |

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

### ReceiveSearchStart

task search enters branch of tree

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActivation

service became active

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveDeactivation

service became inactive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveTickAI

Alternative AI version of ReceiveTick function.

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

### ReceiveSearchStartAI

Alternative AI version of ReceiveSearchStart function.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveActivationAI

Alternative AI version of ReceiveActivation function.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveDeactivationAI

Alternative AI version of ReceiveDeactivation function.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsServiceActive

check if service is currently being active

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

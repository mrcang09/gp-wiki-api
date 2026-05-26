# UBTTask_LuaBase

- Symbol Type: class
- Symbol Path: Others / UBTTask_LuaBase
- Source JSON Path: class/detail/Others/UBTTask_LuaBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_LuaBase.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Base class for lua based task nodes. Do NOT use it for creating native c++ classes!
 
   When task receives Abort event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Execute, but does not handle external events.
   Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIOwner | AAIController * | Cached AIController owner of BehaviorTreeComponent. |  |
| bShowPropertyDetails | uint32 | show detailed information about properties |  |

## Functions

### ReceiveExecuteAI

entry point, task will stay active until FinishExecute is called.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveAbortAI

if blueprint graph contains this event, task will stay active until FinishAbort is called

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

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

### FinishExecute

finishes task execution with Success or Fail result

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bSuccess | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FinishAbort

aborts task execution

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetFinishOnMessage

task execution will be finished (with result 'Success') after receiving specified message

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MessageName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFinishOnMessageWithId

task execution will be finished (with result 'Success') after receiving specified message with indicated ID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MessageName | FName  |  |  |
| RequestID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsTaskExecuting

check if task is currently being executed

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsTaskAborting

check if task is currently being aborted

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

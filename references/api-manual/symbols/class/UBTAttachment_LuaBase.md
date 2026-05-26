# UBTAttachment_LuaBase

- Symbol Type: class
- Symbol Path: Others / UBTAttachment_LuaBase
- Source JSON Path: class/detail/Others/UBTAttachment_LuaBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTAttachment_LuaBase.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Base class for lua based Attachment nodes. Do NOT use it for creating native c++ classes!
 
   When Attachment receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsAttachmentActive() when in doubt.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AIOwner | AAIController * | Cached AIController owner of BehaviorTreeComponent. |  |

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

### ReceiveSearchStartAI

task search enters branch of tree

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

attachment became active

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

attachment became inactive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OwnerController | AAIController *  |  |  |
| ControlledPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsAttachmentActive

check if attachment is currently being active

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

# UBrainComponent

- Symbol Type: class
- Symbol Path: Others / UBrainComponent
- Source JSON Path: class/detail/Others/UBrainComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBrainComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlackboardComp | UBlackboardComponent * | blackboard component |  |
| AIOwner | AAIController * |  |  |

## Functions

### RestartLogic

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopLogic

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reason | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PauseLogic

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reason | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResumeLogic

MUST be called by child implementations!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reason | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EAILogicResuming :: Type  | indicates whether child class' ResumeLogic should be called (true) or has it been  |  |

### IsRunning

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsPaused

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

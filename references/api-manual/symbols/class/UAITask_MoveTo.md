# UAITask_MoveTo

- Symbol Type: class
- Symbol Path: Others / UAITask_MoveTo
- Source JSON Path: class/detail/Others/UAITask_MoveTo.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAITask_MoveTo.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OnRequestFailed | FGenericGameplayTaskDelegate |  |  |
| MoveRequest | FAIMoveRequest | parameters of move request |  |

## Functions

### AIMoveTo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AAIController *  |  |  |
| GoalLocation | FVector  |  |  |
| GoalActor | AActor *  |  |  |
| AcceptanceRadius | float  |  |  |
| StopOnOverlap | EAIOptionFlag :: Type  |  |  |
| AcceptPartialPath | EAIOptionFlag :: Type  |  |  |
| bUsePathfinding | bool  |  |  |
| bLockAILogic | bool  |  |  |
| bUseContinuosGoalTracking | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAITask_MoveTo *  |  |  |

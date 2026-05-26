# UCrowdFollowingComponent

- Symbol Type: class
- Symbol Path: Others / UCrowdFollowingComponent
- Source JSON Path: class/detail/Others/UCrowdFollowingComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCrowdFollowingComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CrowdAgentMoveDirection | FVector |  |  |
| CharacterMovement | UCharacterMovementComponent * |  |  |
| AvoidanceGroup_DEPRECATED | FNavAvoidanceMask | DEPRECATED: Group mask for this agent - use property from CharacterMovementComponent instead |  |
| GroupsToAvoid_DEPRECATED | FNavAvoidanceMask | DEPRECATED: Will avoid other agents if they are in one of specified groups - use property from CharacterMovementComponent instead |  |
| GroupsToIgnore_DEPRECATED | FNavAvoidanceMask | DEPRECATED: Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid - use property from CharacterMovementComponent instead |  |

## Functions

### SuspendCrowdSteering

master switch for crowd steering & avoidance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bSuspend | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

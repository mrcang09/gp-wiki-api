# UNavMovementComponent

- Symbol Type: class
- Symbol Path: Others / UNavMovementComponent
- Source JSON Path: class/detail/Others/UNavMovementComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UNavMovementComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NavAgentProps | FNavAgentProperties | Properties that define how the component can move. |  |
| FixedPathBrakingDistance | float | Braking distance override used with acceleration driven path following (bUseAccelerationForPaths) |  |
| bUpdateNavAgentWithOwnersCollision | uint32 | If set to true NavAgentProps' radius and height will be updated with Owner's collision capsule size |  |
| bUseAccelerationForPaths | uint32 | If set, pathfollowing will control character movement via acceleration values. If false, it will set velocities directly. |  |
| bUseFixedBrakingDistanceForPaths | uint32 | If set, FixedPathBrakingDistance will be used for path following deceleration |  |
| MovementState | FMovementProperties | Expresses runtime state of character's movement. Put all temporal changes to movement properties here |  |

## Functions

### StopActiveMovement

Stops applying further movement (usually zeros acceleration).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopMovementKeepPathing

Stops movement immediately (reset velocity) but keeps following current path

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsCrouching

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if currently crouching |  |

### IsFalling

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if currently falling (not flying, in a non-fluid volume, and not on the ground) |  |

### IsMovingOnGround

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if currently moving on the ground (e.g. walking or driving) |  |

### IsSwimming

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if currently swimming (moving through a fluid volume) |  |

### IsFlying

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if currently flying (moving through a non-fluid volume without resting on the ground) |  |

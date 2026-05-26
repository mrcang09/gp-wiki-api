# UPathFollowingComponent

- Symbol Type: class
- Symbol Path: Others / UPathFollowingComponent
- Source JSON Path: class/detail/Others/UPathFollowingComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPathFollowingComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MovementComp | UNavMovementComponent * | associated movement component |  |
| MyNavData | ANavigationData * | navigation data for agent described in movement component |  |

## Functions

### OnActorBump

called when moving agent collides with another actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SelfActor | AActor *  |  |  |
| OtherActor | AActor *  |  |  |
| NormalImpulse | FVector  |  |  |
| Hit | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPathActionType

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPathFollowingAction :: Type |  |  |

### GetPathDestination

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### OnNavDataRegistered

called when NavigationSystem registers new navigation data type while this component
	 	instance has empty MyNavData. This is usually the case for AI agents hand-placed
	 	on levels.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NavData | ANavigationData * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

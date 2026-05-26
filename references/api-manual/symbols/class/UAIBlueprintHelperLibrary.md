# UAIBlueprintHelperLibrary

- Symbol Type: class
- Symbol Path: Others / UAIBlueprintHelperLibrary
- Source JSON Path: class/detail/Others/UAIBlueprintHelperLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAIBlueprintHelperLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Functions

### CreateMoveToProxyObject

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Pawn | APawn *  |  |  |
| Destination | FVector  |  |  |
| TargetActor | AActor *  |  |  |
| AcceptanceRadius | float  |  |  |
| bStopOnOverlap | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAIAsyncTaskBlueprintProxy *  |  |  |

### SendAIMessage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APawn *  |  |  |
| Message | FName  |  |  |
| MessageSource | UObject *  |  |  |
| bSuccess | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnAIFromClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PawnClass | TSubclassOf < APawn >  |  |  |
| BehaviorTree | UBehaviorTree *  |  |  |
| Location | FVector  |  |  |
| Rotation | FRotator  |  |  |
| bNoCollisionFail | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn *  |  |  |

### GetAIController

The way it works exactly is if the actor passed in is a pawn, then the function retrieves 
	 	pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControlledActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AAIController *  |  |  |

### GetBlackboard

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UBlackboardComponent *  |  |  |

### LockAIResourcesWithAnimation

locks indicated AI resources of animated pawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimInstance | UAnimInstance *  |  |  |
| bLockMovement | bool  |  |  |
| LockAILogic | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnlockAIResourcesWithAnimation

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimInstance | UAnimInstance *  |  |  |
| bUnlockMovement | bool  |  |  |
| UnlockAILogic | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsValidAILocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Location | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValidAIDirection

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DirectionVector | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValidAIRotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Rotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetCurrentPath

Returns a copy of navigation path given controller is currently using. 
	 	The result being a copy means you won't be able to influence agent's pathfollowing 
	 	by manipulating received path

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UNavigationPath *  |  |  |

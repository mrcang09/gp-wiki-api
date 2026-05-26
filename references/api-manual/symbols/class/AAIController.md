# AAIController

- Symbol Type: class
- Symbol Path: Others / AAIController
- Source JSON Path: class/detail/Others/AAIController.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AAIController.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

AIController is the base class of controllers for AI-controlled Pawns.
  
  Controllers are non-physical actors that can be attached to a pawn to control its actions.
  AIControllers manage the artificial intelligence for the pawns they control.
  In networked games, they only exist on the server.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bStopAILogicOnUnposses | uint32 | By default AI's logic gets stopped when controlled Pawn is unpossesed. Setting this flag to false<br>	 	will make AI logic persist past loosing controll over a pawn |  |
| bSkipExtraLOSChecks | uint32 | Skip extra line of sight traces to extremities of target being checked. |  |
| bAllowStrafe | uint32 | Is strafing allowed during movement? |  |
| bWantsPlayerState | uint32 | Specifies if this AI wants its own PlayerState. |  |
| bSetControlRotationFromPawnOrientation | uint32 | Copy Pawn rotation to ControlRotation, if there is no focus point. |  |
| PathFollowingComponent | UPathFollowingComponent * | Component used for moving along a path. |  |
| BrainComponent | UBrainComponent * | Component responsible for behaviors. |  |
| PerceptionComponent | UAIPerceptionComponent * |  |  |
| ActionsComp | UPawnActionsComponent * |  |  |
| Blackboard | UBlackboardComponent * | blackboard |  |
| CachedGameplayTasksComponent | UGameplayTasksComponent * |  |  |
| DefaultNavigationFilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

## Functions

### OnPossess

Event called when PossessedPawn is possessed by this controller.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PossessedPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnUnpossess

Gets triggered after given pawn has been unpossesed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UnpossessedPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MoveToActor

Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Goal | AActor *  |  |  |
| AcceptanceRadius | float  | - finish move if pawn gets close enough |  |
| bStopOnOverlap | bool  | - add pawn's radius to AcceptanceRadius |  |
| bUsePathfinding | bool  | - use navigation data to calculate path (otherwise it will go in straight line) |  |
| bCanStrafe | bool  | - set focus related flag: bAllowStrafe |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |  |
| bAllowPartialPath | bool | - use incomplete path when goal can't be reached |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPathFollowingRequestResult :: Type  |  |  |

### MoveToLocation

Makes AI go toward specified Dest location, aborts any active path following

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Dest | FVector &  |  |  |
| AcceptanceRadius | float  | - finish move if pawn gets close enough |  |
| bStopOnOverlap | bool  | - add pawn's radius to AcceptanceRadius |  |
| bUsePathfinding | bool  | - use navigation data to calculate path (otherwise it will go in straight line) |  |
| bProjectDestinationToNavigation | bool  | - project location on navigation data before using it |  |
| bCanStrafe | bool  | - set focus related flag: bAllowStrafe |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |  |
| bAllowPartialPath | bool  | - use incomplete path when goal can't be reached |  |
| bUseNavLink | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPathFollowingRequestResult :: Type  |  |  |

### GetMoveStatus

Returns status of path following

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPathFollowingStatus :: Type |  |  |

### HasPartialPath

Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetImmediateMoveDestination

Returns position of current path segment's end.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetMoveBlockDetection

Updates state of movement block detection.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RunBehaviorTree

Starts executing behavior tree.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BTAsset | UBehaviorTree * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UseBlackboard

Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlackboardAsset | UBlackboardData *  |  The Blackboard asset to use. |  |
| BlackboardComponent | UBlackboardComponent * & | The Blackboard component that was used or created to work with the passed-in Blackboard Asset. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if we successfully linked the blackboard asset to the blackboard component. |  |

### ClaimTaskResource

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ResourceClass | TSubclassOf < UGameplayTaskResource > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnclaimTaskResource

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ResourceClass | TSubclassOf < UGameplayTaskResource > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnUsingBlackBoard

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BlackboardComp | UBlackboardComponent *  |  |  |
| BlackboardAsset | UBlackboardData * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFocalPoint

Retrieve the final position that controller should be looking at.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### GetFocalPointOnActor

Retrieve the focal point this controller should focus to on given actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### K2_SetFocalPoint

Set the position that controller should be looking at.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FP | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetFocus

Set Focus for actor, will set FocalPoint as a result.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFocus | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFocusActor

Get the focused actor.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### K2_ClearFocus

Clears Focus, will also clear FocalPoint as a result

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnGameplayTaskResourcesClaimed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewlyClaimed | FGameplayResourceSet  |  |  |
| FreshlyReleased | FGameplayResourceSet |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPathFollowingComponent

Returns PathFollowingComponent subobject

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPathFollowingComponent * |  |  |

### GetAIPerceptionComponent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UAIPerceptionComponent * |  |  |

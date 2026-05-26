# UNavigationSystem

- Symbol Type: class
- Symbol Path: Others / UNavigationSystem
- Source JSON Path: class/detail/Others/UNavigationSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UNavigationSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MainNavData | ANavigationData * |  |  |
| AbstractNavData | ANavigationData * | special navigation data for managing direct paths, not part of NavDataSet! |  |
| CrowdManagerClass | TSubclassOf < UCrowdManagerBase > |  |  |
| bAutoCreateNavigationData | uint32 | Should navigation system spawn default Navigation Data when there's none and there are navigation bounds present? |  |
| bAllowClientSideNavigation | uint32 |  |  |
| bSupportRebuilding | uint32 | gets set to true if gathering navigation data (like in navoctree) is required due to the need of navigation generation<br>	 	Is always true in Editor Mode. In other modes it depends on bRebuildAtRuntime of every required NavigationData class' CDO |  |
| ObstacleManagerClassPath | FSoftClassPath |  |  |
| bInitialBuildingLocked | uint32 | if set to true will result navigation system not rebuild navigation until<br>	 	a call to ReleaseInitialBuildingLock() is called. Does not influence<br>	 	editor-time generation (i.e. does influence PIE and Game).<br>	 	Defaults to false. |  |
| bWholeWorldNavigable | uint32 | If set to true (default) navigation will be generated only within special navigation<br>	 	bounds volumes (like ANavMeshBoundsVolume). Set to false means navigation should be generated<br>	 	everywhere. |  |
| bSkipAgentHeightCheckWhenPickingNavData | uint32 | false by default, if set to true will result in not caring about nav agent height<br>	 	when trying to match navigation data to passed in nav agent |  |
| DataGatheringMode | ENavDataGatheringModeConfig |  |  |
| bGenerateNavigationOnlyAroundNavigationInvokers | uint32 | If set to true navigation will be generated only around registered "navigation enforcers"<br>		This has a range of consequences (including how navigation octree operates) so it needs to<br>		be a conscious decision.<br>		Once enabled results in whole world being navigable.<br>		@see RegisterNavigationInvoker |  |
| ActiveTilesUpdateInterval | float | Minimal time, in seconds, between active tiles set update |  |
| SupportedAgents | TArray < FNavDataConfig > |  |  |
| DirtyAreasUpdateFreq | float | update frequency for dirty areas on navmesh |  |
| NavDataSet | TArray < ANavigationData * > |  |  |
| NavDataRegistrationQueue | TArray < ANavigationData * > |  |  |
| OperationMode | FNavigationSystemRunMode |  |  |

## Functions

### BP_ChangeRecastPartitioning

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName  |  |  |
| High | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BP_BuildOne

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BP_DynamicBuildOne

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BP_Build

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BP_AddDynamicNavAffect

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName  |  |  |
| InBounds | FBox & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BP_IncrementalBuild

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BP_CancelBuild

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BP_GetNavigationData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ANavigationData *  |  |  |

### GetNavigationSystem

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UNavigationSystem *  |  |  |

### K2_ProjectPointToNavigation

Project a point onto the NavigationData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Point | FVector &  |  |  |
| ProjectedLocation | FVector &  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  |  |  |
| QueryExtent | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### K2_GetRandomReachablePointInRadius

Generates a random location reachable from given Origin location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector &  |  |  |
| RandomLocation | FVector &  |  |  |
| Radius | float  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  |  |  |
| ExtentRadius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Return Value represents if the call was successful |  |

### K2_GetRandomPointInNavigableRadius

Generates a random location in navigable space within given radius of Origin.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector &  |  |  |
| RandomLocation | FVector &  |  |  |
| Radius | float  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Return Value represents if the call was successful |  |

### GetPathCost

Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PathStart | FVector &  |  |  |
| PathEnd | FVector &  |  |  |
| PathCost | float &  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENavigationQueryResult :: Type  |  |  |

### GetPathLength

Potentially expensive. Use with caution

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PathStart | FVector &  |  |  |
| PathEnd | FVector &  |  |  |
| PathLength | float &  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENavigationQueryResult :: Type  |  |  |

### IsNavigationBeingBuilt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsNavigationBeingBuiltOrLocked

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SimpleMoveToActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController *  |  |  |
| Goal | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SimpleMoveToLocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController *  |  |  |
| Goal | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FindPathToLocationSynchronously

Finds path instantly, in a FindPath Synchronously.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PathStart | FVector &  |  |  |
| PathEnd | FVector &  |  |  |
| PathfindingContext | AActor *  | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UNavigationPath *  |  |  |

### FindPathToActorSynchronously

Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
	 	the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PathStart | FVector &  |  |  |
| GoalActor | AActor *  |  |  |
| TetherDistance | float  |  |  |
| PathfindingContext | AActor *  | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UNavigationPath *  |  |  |

### NavigationRaycast

Performs navigation raycast on NavigationData appropriate for given Querier.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| RayStart | FVector &  |  |  |
| RayEnd | FVector &  |  |  |
| HitLocation | FVector &  | if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  |  |  |
| Querier | AController * | if not passed default navigation data will be used |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if line from RayStart to RayEnd was obstructed. Also, true when no navigation data present |  |

### SetMaxSimultaneousTileGenerationJobsCount

will limit the number of simultaneously running navmesh tile generation jobs to specified number.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaxNumberOfJobs | int32 | gets trimmed to be at least 1. You cannot use this function to pause navmesh generation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetMaxSimultaneousTileGenerationJobsCount

Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RegisterNavigationInvoker

Registers given actor as a "navigation enforcer" which means navigation system will
	 	make sure navigation is being generated in specified radius around it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Invoker | AActor *  |  |  |
| TileGenerationRadius | float  |  |  |
| TileRemovalRadius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnregisterNavigationInvoker

Removes given actor from the list of active navigation enforcers.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Invoker | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetGeometryGatheringMode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMode | ENavDataGatheringModeConfig |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnNavigationBoundsUpdated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NavVolume | ANavMeshBoundsVolume * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ProjectPointToNavigation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Point | FVector &  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter >  |  |  |
| QueryExtent | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRandomReachablePointInRadius

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector &  |  |  |
| Radius | float  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRandomPointInNavigableRadius

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector &  |  |  |
| Radius | float  |  |  |
| NavData | ANavigationData *  |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### UpdateDynamicGenerateTargetNav

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsAdd | bool  |  |  |
| GenerateTargetNav | FDynamicGenerateTargetNavigation |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UNavLocalGridManager

- Symbol Type: class
- Symbol Path: Others / UNavLocalGridManager
- Source JSON Path: class/detail/Others/UNavLocalGridManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UNavLocalGridManager.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Manager for local navigation grids
  
   Builds non overlapping grid from multiple sources, that can be used later for pathfinding.
   Check also: UGridPathFollowingComponent, FNavLocalGridData

## Functions

### SetLocalNavigationGridDensity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| CellSize | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### AddLocalNavigationGridForPoint

creates new grid data for single point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Location | FVector &  |  |  |
| Radius2D | int32  |  |  |
| Height | float  |  |  |
| bRebuildGrids | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### AddLocalNavigationGridForPoints

creates single grid data for set of points

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Locations | TArray < FVector > &  |  |  |
| Radius2D | int32  |  |  |
| Height | float  |  |  |
| bRebuildGrids | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### AddLocalNavigationGridForBox

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Location | FVector &  |  |  |
| Extent | FVector  |  |  |
| Rotation | FRotator  |  |  |
| Radius2D | int32  |  |  |
| Height | float  |  |  |
| bRebuildGrids | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### AddLocalNavigationGridForCapsule

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Location | FVector &  |  |  |
| CapsuleRadius | float  |  |  |
| CapsuleHalfHeight | float  |  |  |
| Radius2D | int32  |  |  |
| Height | float  |  |  |
| bRebuildGrids | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RemoveLocalNavigationGrid

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| GridId | int32  |  |  |
| bRebuildGrids | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FindLocalNavigationGridPath

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector &  |  |  |
| End | FVector &  |  |  |
| PathPoints | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

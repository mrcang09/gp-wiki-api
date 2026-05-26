# UHierarchicalInstancedStaticMeshComponent

- Symbol Type: class
- Symbol Path: Others / UHierarchicalInstancedStaticMeshComponent
- Source JSON Path: class/detail/Others/UHierarchicalInstancedStaticMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UHierarchicalInstancedStaticMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SortedInstances | TArray < int32 > |  |  |
| NumBuiltInstances | int32 |  |  |
| BuiltInstanceBounds | FBox |  |  |
| UnbuiltInstanceBounds | FBox |  |  |
| UnbuiltInstanceBoundsList | TArray < FBox > |  |  |
| UnbuiltInstanceIndexList | TArray < int32 > |  |  |
| bEnableDensityScaling | uint32 |  |  |
| OcclusionLayerNumNodes | int32 |  |  |
| CacheMeshExtendedBounds | FBoxSphereBounds |  |  |
| bDisableCollision | bool |  |  |
| MinInstancesToSplitNode | int32 | Culling by Num |  |
| OptimiMinInstancesToSplitNode | int32 | Culling by Num For Optimization FClusterTree |  |
| IsOpenTreeOptimi | bool | Mark Use OptimiMinInstancesToSplitNode With FClusterTree |  |
| bEnableScaleOpt | bool |  |  |
| AverageScale | FVector |  |  |

## Functions

### RemoveInstances

Removes all the instances with indices specified in the InstancesToRemove array. Returns true on success.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstancesToRemove | TArray < int32 > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

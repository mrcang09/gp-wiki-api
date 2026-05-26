# UGridVisibilityCaptureComponent

- Symbol Type: class
- Symbol Path: Others / UGridVisibilityCaptureComponent
- Source JSON Path: class/detail/Others/UGridVisibilityCaptureComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGridVisibilityCaptureComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FOVAngle | float | Camera field of view (in degrees). |  |
| CaptureViewSize | FIntPoint |  |  |
| NearClipPlane | float |  |  |
| GridMesh | UStaticMesh * |  |  |
| GridMeshSizeScale | FVector |  |  |
| GridMeshLocationOffset | FVector |  |  |
| bForceLowestLOD | uint32 |  |  |
| bHiddenFoliage | uint32 |  |  |
| OcclusionDepthDiffThreshold | float |  |  |
| bShouldRenderGridMeshInMainPass | uint32 |  |  |
| MaxNumProcessWaitingResultCmdsPerFrame | int32 |  |  |
| MaxNumProcessWaitingCalculateCmdsPerFrame | int32 |  |  |
| GridSize | FIntPoint |  |  |
| RenderTargetToCreateRenderer | UTextureRenderTarget2D * |  |  |
| GridMeshComp | UInstancedStaticMeshComponent * |  |  |

## Functions

### InitGridIDVisibilityCalculation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InGridLocations | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CalculateGridIDVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GridID | int32  |  |  |
| CameraLocations | TArray < FGridVisibilityCameraInfo > &  |  |  |
| PotentialGrids | TArray < int32 > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FinishGridIDVisibilityCalculation

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

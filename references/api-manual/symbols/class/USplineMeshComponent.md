# USplineMeshComponent

- Symbol Type: class
- Symbol Path: Others / USplineMeshComponent
- Source JSON Path: class/detail/Others/USplineMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USplineMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A Spline Mesh Component is a derivation of a Static Mesh Component which can be deformed using a spline. Only a start and end position (and tangent) can be specified.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SplineParams | FSplineMeshParams | Spline that is used to deform mesh |  |
| SplineUpDir | FVector | Axis (in component space) that is used to determine X axis for co-ordinates along spline |  |
| bAllowSplineEditingPerInstance | uint32 | If true, spline keys may be edited per instance in the level viewport. Otherwise, the spline should be initialized in the construction script. |  |
| bSmoothInterpRollScale | uint32 | If true, will use smooth interpolation (ease inout) for Scale, Roll, and Offset along this section of spline. If false, uses linear |  |
| ForwardAxis | TEnumAsByte < ESplineMeshAxis :: Type > | Chooses the forward axis for the spline mesh orientation |  |
| SplineBoundaryMin | float | Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds |  |
| SplineBoundaryMax | float | Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds |  |
| BodySetup | UBodySetup * |  |  |
| CachedMeshBodySetupGuid | FGuid |  |  |
| bMeshDirty | uint32 |  |  |
| bHasBeenBakedWithLandcape | uint32 |  |  |

## Functions

### UpdateMesh

Update the collision and render state on the spline mesh following changes to its geometry

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetStartPosition

Get the start position of spline in local space

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetStartPosition

Set the start position of spline in local space

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartPos | FVector  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStartTangent

Get the start tangent vector of spline in local space

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetStartTangent

Set the start tangent vector of spline in local space

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartTangent | FVector  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEndPosition

Get the end position of spline in local space

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetEndPosition

Set the end position of spline in local space

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndPos | FVector  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEndTangent

Get the end tangent vector of spline in local space

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetEndTangent

Set the end tangent vector of spline in local space

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndTangent | FVector  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStartAndEnd

Set the start and end, position and tangent, all in local space

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartPos | FVector  |  |  |
| StartTangent | FVector  |  |  |
| EndPos | FVector  |  |  |
| EndTangent | FVector  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStartScale

Get the start scaling

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetStartScale

Set the start scaling

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartScale | FVector2D  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStartRoll

Get the start roll

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetStartRoll

Set the start roll

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartRoll | float  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetStartOffset

Get the start offset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetStartOffset

Set the start offset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartOffset | FVector2D  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEndScale

Get the end scaling

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetEndScale

Set the end scaling

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndScale | FVector2D  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEndRoll

Get the end roll

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetEndRoll

Set the end roll

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndRoll | float  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEndOffset

Get the end offset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### SetEndOffset

Set the end offset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndOffset | FVector2D  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetForwardAxis

Get the forward axis

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESplineMeshAxis :: Type |  |  |

### SetForwardAxis

Set the forward axis

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForwardAxis | ESplineMeshAxis :: Type  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSplineUpDir

Get the spline up direction

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### SetSplineUpDir

Set the spline up direction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSplineUpDir | FVector &  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoundaryMin

Get the boundary min

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetBoundaryMin

Set the boundary min

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoundaryMin | float  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoundaryMax

Get the boundary max

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetBoundaryMax

Set the boundary max

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBoundaryMax | float  |  |  |
| bUpdateMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

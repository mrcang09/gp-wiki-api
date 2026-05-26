# USplineComponent

- Symbol Type: class
- Symbol Path: Others / USplineComponent
- Source JSON Path: class/detail/Others/USplineComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USplineComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SplineCurves | FSplineCurves |  |  |
| SplineInfo_DEPRECATED | FInterpCurveVector | Deprecated - please use GetSplinePointsPosition() to fetch this FInterpCurve |  |
| SplineRotInfo_DEPRECATED | FInterpCurveQuat | Deprecated - please use GetSplinePointsRotation() to fetch this FInterpCurve |  |
| SplineScaleInfo_DEPRECATED | FInterpCurveVector | Deprecated - please use GetSplinePointsScale() to fetch this FInterpCurve |  |
| SplineReparamTable_DEPRECATED | FInterpCurveFloat |  |  |
| bAllowSplineEditingPerInstance_DEPRECATED | bool |  |  |
| ReparamStepsPerSegment | int32 | Number of steps per spline segment to place in the reparameterization table |  |
| Duration | float | Specifies the duration of the spline in seconds |  |
| bStationaryEndpoints | bool | Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors. |  |
| bSplineHasBeenEdited | bool | Whether the spline has been edited from its default by the spline component visualizer |  |
| bModifiedByConstructionScript | bool | Whether the UCS has made changes to the spline points |  |
| bInputSplinePointsToConstructionScript | bool | Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.<br>	  If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor. |  |
| bDrawDebug | bool | If true, the spline will be rendered if the Splines showflag is set. |  |
| bClosedLoop | bool | Whether the spline is to be considered as a closed loop.<br>	  Use SetClosedLoop() to set this property, and IsClosedLoop() to read it. |  |
| bLoopPositionOverride | bool |  |  |
| LoopPosition | float |  |  |
| DefaultUpVector | FVector | Default up vector in local space to be used when calculating transforms along the spline |  |
| bUseConfigRotation | bool | Engine Modify Start |  |
| bUseConfigRotationXY | bool |  |  |
| EditorUnselectedSplineSegmentColor | FLinearColor | Engine Modify End<br>	 <br>	 Color of an unselected spline component segment in the editor |  |
| EditorSelectedSplineSegmentColor | FLinearColor | Color of a selected spline component segment in the editor |  |
| bAllowDiscontinuousSpline | bool | Whether the spline's leave and arrive tangents can be different |  |
| bShouldVisualizeScale | bool | Whether scale visualization should be displayed |  |
| ScaleVisualizationWidth | float | Width of spline in editor for use with scale visualization |  |
| PostionModifyer | USplineComponentEditorModifer * |  |  |
| SelectedIndexs | TSet < int32 > |  |  |
| SnappingType | ESplineSnappingType |  |  |
| SnapInterval | float |  |  |
| SnapTopDownRange | FVector2D |  |  |
| TraceLength | float |  |  |

## Functions

### UpdateSpline

Update the spline tangents and SplineReparamTable

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetDistanceAlongSplineAtSplineInputKey

Get distance along the spline at the provided input key value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InKey | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SetUnselectedSplineSegmentColor

Specify unselected spline component segment color in the editor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SegmentColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSelectedSplineSegmentColor

Specify selected spline component segment color in the editor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SegmentColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EditorSnapToGround

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EditorNormalizeSplineTangent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetDrawDebug

Specify whether this spline should be rendered when the EditorGame spline show flag is set

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bShow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetClosedLoop

Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInClosedLoop | bool  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetClosedLoopAtPosition

Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInClosedLoop | bool  |  |  |
| Key | float  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsClosedLoop

Check whether the spline is a closed loop or not

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ClearSplinePoints

Clears all the points in the spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddPoint

Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FSplinePoint &  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddPoints

Adds an array of FSplinePoints to the spline.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Points | TArray < FSplinePoint > &  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSplinePoint

Adds a point to the spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Position | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSplinePointAtIndex

Adds a point to the spline at the specified index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Position | FVector &  |  |  |
| Index | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveSplinePoint

Removes point at specified index from the spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSplineWorldPoint

Adds a world space point to the spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Position | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSplineLocalPoint

Adds a local space point to the spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Position | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSplinePoints

Sets the spline to an array of points

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Points | TArray < FVector > &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSplineWorldPoints

Sets the spline to an array of world space points

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Points | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSplineLocalPoints

Sets the spline to an array of local space points

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Points | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLocationAtSplinePoint

Move an existing point to a new location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| InLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWorldLocationAtSplinePoint

Move an existing point to a new world location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| InLocation | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTangentAtSplinePoint

Specify the tangent at a given spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| InTangent | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTangentsAtSplinePoint

Specify the tangents at a given spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| InArriveTangent | FVector &  |  |  |
| InLeaveTangent | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUpVectorAtSplinePoint

Specify the up vector at a given spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| InUpVector | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSplinePointType

Get the type of a spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESplinePointType :: Type  |  |  |

### SetSplinePointType

Specify the type of a spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| Type | ESplinePointType :: Type  |  |  |
| bUpdateSpline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNumberOfSplinePoints

Get the number of points that make up this spline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetLocationAtSplinePoint

Get the location at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldLocationAtSplinePoint

Get the world location at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetDirectionAtSplinePoint

Get the location at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTangentAtSplinePoint

Get the tangent at spline point. This fetches the Leave tangent of the point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetArriveTangentAtSplinePoint

Get the arrive tangent at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetLeaveTangentAtSplinePoint

Get the leave tangent at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRotationAtSplinePoint

Get the rotation at spline point as a rotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetUpVectorAtSplinePoint

Get the up vector at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRightVectorAtSplinePoint

Get the right vector at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRollAtSplinePoint

Get the amount of roll at spline point, in degrees

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetScaleAtSplinePoint

Get the scale at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTransformAtSplinePoint

Get the transform at spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### GetLocationAndTangentAtSplinePoint

Get location and tangent at a spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| Location | FVector &  |  |  |
| Tangent | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLocalLocationAndTangentAtSplinePoint

Get local location and tangent at a spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32  |  |  |
| LocalLocation | FVector &  |  |  |
| LocalTangent | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDistanceAlongSplineAtSplinePoint

Get the distance along the spline at the spline point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetSplineLength

Returns total length along this spline

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetDefaultUpVector

Sets the default up vector used by this spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UpVector | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDefaultUpVector

Gets the default up vector used by this spline

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetInputKeyAtDistanceAlongSpline

Given a distance along the length of this spline, return the corresponding input key at that point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetTimeAtDistanceAlongSpline

Given a distance along the length of this spline, return the corresponding time at that point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetLocationAtDistanceAlongSpline

Given a distance along the length of this spline, return the point in space where this puts you

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldLocationAtDistanceAlongSpline

Given a distance along the length of this spline, return the point in world space where this puts you

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetDirectionAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldDirectionAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there, in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTangentAtDistanceAlongSpline

Given a distance along the length of this spline, return the tangent vector of the spline there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldTangentAtDistanceAlongSpline

Given a distance along the length of this spline, return the tangent vector of the spline there, in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRotationAtDistanceAlongSpline

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetWorldRotationAtDistanceAlongSpline

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there, in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetUpVectorAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRightVectorAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRollAtDistanceAlongSpline

Given a distance along the length of this spline, return the spline's roll there, in degrees.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetScaleAtDistanceAlongSpline

Given a distance along the length of this spline, return the spline's scale there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTransformAtDistanceAlongSpline

Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Distance | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### GetLocationAtTime

Given a time from 0 to the spline duration, return the point in space where this puts you

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldLocationAtTime

Given a time from 0 to the spline duration, return the point in space where this puts you

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetDirectionAtTime

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetWorldDirectionAtTime

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTangentAtTime

Given a time from 0 to the spline duration, return the spline's tangent there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRotationAtTime

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetWorldRotationAtTime

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetUpVectorAtTime

Given a time from 0 to the spline duration, return the spline's up vector there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRightVectorAtTime

Given a time from 0 to the spline duration, return the spline's right vector there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTransformAtTime

Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool  |  |  |
| bUseScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### GetRollAtTime

Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetScaleAtTime

Given a time from 0 to the spline duration, return the spline's scale there.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bUseConstantVelocity | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindInputKeyClosestToWorldLocation

Given a location, in world space, return the input key closest to that location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FindLocationClosestToWorldLocation

Given a location, in world space, return the point on the curve that is closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindDirectionClosestToWorldLocation

Given a location, in world spcae, return a unit direction vector of the spline tangent closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindTangentClosestToWorldLocation

Given a location, in world space, return the tangent vector of the spline closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindRotationClosestToWorldLocation

Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### FindUpVectorClosestToWorldLocation

Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindRightVectorClosestToWorldLocation

Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindRollClosestToWorldLocation

Given a location, in world space, return the spline's roll closest to the location, in degrees.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FindScaleClosestToWorldLocation

Given a location, in world space, return the spline's scale closest to the location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### FindTransformClosestToWorldLocation

Given a location, in world space, return an FTransform closest to that location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| CoordinateSpace | ESplineCoordinateSpace :: Type  |  |  |
| bUseScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

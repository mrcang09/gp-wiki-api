# UCapsuleComponent

- Symbol Type: class
- Symbol Path: Others / UCapsuleComponent
- Source JSON Path: class/detail/Others/UCapsuleComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCapsuleComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A capsule generally used for simple collision. Bounds are rendered as lines in the editor.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CapsuleHalfHeight | float | Half-height, from center of capsule to the end of top or bottom hemisphere.  <br>	 	This cannot be less than CapsuleRadius. |  |
| CapsuleRadius | float | Radius of cap hemispheres and center cylinder. <br>	 	This cannot be more than CapsuleHalfHeight. |  |
| UseDelayPhysicUpdated | int32 |  |  |
| bTransformDataDirty | bool |  |  |
| CapsuleHeight_DEPRECATED | float |  |  |

## Functions

### SetCapsuleSize

Change the capsule size. This is the unscaled size, before component scale is applied.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRadius | float  | : radius of end-cap hemispheres and center cylinder. |  |
| InHalfHeight | float  | : half-height, from capsule center to end of top or bottom hemisphere. |  |
| bUpdateOverlaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCapsuleRadius

Set the capsule radius. This is the unscaled radius, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Radius | float  | : radius of end-cap hemispheres and center cylinder. |  |
| bUpdateOverlaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCapsuleHalfHeight

Set the capsule half-height. This is the unscaled half-height, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HalfHeight | float  | : half-height, from capsule center to end of top or bottom hemisphere. |  |
| bUpdateOverlaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetScaledCapsuleRadius

Returns the capsule radius scaled by the component scale.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | The capsule radius scaled by the component scale. |  |

### GetScaledCapsuleHalfHeight

Returns the capsule half-height scaled by the component scale. This includes both the cylinder and hemisphere cap.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | The capsule half-height scaled by the component scale. |  |

### GetScaledCapsuleHalfHeight_WithoutHemisphere

Returns the capsule half-height minus radius (to exclude the hemisphere), scaled by the component scale.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | The capsule half-height minus radius, scaled by the component scale. |  |

### GetScaledCapsuleSize

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutRadius | float &  | Radius of the capsule, scaled by the component scale. |  |
| OutHalfHeight | float & | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | The capsule radius and half-height scaled by the component scale. |  |

### GetScaledCapsuleSize_WithoutHemisphere

Returns the capsule radius and half-height scaled by the component scale. Half-height excludes the hemisphere end cap.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutRadius | float &  | Radius of the capsule, ignoring component scaling. |  |
| OutHalfHeightWithoutHemisphere | float & | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | The capsule radius and half-height scaled by the component scale. |  |

### GetUnscaledCapsuleRadius

Returns the capsule radius, ignoring component scaling.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | the capsule radius, ignoring component scaling. |  |

### GetUnscaledCapsuleHalfHeight

Returns the capsule half-height, ignoring component scaling. This includes the hemisphere end cap.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | The capsule radius, ignoring component scaling. |  |

### GetUnscaledCapsuleHalfHeight_WithoutHemisphere

Returns the capsule half-height minus radius (to exclude the hemisphere), ignoring component scaling. This excludes the hemisphere end cap.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | The capsule half-height minus radius, ignoring component scaling. |  |

### GetUnscaledCapsuleSize

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutRadius | float &  | Radius of the capsule, scaled by the component scale. |  |
| OutHalfHeight | float & | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | The capsule radius and half-height scaled by the component scale. |  |

### GetUnscaledCapsuleSize_WithoutHemisphere

Returns the capsule radius and half-height, ignoring component scaling. Half-height excludes the hemisphere end cap.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutRadius | float &  | Radius of the capsule, ignoring component scaling. |  |
| OutHalfHeightWithoutHemisphere | float & | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | The capsule radius and half-height (excluding hemisphere end cap), ignoring component scaling. |  |

### GetShapeScale

Get the scale used by this shape. This is a uniform scale that is the minimum of any non-uniform scaling.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | the scale used by this shape. |  |

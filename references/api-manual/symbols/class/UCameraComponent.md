# UCameraComponent

- Symbol Type: class
- Symbol Path: Others / UCameraComponent
- Source JSON Path: class/detail/Others/UCameraComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCameraComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
   The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FieldOfView | float | The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode) |  |
| FirstPersonFieldOfView | float | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |  |
| FirstPersonScale | float | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |  |
| FirstPersonScaleCurveNearValue | float |  |  |
| FirstPersonScaleMaxLength | float |  |  |
| FirstPersonScaleCurvePow | float |  |  |
| bEnableFirstPersonFieldOfView | uint8 | True if the first person field of view should be used for primitives tagged as "IsFirstPerson". |  |
| bEnableFirstPersonScale | uint8 | True if the first person scale should be used for primitives tagged as "IsFirstPerson". |  |
| OrthoWidth | float | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |  |
| OrthoNearClipPlane | float | The near plane distance of the orthographic view (in world units) |  |
| OrthoFarClipPlane | float | The far plane distance of the orthographic view (in world units) |  |
| AspectRatio | float |  |  |
| WidthHeight | FVector2D |  |  |
| bConstrainAspectRatio | uint32 |  |  |
| bUseFieldOfViewForLOD | uint32 |  |  |
| bLockToHmd | uint32 | True if the camera's orientation and position should be locked to the HMD |  |
| bUsePawnControlRotation | uint32 | If this camera component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  @see APawn::GetViewRotation() |  |
| bEnableModifyAdditiveOffset | uint32 |  |  |
| ProjectionMode | TEnumAsByte < ECameraProjectionMode :: Type > |  |  |
| PostProcessBlendWeight | float | Indicates if PostProcessSettings should be used when using this Camera to view through. |  |
| PostProcessSettings | FPostProcessSettings | Post process settings to use for this camera. Don't forget to check the properties you want to override |  |
| bUseControllerViewRotation_DEPRECATED | uint32 | DEPRECATED: use bUsePawnControlRotation instead |  |

## Functions

### SetFieldOfView

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFieldOfView | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFirstPersonFieldOfView

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFirstPersonFieldOfView | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFirstPersonScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFirstPersonScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFirstPersonScaleParams

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFirstPersonScale | float  |  |  |
| InFPScaleCurveNearValue | float  |  |  |
| InFPScaleMaxLen | float  |  |  |
| InFPScaleCurvePow | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEnableFirstPersonFieldOfView

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInEnableFirstPersonFieldOfView | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetEnableFirstPersonScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInEnableFirstPersonScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewActive | bool  |  |  |
| bReset | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ApplyDrawDistanceOffset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFieldOfView | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOrthoWidth

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOrthoWidth | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOrthoNearClipPlane

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOrthoNearClipPlane | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOrthoFarClipPlane

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOrthoFarClipPlane | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAspectRatio

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAspectRatio | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWidthHeight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InWidthHeight | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintAspectRatio

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInConstrainAspectRatio | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUseFieldOfViewForLOD

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInUseFieldOfViewForLOD | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetProjectionMode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InProjectionMode | ECameraProjectionMode :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPostProcessBlendWeight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPostProcessBlendWeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCameraView

Returns camera's Point of View.
	  Called by Camera class. Subclass and postprocess to add any effects.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTime | float  |  |  |
| DesiredView | FMinimalViewInfo & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddOrUpdateBlendable

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendableObject | TScriptInterface < IBlendableInterface >  |  |  |
| InWeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveBlendable

Removes a blendable.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendableObject | TScriptInterface < IBlendableInterface > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetbEnableModifyAdditiveOffset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetEnableModifyAdditiveOffset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### AddAdditiveOffset

Applies the given additive offset, preserving any existing offset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Transform | FTransform &  |  |  |
| FOV | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAdditiveOffset

Removes any additive offset.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetAddtiveInfo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutIsAddtive | bool &  |  |  |
| OutAddtiveOffset | float &  |  |  |
| OutAddtiveTrans | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

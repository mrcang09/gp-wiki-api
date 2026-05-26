# UPhysicsHandleComponent

- Symbol Type: class
- Symbol Path: Others / UPhysicsHandleComponent
- Source JSON Path: class/detail/Others/UPhysicsHandleComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsHandleComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

Utility object for moving physics objects around.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GrabbedComponent | UPrimitiveComponent * | Component we are currently holding |  |
| bSoftAngularConstraint | uint32 |  |  |
| bSoftLinearConstraint | uint32 |  |  |
| bInterpolateTarget | uint32 |  |  |
| LinearDamping | float | Linear damping of the handle spring. |  |
| LinearStiffness | float | Linear stiffness of the handle spring |  |
| AngularDamping | float | Angular stiffness of the handle spring |  |
| AngularStiffness | float | Angular stiffness of the handle spring |  |
| InterpolationSpeed | float | How quickly we interpolate the physics target transform |  |

## Functions

### GrabComponent

Grab the specified component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  |  |  |
| InBoneName | FName  |  |  |
| GrabLocation | FVector  |  |  |
| bConstrainRotation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API virtual void  |  |  |

### GrabComponentAtLocation

Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  |  |  |
| InBoneName | FName  |  |  |
| GrabLocation | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GrabComponentAtLocationWithRotation

Grab the specified component at a given location and rotation. Constrains rotation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  |  |  |
| InBoneName | FName  |  |  |
| Location | FVector  |  |  |
| Rotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### ReleaseComponent

Release the currently held component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API virtual void |  |  |

### GetGrabbedComponent

Returns the currently grabbed component, or null if nothing is grabbed.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API class UPrimitiveComponent * |  |  |

### SetTargetLocation

Set the target location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetTargetRotation

Set the target rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetTargetLocationAndRotation

Set target location and rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector  |  |  |
| NewRotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### GetTargetLocationAndRotation

Get the current location and rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetLocation | FVector &  |  |  |
| TargetRotation | FRotator & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetLinearDamping

Set linear damping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLinearDamping | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetLinearStiffness

Set linear stiffness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLinearStiffness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetAngularDamping

Set angular damping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngularDamping | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetAngularStiffness

Set angular stiffness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngularStiffness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

### SetInterpolationSpeed

Set interpolation speed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewInterpolationSpeed | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

# UPhysicsConstraintComponent

- Symbol Type: class
- Symbol Path: Others / UPhysicsConstraintComponent
- Source JSON Path: class/detail/Others/UPhysicsConstraintComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsConstraintComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintActor1 | AActor * | Pointer to first Actor to constrain. |  |
| ComponentName1 | FConstrainComponentPropName | Name of first component property to constrain. If Actor1 is NULL, will look within Owner.<br>	 	If this is NULL, will use RootComponent of Actor1 |  |
| ConstraintActor2 | AActor * | Pointer to second Actor to constrain. |  |
| ComponentName2 | FConstrainComponentPropName | Name of second component property to constrain. If Actor2 is NULL, will look within Owner. <br>	 	If this is NULL, will use RootComponent of Actor2 |  |
| ConstraintSetup_DEPRECATED | UPhysicsConstraintTemplate * |  |  |
| OnConstraintBroken | FConstraintBrokenSignature | Notification when constraint is broken. |  |
| ConstraintInstance | FConstraintInstance | All constraint settings |  |

## Functions

### SetConstrainedComponents

Directly specify component to connect. Will update frames based on current position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component1 | UPrimitiveComponent *  |  |  |
| BoneName1 | FName  |  |  |
| Component2 | UPrimitiveComponent *  |  |  |
| BoneName2 | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BreakConstraint

Break this constraint

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetLinearPositionDrive

EnablesDisables linear position drive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableDriveX | bool  | Indicates whether the drive for the X-Axis should be enabled |  |
| bEnableDriveY | bool  | Indicates whether the drive for the Y-Axis should be enabled |  |
| bEnableDriveZ | bool | Indicates whether the drive for the Z-Axis should be enabled |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearVelocityDrive

EnablesDisables linear position drive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableDriveX | bool  | Indicates whether the drive for the X-Axis should be enabled |  |
| bEnableDriveY | bool  | Indicates whether the drive for the Y-Axis should be enabled |  |
| bEnableDriveZ | bool | Indicates whether the drive for the Z-Axis should be enabled |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularOrientationDrive

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSwingDrive | bool  | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |
| bEnableTwistDrive | bool | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOrientationDriveTwistAndSwing

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableTwistDrive | bool  | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |
| bEnableSwingDrive | bool | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOrientationDriveSLERP

EnablesDisables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSLERP | bool |   Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularVelocityDrive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSwingDrive | bool  |  |  |
| bEnableTwistDrive | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularVelocityDriveTwistAndSwing

EnablesDisables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableTwistDrive | bool  | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |
| bEnableSwingDrive | bool | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularVelocityDriveSLERP

EnablesDisables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableSLERP | bool |   Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularDriveMode

Switches the angular drive mode between SLERP and Twist And Swing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DriveMode | EAngularDriveMode :: Type | The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearPositionTarget

Sets the target position for the linear drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPosTarget | FVector & | Target position |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearVelocityTarget

Sets the target velocity for the linear drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVelTarget | FVector & | Target velocity |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearDriveParams

Sets the drive params for the linear drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PositionStrength | float  | Positional strength for the drive (stiffness) |  |
| VelocityStrength | float  | Velocity strength of the drive (damping) |  |
| InForceLimit | float | Max force applied by the drive |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularOrientationTarget

Sets the target orientation for the angular drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPosTarget | FRotator & | Target orientation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularVelocityTarget

Sets the target velocity for the angular drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVelTarget | FVector & | Target velocity |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularDriveParams

Sets the drive params for the angular drive.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PositionStrength | float  | Positional strength for the drive (stiffness) |  |
| VelocityStrength | float  | Velocity strength of the drive (damping) |  |
| InForceLimit | float | Max force applied by the drive |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearXLimit

Sets the LinearX Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintType | ELinearConstraintMotion  | New Constraint Type |  |
| LimitSize | float | Size of limit |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearYLimit

Sets the LinearY Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintType | ELinearConstraintMotion  | New Constraint Type |  |
| LimitSize | float | Size of limit |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearZLimit

Sets the LinearZ Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintType | ELinearConstraintMotion  | New Constraint Type |  |
| LimitSize | float | Size of limit |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularSwing1Limit

Sets the Angular Swing1 Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MotionType | EAngularConstraintMotion  |  |  |
| Swing1LimitAngle | float | Size of limit in degrees |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularSwing2Limit

Sets the Angular Swing2 Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MotionType | EAngularConstraintMotion  |  |  |
| Swing2LimitAngle | float | Size of limit in degrees |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularTwistLimit

Sets the Angular Twist Motion Type

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintType | EAngularConstraintMotion  | New Constraint Type |  |
| TwistLimitAngle | float | Size of limit in degrees |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearBreakable

Sets the Linear Breakable properties

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bLinearBreakable | bool  | Whether it is possible to break the joint with linear force |  |
| LinearBreakThreshold | float | Force needed to break the joint |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAngularBreakable

Sets the Angular Breakable properties

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAngularBreakable | bool  | Whether it is possible to break the joint with angular force |  |
| AngularBreakThreshold | float | Torque needed to break the joint |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentTwist

Gets the current Angular Twist of the constraint

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetCurrentSwing1

Gets the current Swing1 of the constraint

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetCurrentSwing2

Gets the current Swing2 of the constraint

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetConstraintReferenceFrame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Frame | EConstraintFrame :: Type  |  |  |
| RefFrame | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintReferencePosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Frame | EConstraintFrame :: Type  |  |  |
| RefPosition | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintReferenceOrientation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Frame | EConstraintFrame :: Type  |  |  |
| PriAxis | FVector &  |  |  |
| SecAxis | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDisableCollision

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bDisableCollision | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetConstraintForce

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutLinearForce | FVector &  |  |  |
| OutAngularForce | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBroken

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

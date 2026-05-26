# FConstraintProfileProperties

- Symbol Type: struct
- Symbol Path: FConstraintProfileProperties
- Source JSON Path: cppstruct/detail/FConstraintProfileProperties.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FConstraintProfileProperties.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Container for properties of a physics constraint that can be easily swapped at runtime. This is useful for switching different setups when going from ragdoll to standup for example

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProjectionLinearTolerance | float | Linear tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |  |
| ProjectionAngularTolerance | float | Angular tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |  |
| LinearBreakThreshold | float | Force needed to break the distance constraint. |  |
| AngularBreakThreshold | float | Torque needed to break the joint. |  |
| LinearLimit | FLinearConstraint |  |  |
| ConeLimit | FConeConstraint |  |  |
| TwistLimit | FTwistConstraint |  |  |
| LinearDrive | FLinearDriveConstraint |  |  |
| AngularDrive | FAngularDriveConstraint |  |  |
| bDisableCollision | uint8 |  |  |
| bParentDominates | uint8 |  |  |
| bEnableProjection | uint8 | If distance error between bodies exceeds 0.1 units, or rotation error exceeds 10 degrees, body will be projected to fix this.<br>	 For example a chain spinning too fast will have its elements appear detached due to velocity, this will project all bodies so they still appear attached to each other. |  |
| bAngularBreakable | uint8 | Whether it is possible to break the joint with angular force. |  |
| bLinearBreakable | uint8 | Whether it is possible to break the joint with linear force. |  |

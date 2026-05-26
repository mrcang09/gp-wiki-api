# FClothConfig

- Symbol Type: struct
- Symbol Path: FClothConfig
- Source JSON Path: cppstruct/detail/FClothConfig.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FClothConfig.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Holds initial, asset level config for clothing actors.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WindMethod | EClothingWindMethod |  |  |
| VerticalConstraintConfig | FClothConstraintSetup |  |  |
| HorizontalConstraintConfig | FClothConstraintSetup |  |  |
| BendConstraintConfig | FClothConstraintSetup |  |  |
| ShearConstraintConfig | FClothConstraintSetup |  |  |
| SelfCollisionRadius | float |  |  |
| SelfCollisionStiffness | float |  |  |
| SelfCollisionCullScale | float | Scale to use for the radius of the culling checks for self collisions.<br>	  Any other self collision body within the radius of this check will be culled.<br>	  This helps performance with higher resolution meshes by reducing the number<br>	  of colliding bodies within the cloth. Reducing this will have a negative<br>	  effect on performance! |  |
| Damping | FVector |  |  |
| Friction | float |  |  |
| WindDragCoefficient | float |  |  |
| WindLiftCoefficient | float |  |  |
| LinearDrag | FVector |  |  |
| AngularDrag | FVector |  |  |
| LinearInertiaScale | FVector |  |  |
| AngularInertiaScale | FVector |  |  |
| CentrifugalInertiaScale | FVector |  |  |
| SolverFrequency | float |  |  |
| StiffnessFrequency | float |  |  |
| GravityScale | float |  |  |
| TetherStiffness | float |  |  |
| TetherLimit | float |  |  |
| CollisionThickness | float |  |  |

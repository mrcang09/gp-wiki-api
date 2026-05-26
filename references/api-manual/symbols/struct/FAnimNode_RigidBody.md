# FAnimNode_RigidBody

- Symbol Type: struct
- Symbol Path: FAnimNode_RigidBody
- Source JSON Path: cppstruct/detail/FAnimNode_RigidBody.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RigidBody.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverridePhysicsAsset | UPhysicsAsset * | Physics asset to use. If empty use the skeletal mesh's default physics asset |  |
| LastUsePhysicsAsset | TWeakObjectPtr < UPhysicsAsset > |  |  |
| OverrideWorldGravity | FVector | Override gravity |  |
| ExternalForce | FVector | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |  |
| OverlapChannel | TEnumAsByte < ECollisionChannel > | The channel we use to find static geometry to collide with |  |
| bEnableWorldGeometry | bool |  |  |
| SimulationSpace | ESimulationSpace | What space to simulate the bodies in. This affects how velocities are generated |  |
| bOverrideWorldGravity | bool |  |  |
| CachedBoundsScale | float | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds). |  |
| bUseCompPhysicsAssetWhenNotSet | bool |  |  |
| bUseIntersectDetect | bool |  |  |
| bUseMultipleRigidBodyNodeInitDelay | bool |  |  |
| bComponentSpaceSimulation_DEPRECATED | bool |  |  |
| BoneShiftTolerenceChecker | FAnimNodeBoneShiftTolerenceChecker | Bone Shift Tolerence Check Start |  |

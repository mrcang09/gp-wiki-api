# FAnimPhysBodyDefinition_UE5

- Symbol Type: struct
- Symbol Path: FAnimPhysBodyDefinition_UE5
- Source JSON Path: cppstruct/detail/FAnimPhysBodyDefinition_UE5.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysBodyDefinition_UE5.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoundBone | FBoneReference |  |  |
| BoxExtents | FVector | Extents of the box to use for simulation |  |
| LocalJointOffset | FVector | Vector relative to the body being simulated to attach the constraint to |  |
| ConstraintSetup | FAnimPhysConstraintSetup_UE5 | Data describing the constraints we will apply to the body |  |
| CollisionType | AnimPhysCollisionType | Resolution method for planar limits |  |
| SphereCollisionRadius | float | Radius to use if CollisionType is set to CustomSphere |  |

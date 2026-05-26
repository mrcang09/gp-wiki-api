# FConstraint

- Symbol Type: struct
- Symbol Path: FConstraint
- Source JSON Path: cppstruct/detail/FConstraint.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FConstraint.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Constraint Set up

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetBone | FBoneReference | Target Bone this is constraint to |  |
| OffsetOption | EConstraintOffsetOption | Maintain offset based on refpose or not.<br>	  <br>	  None - no offset<br>	  Offset_RefPose - offset is created based on reference pose<br>	  <br>	  In the future, we'd like to support custom offset, not just based on ref pose |  |
| TransformType | ETransformConstraintType | What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component |  |
| PerAxis | FFilterOptionPerAxis | Per axis filter options - applied in their local space not in world space |  |

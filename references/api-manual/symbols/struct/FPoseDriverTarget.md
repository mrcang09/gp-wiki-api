# FPoseDriverTarget

- Symbol Type: struct
- Symbol Path: FPoseDriverTarget
- Source JSON Path: cppstruct/detail/FPoseDriverTarget.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FPoseDriverTarget.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Information about each target in the PoseDriver

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneTransforms | TArray < FPoseDriverTransform > | Translation of this target |  |
| TargetRotation | FRotator | Rotation of this target |  |
| TargetScale | float | Scale applied to this target's function - a larger value will activate this target sooner |  |
| bApplyCustomCurve | bool | If we should apply a custom curve mapping to how this target activates |  |
| CustomCurve | FRichCurve | Custom curve mapping to apply if bApplyCustomCurve is true |  |
| DrivenName | FName | Name of item to drive - depends on DriveOutput setting.  <br>	 	If DriveOutput is DrivePoses, this should be the name of a pose in the assigned PoseAsset<br>	 	If DriveOutput is DriveCurves, this is the name of the curve (morph target, material param etc) to drive |  |

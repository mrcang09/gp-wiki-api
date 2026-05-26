# FAnimNode_ObserveBone

- Symbol Type: struct
- Symbol Path: FAnimNode_ObserveBone
- Source JSON Path: cppstruct/detail/FAnimNode_ObserveBone.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ObserveBone.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Debugging node that displays the current value of a bone in a specific space.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneToObserve | FBoneReference | Name of bone to observe. |  |
| DisplaySpace | TEnumAsByte < EBoneControlSpace > | Reference frame to display the bone transform in. |  |
| bRelativeToRefPose | bool | Show the difference from the reference pose? |  |
| Translation | FVector | Translation of the bone being observed. |  |
| Rotation | FRotator | Rotation of the bone being observed. |  |
| Scale | FVector | Scale of the bone being observed. |  |

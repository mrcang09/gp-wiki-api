# FDirectorTrackCut

- Symbol Type: struct
- Symbol Path: FDirectorTrackCut
- Source JSON Path: cppstruct/detail/FDirectorTrackCut.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FDirectorTrackCut.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

A track type used for binding the view of a Player (attached to this tracks group) to the actor of a different group.
 
 
 Information for one cut in this track.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float | Time to perform the cut. |  |
| TransitionTime | float | Time taken to move view to new camera. |  |
| TargetCamGroup | FName | GroupName of UInterpGroup to cut viewpoint to. |  |
| ShotNumber | int32 | Shot number for developer reference |  |

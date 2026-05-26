# FAnimNode_PoseSnapshot

- Symbol Type: struct
- Symbol Path: FAnimNode_PoseSnapshot
- Source JSON Path: cppstruct/detail/FAnimNode_PoseSnapshot.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_PoseSnapshot.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Provide a snapshot pose, either from the internal named pose cache or via a supplied snapshot

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Mode | ESnapshotSourceMode | How to access the snapshot |  |
| SnapshotName | FName | The name of the snapshot previously stored with SavePoseSnapshot |  |
| Snapshot | FPoseSnapshot | Snapshot to use. This should be populated at first by calling SnapshotPose |  |

# FAnimNode_CopyPoseFromMesh

- Symbol Type: struct
- Symbol Path: FAnimNode_CopyPoseFromMesh
- Source JSON Path: cppstruct/detail/FAnimNode_CopyPoseFromMesh.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromMesh.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceMeshComponent | TWeakObjectPtr < USkeletalMeshComponent > | This is used by default if it's valid |  |
| bUseAttachedParent | bool | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |  |

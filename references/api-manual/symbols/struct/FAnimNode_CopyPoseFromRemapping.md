# FAnimNode_CopyPoseFromRemapping

- Symbol Type: struct
- Symbol Path: FAnimNode_CopyPoseFromRemapping
- Source JSON Path: cppstruct/detail/FAnimNode_CopyPoseFromRemapping.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromRemapping.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceMeshComponent | TWeakObjectPtr < USkeletalMeshComponent > | This is used by default if it's valid |  |
| bUseAttachedParent | bool | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |  |
| bIkGunValid | bool |  |  |
| bParentPoseOffset | bool |  |  |
| NewFPPPoseOffset | FNewFPPPoseOffset |  |  |
| BoneNeedRelevant | TMap < FName , FName > |  |  |

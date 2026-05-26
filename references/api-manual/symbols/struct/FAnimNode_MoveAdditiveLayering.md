# FAnimNode_MoveAdditiveLayering

- Symbol Type: struct
- Symbol Path: FAnimNode_MoveAdditiveLayering
- Source JSON Path: cppstruct/detail/FAnimNode_MoveAdditiveLayering.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_MoveAdditiveLayering.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BasePose | FPoseLink |  |  |
| TargetPose | FPoseLink |  |  |
| RefPose | FPoseLink |  |  |
| bFixRootRotation | bool |  |  |
| ArmMeshSpaceAlphaL | float |  |  |
| ArmMeshSpaceAlphaR | float |  |  |
| ArmSwayAlphaL | float |  |  |
| ArmSwayAlphaR | float |  |  |
| HandAlphaL | float |  |  |
| HandAlphaR | float |  |  |
| UpperPoseOverrideLayerSetup | TArray < FInputBlendPose > | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |  |
| SpineLocalSpaceAdditiveLayerSetup | TArray < FInputBlendPose > |  |  |
| MeshSpaceAdditiveLayerSetup_Left | TArray < FInputBlendPose > |  |  |
| MeshSpaceAdditiveLayerSetup_Right | TArray < FInputBlendPose > |  |  |
| ArmLocalSpaceAdditiveLayerSetup | TArray < FInputBlendPose > |  |  |
| bEvaluateLayer0 | bool |  |  |
| bEvaluateLayer1 | bool |  |  |
| bEvaluateLayer2 | bool |  |  |
| bEvaluateLayer3 | bool |  |  |
| SkeletonGuid | FGuid |  |  |
| VirtualBoneGuid | FGuid |  |  |
| UpperPoseOverrideData | FMoveAdditiveLayeringData |  |  |
| SpineLocalSpaceAdditiveData | FMoveAdditiveLayeringData |  |  |
| MeshSpaceAdditiveData_Left | FMoveAdditiveLayeringData |  |  |
| MeshSpaceAdditiveData_Right | FMoveAdditiveLayeringData |  |  |
| ArmLocalSpaceAdditiveData | FMoveAdditiveLayeringData |  |  |
| bOutputTargetPose | bool |  |  |
| bOutputRefPose | bool |  |  |
| bOutputLocalSpaceAdditivePose | bool |  |  |
| bOutputMeshSpaceAdditivePose | bool |  |  |

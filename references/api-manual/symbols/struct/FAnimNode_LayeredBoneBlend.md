# FAnimNode_LayeredBoneBlend

- Symbol Type: struct
- Symbol Path: FAnimNode_LayeredBoneBlend
- Source JSON Path: cppstruct/detail/FAnimNode_LayeredBoneBlend.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_LayeredBoneBlend.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BasePose | FPoseLink | The source pose |  |
| BlendPoses | TArray < FPoseLink > | Each layer's blended pose |  |
| LayerSetup | TArray < FInputBlendPose > | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |  |
| BlendWeights | TArray < float > | The weights of each layer |  |
| bMeshSpaceRotationBlend | bool | Whether to blend bone rotations in mesh space or in local space |  |
| CurveBlendOption | TEnumAsByte < enum ECurveBlendOption :: Type > | How to blend the layers together |  |
| bBlendRootMotionBasedOnRootBone | bool | Whether to incorporate the per-bone blend weight of the root bone when lending root motion |  |
| bHasRelevantPoses | bool |  |  |
| PerBoneBlendWeights | TArray < FPerBoneBlendWeight > |  |  |
| SkeletonGuid | FGuid |  |  |
| VirtualBoneGuid | FGuid |  |  |
| DesiredBoneBlendWeightsInitMesh | TWeakObjectPtr < USkeletalMesh > |  |  |

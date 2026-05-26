# FAnimNode_BoneFollowChain

- Symbol Type: struct
- Symbol Path: FAnimNode_BoneFollowChain
- Source JSON Path: cppstruct/detail/FAnimNode_BoneFollowChain.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneFollowChain.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

make bone list move like snake

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BasePose | FPoseLink |  |  |
| ToParentDisTolerence | int32 |  |  |
| ToParentMaxDisTolerence | int32 |  |  |
| bLeaderBoneMoveFromAnim | bool |  |  |
| bClearParentBonePathWhenNoMove | bool |  |  |
| bEnableTerrainAdaptFeature | bool |  |  |
| TerrainTraceStart | float |  |  |
| TerrainTraceEnd | float |  |  |
| ToParentRotationScale | float |  |  |
| bLerpBoneRotaion | bool |  |  |
| bLerpBoneRotaionCalcCurFrameBoneTransform | bool |  |  |
| MaxBonePathRecordBufferSize | int32 |  |  |
| LeaderBone | FBoneReference |  |  |
| FollowBoneList | TArray < FBoneReference > |  |  |

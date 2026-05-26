# FAnimNode_QuadrupedTerrainAdapting

- Symbol Type: struct
- Symbol Path: FAnimNode_QuadrupedTerrainAdapting
- Source JSON Path: cppstruct/detail/FAnimNode_QuadrupedTerrainAdapting.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_QuadrupedTerrainAdapting.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool |  |  |
| bDrawDebug | bool |  |  |
| RayTrace_SphereRadius | float |  |  |
| RayTrace_MaxGroundAngle | float |  |  |
| RayTrace_LHandBottom | FBoneSocketTarget |  |  |
| RayTrace_RHandBottom | FBoneSocketTarget |  |  |
| RayTrace_LFootBottom | FBoneSocketTarget |  |  |
| RayTrace_RFootBottom | FBoneSocketTarget |  |  |
| bActorAdjustRotationFloor | bool |  |  |
| bEnableSlopeAdapting | bool |  |  |
| bResetSlopeAdaptingOnSkipCal | bool |  |  |
| bLerpSlopeAdaptingOnSkipCal | bool |  |  |
| bEnableLionDanceSlopeAdapting | bool |  |  |
| bEnableUpdateChildrenComps | bool |  |  |
| UpdateChildrenCompsFrequency | int32 |  |  |
| SlopeAdapting_Pelvis | FBoneReference |  |  |
| SlopeAdapting_Pelvis1 | FBoneReference |  |  |
| SlopeAdapting_Pelvis2 | FBoneReference |  |  |
| SlopeAdapting_LClavicle | FBoneReference |  |  |
| SlopeAdapting_RClavicle | FBoneReference |  |  |
| SlopeAdapting_LThigh | FBoneReference |  |  |
| SlopeAdapting_RThigh | FBoneReference |  |  |
| SlopeAdapting_Root | FBoneReference |  |  |
| TraceDownLength | float |  |  |
| SlopeAdapting_PelvisLimitHeight | float |  |  |
| SlopeAdapting_LimitSlopeAngle | float |  |  |
| SlopeAdapting_PositionLerpSpeed | float |  |  |
| SlopeAdapting_RotationLerpSpeed | float |  |  |
| SlopeAdapting_BehindLegModifyFactor | float |  |  |
| BoneToFlooroffset | float |  |  |
| bEnableLegAdapting | bool |  |  |
| LegAdapting_IKLerpSpeed | float |  |  |
| LegAdapting_IKMaxHeight | float |  |  |
| LegAdapting_LHand | FAnimNode_TwoBoneIK |  |  |
| LegAdapting_RHand | FAnimNode_TwoBoneIK |  |  |
| LegAdapting_LFoot | FAnimNode_TwoBoneIK |  |  |
| LegAdapting_RFoot | FAnimNode_TwoBoneIK |  |  |
| fSlopeAdaptOffset | float |  |  |
| bEnableLionDanceLegAdapting | bool |  |  |
| bEnableFootAdapting | bool |  |  |
| FootAdapting_LHand | FBoneReference |  |  |
| FootAdapting_RHand | FBoneReference |  |  |
| FootAdapting_LFoot | FBoneReference |  |  |
| FootAdapting_RFoot | FBoneReference |  |  |
| FootAdapting_LimitRotation | FRotator |  |  |
| FootAdapting_RotationLerpSpeed | float |  |  |

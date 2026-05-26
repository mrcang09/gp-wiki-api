# FAnimNode_AssetPlayerBase

- Symbol Type: struct
- Symbol Path: FAnimNode_AssetPlayerBase
- Source JSON Path: cppstruct/detail/FAnimNode_AssetPlayerBase.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_AssetPlayerBase.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Description

Base class for any asset playing anim node

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIgnoreForRelevancyTest | bool | If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore<br>	   this node |  |
| GroupIndex | int32 |  |  |
| GroupName | FName |  |  |
| GroupRole | TEnumAsByte < EAnimGroupRole :: Type > |  |  |
| bNeedAnimNotifyWhenNotLeader | bool |  |  |
| bShouldSortWithTimeAccumulator | bool |  |  |
| BlendWeight | float | Last encountered blendweight for this node |  |
| InternalTimeAccumulator | float | Accumulated time used to reference the asset in this node |  |

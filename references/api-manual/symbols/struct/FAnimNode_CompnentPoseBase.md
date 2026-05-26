# FAnimNode_CompnentPoseBase

- Symbol Type: struct
- Symbol Path: FAnimNode_CompnentPoseBase
- Source JSON Path: cppstruct/detail/FAnimNode_CompnentPoseBase.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CompnentPoseBase.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Alpha | float |  |  |
| AlphaScaleBias | FInputScaleBias |  |  |
| LODThreshold | int32 | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |  |
| bActiveNode | bool | Engine Modify<br>	 Enable Node to be ignored at runtime but keep alpha value no change<br>	 false will ignore (do no or skip) evaluate, but no affect on update |  |
| ActualAlpha | float |  |  |

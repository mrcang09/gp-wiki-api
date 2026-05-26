# FAnimNode_ApplyAdditive

- Symbol Type: struct
- Symbol Path: FAnimNode_ApplyAdditive
- Source JSON Path: cppstruct/detail/FAnimNode_ApplyAdditive.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ApplyAdditive.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Base | FPoseLink |  |  |
| Additive | FPoseLink |  |  |
| Alpha | float |  |  |
| AlphaScaleBias | FInputScaleBias |  |  |
| LODThreshold | int32 | Max LOD that this node is allowed to run<br>	  For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	  when the component LOD becomes 3, it will stop updateevaluate<br>	  currently transition would be issue and that has to be re-visited |  |
| ActualAlpha | float |  |  |

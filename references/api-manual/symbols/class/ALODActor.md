# ALODActor

- Symbol Type: class
- Symbol Path: Others / ALODActor
- Source JSON Path: class/detail/Others/ALODActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ALODActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMeshComponent | UStaticMeshComponent * |  |  |
| Proxy | UHLODProxy * | The mesh proxy used to display this LOD |  |
| Key | FName | The key used to validate this actor against the proxy |  |
| LODDrawDistance | float | what distance do you want this to show up instead of SubActors |  |
| SubActors | TArray < AActor * > |  |  |
| LODLevel | int32 | The hierarchy level of this actor; the first tier of HLOD is level 1, the second tier is level 2 and so on. |  |
| CachedNumHLODLevels | uint8 |  |  |
| HLODActorDebugDynamicMaterialInstance | UMaterialInstanceDynamic * |  |  |
| SubActorsDebugDynamicMaterialInstance | UMaterialInstanceDynamic * |  |  |
| NumTrianglesInSubActors | uint32 | Cached number of triangles contained in the SubActors |  |
| NumTrianglesInMergedMesh | uint32 | Cached number of triangles contained in the SubActors |  |
| bOverrideMaterialMergeSettings | bool | Flag whether or not to use the override MaterialSettings when creating the proxy mesh |  |
| MaterialSettings | FMaterialProxySettings | Override Material Settings, used when creating the proxy mesh |  |
| bOverrideTransitionScreenSize | bool | Flag whether or not to use the override TransitionScreenSize for this proxy mesh |  |
| TransitionScreenSize | float | Override transition screen size value, determines the screen size at which the proxy is visible<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |  |
| bOverrideScreenSize | bool | Flag whether or not to use the override ScreenSize when creating the proxy mesh |  |
| ScreenSize | int32 | Override screen size value used in mesh reduction, when creating the proxy mesh |  |

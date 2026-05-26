# FHierarchicalSimplification

- Symbol Type: struct
- Symbol Path: FHierarchicalSimplification
- Source JSON Path: cppstruct/detail/FHierarchicalSimplification.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FHierarchicalSimplification.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TransitionScreenSize | float | The screen radius an mesh object should reach before swapping to the LOD actor, once one of parent displays, it won't draw any of children. |  |
| OverrideDrawDistance | float |  |  |
| bUseOverrideDrawDistance | bool |  |  |
| bAllowSpecificExclusion | uint8 |  |  |
| bSimplifyMesh | bool | If this is true, it will simplify mesh but it is slower.<br>	 If false, it will just merge actors but not simplify using the lower LOD if exists.<br>	 For example if you build LOD 1, it will use LOD 1 of the mesh to merge actors if exists.<br>	 If you merge material, it will reduce drawcalls. |  |
| ProxySetting | FMeshProxySettings | Simplification Setting if bSimplifyMesh is true |  |
| MergeSetting | FMeshMergingSettings | Merge Mesh Setting if bSimplifyMesh is false |  |
| DesiredBoundRadius | float | Desired Bounding Radius for clustering - this is not guaranteed but used to calculate filling factor for auto clustering |  |
| DesiredFillingPercentage | float | Desired Filling Percentage for clustering - this is not guaranteed but used to calculate filling factor  for auto clustering |  |
| DesiredGridSize | float |  |  |
| DesiredGridOffset | float |  |  |
| DesiredGridVolume | TArray < FVector4 > |  |  |
| GridIgnoreStaticMeshs | TArray < FString > |  |  |
| MinNumberOfActorsToBuild | int32 | Min number of actors to build LODActor |  |
| bOnlyGenerateClustersForVolumes | bool | Min number of actors to build LODActor |  |
| bReusePreviousLevelClusters | bool | Will reuse the clusters generated for the previous (lower) HLOD level |  |

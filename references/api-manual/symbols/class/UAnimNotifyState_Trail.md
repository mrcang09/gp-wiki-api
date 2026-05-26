# UAnimNotifyState_Trail

- Symbol Type: class
- Symbol Path: Others / UAnimNotifyState_Trail
- Source JSON Path: class/detail/Others/UAnimNotifyState_Trail.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState_Trail.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PSTemplate | UParticleSystem * | The particle system to use for this trail. |  |
| FirstSocketName | FName | Name of the first socket defining this trail. |  |
| SecondSocketName | FName | Name of the second socket defining this trail. |  |
| FirstSocketRelativeOffset | FTransform |  |  |
| SecondSocketRelativeOffset | FTransform |  |  |
| WidthScaleMode | TEnumAsByte < enum ETrailWidthMode > |  |  |
| WidthScaleCurve | FName | Name of the curve to drive the width scale. |  |
| bRecycleSpawnedSystems | uint32 |  |  |
| bRenderGeometry | uint32 | If true, render the trail geometry (this should typically be on) |  |
| bRenderSpawnPoints | uint32 | If true, render stars at each spawned particle point along the trail |  |
| bRenderTangents | uint32 | If true, render a line showing the tangent at each spawned particle point along the trail |  |
| bRenderTessellation | uint32 | If true, render the tessellated path between spawned particles |  |

## Functions

### OverridePSTemplate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshComp | USkeletalMeshComponent *  |  |  |
| Animation | UAnimSequenceBase * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UParticleSystem *  |  |  |

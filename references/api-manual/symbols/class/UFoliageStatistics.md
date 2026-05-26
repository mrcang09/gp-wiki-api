# UFoliageStatistics

- Symbol Type: class
- Symbol Path: Others / UFoliageStatistics
- Source JSON Path: class/detail/Others/UFoliageStatistics.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UFoliageStatistics.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Functions

### FoliageOverlappingSphereCount

Counts how many foliage instances overlap a given sphere

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| StaticMesh | UStaticMesh *  |  |  |
| CenterPosition | FVector  | The center position of the sphere |  |
| Radius | float |  The radius of the sphere. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### FoliageOverlappingBoxCount

Gets the number of instances overlapping a provided box

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| StaticMesh | UStaticMesh *  | Mesh to count |  |
| Box | FBox | Box to overlap |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

# UNavCollision

- Symbol Type: class
- Symbol Path: Others / UNavCollision
- Source JSON Path: class/detail/Others/UNavCollision.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UNavCollision.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CylinderCollision | TArray < FNavCollisionCylinder > | list of nav collision cylinders |  |
| BoxCollision | TArray < FNavCollisionBox > | list of nav collision boxes |  |
| AreaClass | TSubclassOf < UNavArea > | navigation area type (empty = default obstacle) |  |
| bIsDynamicObstacle | uint32 | If set, mesh will be used as dynamic obstacle (don't create navmesh on top, much faster addingremoving) |  |
| bGatherConvexGeometry | uint32 | If set, convex collisions will be exported offline for faster runtime navmesh building (increases memory usage) |  |

# UShapeComponent

- Symbol Type: class
- Symbol Path: Others / UShapeComponent
- Source JSON Path: class/detail/Others/UShapeComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UShapeComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

ShapeComponent is a PrimitiveComponent that is represented by a simple geometrical shape (sphere, capsule, box, etc).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShapeColor | FColor | Color used to draw the shape. |  |
| ShapeBodySetup | UBodySetup * | Description of collision |  |
| bDrawOnlyIfSelected | uint8 | Only show this component if the actor is selected |  |
| bShouldCollideWhenPlacing | uint8 | If true it allows Collision when placing even if collision is not enabled |  |
| bDynamicObstacle | uint8 | If set, shape will be exported for navigation as dynamic modifier instead of using regular collision data |  |
| AreaClass | TSubclassOf < UNavArea > | Navigation area type (empty = default obstacle) |  |

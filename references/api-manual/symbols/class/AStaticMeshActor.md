# AStaticMeshActor

- Symbol Type: class
- Symbol Path: Others / AStaticMeshActor
- Source JSON Path: class/detail/Others/AStaticMeshActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AStaticMeshActor.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

StaticMeshActor is an instance of a UStaticMesh in the world.
  Static meshes are geometry that do not animate or otherwise deform, and are more efficient to render than other types of geometry.
  Static meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
 
  @see UStaticMesh

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMeshComponent | UStaticMeshComponent * |  |  |
| bStaticMeshReplicateMovement | bool | This static mesh should replicate movement. Automatically sets the RemoteRole and bReplicateMovement flags. Meant to be edited on placed actors (those other two properties are not) |  |
| NavigationGeometryGatheringMode | ENavDataGatheringMode |  |  |

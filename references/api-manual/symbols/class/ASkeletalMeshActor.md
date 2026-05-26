# ASkeletalMeshActor

- Symbol Type: class
- Symbol Path: Others / ASkeletalMeshActor
- Source JSON Path: class/detail/Others/ASkeletalMeshActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ASkeletalMeshActor.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

SkeletalMeshActor is an instance of a USkeletalMesh in the world.
  Skeletal meshes are deformable meshes that can be animated and change their geometry at run-time.
  Skeletal meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
  
  @see USkeletalMesh

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bShouldDoAnimNotifies | uint32 | Whether or not this actor should respond to anim notifies - CURRENTLY ONLY AFFECTS PlayParticleEffect NOTIFIES |  |
| bWakeOnLevelStart_DEPRECATED | uint32 |  |  |
| SkeletalMeshComponent | USkeletalMeshComponent * |  |  |
| ReplicatedMesh | USkeletalMesh * | Used to replicate mesh to clients |  |
| ReplicatedPhysAsset | UPhysicsAsset * | Used to replicate physics asset to clients |  |
| ReplicatedMaterial0 | UMaterialInterface * | used to replicate the material in index 0 |  |
| ReplicatedMaterial1 | UMaterialInterface * |  |  |

## Functions

### OnRep_ReplicatedMesh

Replication Notification Callbacks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ReplicatedPhysAsset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ReplicatedMaterial0

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ReplicatedMaterial1

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

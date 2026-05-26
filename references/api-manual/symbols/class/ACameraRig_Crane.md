# ACameraRig_Crane

- Symbol Type: class
- Symbol Path: Others / ACameraRig_Crane
- Source JSON Path: class/detail/Others/ACameraRig_Crane.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ACameraRig_Crane.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

A simple rig for simulating crane-like camera movements.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CranePitch | float | Controls the pitch of the crane arm. |  |
| CraneYaw | float | Controls the yaw of the crane arm. |  |
| CraneArmLength | float | Controls the length of the crane arm. |  |
| bLockMountPitch | bool | Lock the mount pitch so that an attached camera is locked and pitched in the direction of the crane arm |  |
| bLockMountYaw | bool | Lock the mount yaw so that an attached camera is locked and oriented in the direction of the crane arm |  |
| TransformComponent | USceneComponent * | Root component to give the whole actor a transform. |  |
| CraneYawControl | USceneComponent * | Component to control Yaw. |  |
| CranePitchControl | USceneComponent * | Component to control Pitch. |  |
| CraneCameraMount | USceneComponent * | Component to define the attach point for cameras. |  |
| PreviewMesh_CraneArm | UStaticMeshComponent * | Preview meshes for visualization |  |
| PreviewMesh_CraneBase | UStaticMeshComponent * |  |  |
| PreviewMesh_CraneMount | UStaticMeshComponent * |  |  |
| PreviewMesh_CraneCounterWeight | UStaticMeshComponent * |  |  |

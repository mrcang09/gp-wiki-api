# UAnimBlueprint

- Symbol Type: class
- Symbol Path: Others / UAnimBlueprint
- Source JSON Path: class/detail/Others/UAnimBlueprint.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimBlueprint.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

An Anim Blueprint is essentially a specialized Blueprint whose graphs control the animation of a Skeletal Mesh.
  It can perform blending of animations, directly control the bones of the skeleton, and output a final pose
  for a Skeletal Mesh each frame.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetSkeleton | USkeleton * | The kind of skeleton that animation graphs compiled from the blueprint will animate |  |
| Groups | TArray < FAnimGroupInfo > |  |  |
| bUseMultiThreadedAnimationUpdate | bool | Allows this anim Blueprint to update its native update, blend tree, montages and asset players on<br>	  a worker thread. The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded <br>	  Animation Update" should be set. |  |
| bWarnAboutBlueprintUsage | bool | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |  |

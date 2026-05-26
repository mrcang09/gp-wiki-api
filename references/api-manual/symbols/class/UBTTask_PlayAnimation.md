# UBTTask_PlayAnimation

- Symbol Type: class
- Symbol Path: Others / UBTTask_PlayAnimation
- Source JSON Path: class/detail/Others/UBTTask_PlayAnimation.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_PlayAnimation.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Play indicated AnimationAsset on Pawn controlled by BT 
 	Note that this node is generic and is handing multiple special cases,
 	If you want a more efficient solution you'll need to implement it yourself (or wait for our BTTask_PlayCharacterAnimation)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimationToPlay | UAnimationAsset * | Animation asset to play. Note that it needs to match the skeleton of pawn this BT is controlling |  |
| bLooping | uint32 |  |  |
| bNonBlocking | uint32 | if true the task will just trigger the animation and instantly finish. Fire and Forget. |  |
| MyOwnerComp | UBehaviorTreeComponent * |  |  |
| CachedSkelMesh | USkeletalMeshComponent * |  |  |

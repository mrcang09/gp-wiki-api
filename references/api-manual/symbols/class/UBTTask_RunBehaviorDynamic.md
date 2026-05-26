# UBTTask_RunBehaviorDynamic

- Symbol Type: class
- Symbol Path: Others / UBTTask_RunBehaviorDynamic
- Source JSON Path: class/detail/Others/UBTTask_RunBehaviorDynamic.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehaviorDynamic.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

RunBehaviorDynamic task allows pushing subtrees on execution stack.
  Subtree asset can be assigned at runtime with SetDynamicSubtree function of BehaviorTreeComponent.
 
  Does NOT support subtree's root level decorators!

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InjectionTag | FGameplayTag | Gameplay tag that will identify this task for subtree injection |  |
| DefaultBehaviorAsset | UBehaviorTree * | default behavior to run |  |
| BehaviorAsset | UBehaviorTree * | current subtree |  |

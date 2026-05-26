# UBTTask_RunBehavior

- Symbol Type: class
- Symbol Path: Others / UBTTask_RunBehavior
- Source JSON Path: class/detail/Others/UBTTask_RunBehavior.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehavior.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

RunBehavior task allows pushing subtrees on execution stack.
  Subtree asset can't be changed in runtime! 
 
  This limitation is caused by support for subtree's root level decorators,
  which are injected into parent tree, and structure of running tree
  cannot be modified in runtime (see: BTNode: ExecutionIndex, MemoryOffset)
 
  Use RunBehaviorDynamic task for subtrees that need to be changed in runtime.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BehaviorAsset | UBehaviorTree * | behavior to run |  |

# UBTTaskNode

- Symbol Type: class
- Symbol Path: Others / UBTTaskNode
- Source JSON Path: class/detail/Others/UBTTaskNode.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTaskNode.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Task are leaf nodes of behavior tree, which perform actual actions
 
  Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
   - ExecuteTask
   - AbortTask
   - TickTask
   - OnMessage
 
  If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
  Template nodes are shared across all behavior tree components using the same tree asset and must store
  their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Services | TArray < UBTService * > | service nodes |  |
| bIgnoreRestartSelf | uint32 | if set, task search will be discarded when this task is selected to execute but is already running |  |

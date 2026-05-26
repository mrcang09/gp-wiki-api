# UBTDecorator

- Symbol Type: class
- Symbol Path: Others / UBTDecorator
- Source JSON Path: class/detail/Others/UBTDecorator.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Decorators are supporting nodes placed on parent-child connection, that receive notification about execution flow and can be ticked
 
  Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
   - OnNodeActivation
   - OnNodeDeactivation
   - OnNodeProcessed
   - OnBecomeRelevant (from UBTAuxiliaryNode)
   - OnCeaseRelevant (from UBTAuxiliaryNode)
   - TickNode (from UBTAuxiliaryNode)
 
  If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
  Template nodes are shared across all behavior tree components using the same tree asset and must store
  their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInverseCondition | uint32 | if set, condition check result will be inversed |  |
| FlowAbortMode | TEnumAsByte < EBTFlowAbortMode :: Type > | flow controller settings |  |

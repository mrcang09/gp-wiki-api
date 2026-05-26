# UBTTask_GameplayTaskBase

- Symbol Type: class
- Symbol Path: Others / UBTTask_GameplayTaskBase
- Source JSON Path: class/detail/Others/UBTTask_GameplayTaskBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_GameplayTaskBase.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Base class for managing gameplay tasks
  Since AITask doesn't have any kind of successfailed results, default implemenation will only return EBTNode::Succeeded
 
  In your ExecuteTask:
  - use NewBTAITask() helper to create task
  - initialize task with values if needed
  - use StartGameplayTask() helper to execute and get node result

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bWaitForGameplayTask | uint32 | if set, behavior tree task will wait until gameplay tasks finishes |  |

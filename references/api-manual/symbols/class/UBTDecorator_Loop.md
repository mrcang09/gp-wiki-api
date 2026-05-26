# UBTDecorator_Loop

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_Loop
- Source JSON Path: class/detail/Others/UBTDecorator_Loop.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Loop.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Loop decorator node.
  A decorator node that bases its condition on whether its loop counter has been exceeded.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NumLoops | int32 | number of executions |  |
| bInfiniteLoop | bool | infinite loop |  |
| InfiniteLoopTimeoutTime | float | timeout (when looping infinitely, when we finish a loop we will check whether we have spent this time looping, if we have we will stop looping). A negative value means loop forever. |  |

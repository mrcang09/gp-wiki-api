# UGameplayTask_TimeLimitedExecution

- Symbol Type: class
- Symbol Path: Others / UGameplayTask_TimeLimitedExecution
- Source JSON Path: class/detail/Others/UGameplayTask_TimeLimitedExecution.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_TimeLimitedExecution.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

Adds time limit for running a child task
  - child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner 
  - activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
  - OnFinished and OnTimeExpired are mutually exclusive

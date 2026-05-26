# UGameplayTask

- Symbol Type: class
- Symbol Path: Others / UGameplayTask
- Source JSON Path: class/detail/Others/UGameplayTask.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceName | FName | This name allows us to find the task later so that we can end it. |  |
| ResourceOverlapPolicy | ETaskResourceOverlapPolicy |  |  |
| ChildTask | UGameplayTask * | child task instance |  |

## Functions

### ReadyForActivation

Called to trigger the actual task once the delegates have been set up

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EndTask

Called explicitly to end the task (usually by the task itself). Calls OnDestroy.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

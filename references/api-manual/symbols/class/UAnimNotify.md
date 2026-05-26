# UAnimNotify

- Symbol Type: class
- Symbol Path: Others / UAnimNotify
- Source JSON Path: class/detail/Others/UAnimNotify.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bCheckAnimIsolation | bool |  |  |
| bCheckAnimIsolation_OnlyNewFPP | bool |  |  |
| bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode | bool |  |  |

## Functions

### GetNotifyName

Implementable event to get a custom name for the notify

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### Received_Notify

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshComp | USkeletalMeshComponent *  |  |  |
| Animation | UAnimSequenceBase *  |  |  |
| InvokeAnimInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

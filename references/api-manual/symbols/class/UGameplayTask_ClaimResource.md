# UGameplayTask_ClaimResource

- Symbol Type: class
- Symbol Path: Others / UGameplayTask_ClaimResource
- Source JSON Path: class/detail/Others/UGameplayTask_ClaimResource.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_ClaimResource.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Functions

### ClaimResource

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTaskOwner | TScriptInterface < IGameplayTaskOwnerInterface >  |  |  |
| ResourceClass | TSubclassOf < UGameplayTaskResource >  |  |  |
| Priority | uint8  |  |  |
| TaskInstanceName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameplayTask_ClaimResource *  |  |  |

### ClaimResources

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTaskOwner | TScriptInterface < IGameplayTaskOwnerInterface >  |  |  |
| ResourceClasses | TArray < TSubclassOf < UGameplayTaskResource > >  |  |  |
| Priority | uint8  |  |  |
| TaskInstanceName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameplayTask_ClaimResource *  |  |  |

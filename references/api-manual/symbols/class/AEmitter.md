# AEmitter

- Symbol Type: class
- Symbol Path: Others / AEmitter
- Source JSON Path: class/detail/Others/AEmitter.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AEmitter.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParticleSystemComponent | UParticleSystemComponent * |  |  |
| bDestroyOnSystemFinish | uint32 |  |  |
| bPostUpdateTickGroup | uint32 |  |  |
| bCurrentlyActive | uint32 | used to update status of toggleable level placed emitters on clients |  |

## Functions

### OnParticleSystemFinished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FinishedComponent | UParticleSystemComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRep_bCurrentlyActive

Replication Notification Callbacks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Activate

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Deactivate

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ToggleActive

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsActive

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetTemplate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTemplate | UParticleSystem * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFloatParameter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Param | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVectorParameter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Param | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColorParameter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Param | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActorParameter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Param | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMaterialParameter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| Param | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

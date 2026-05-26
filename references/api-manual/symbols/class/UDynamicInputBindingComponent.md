# UDynamicInputBindingComponent

- Symbol Type: class
- Symbol Path: Others / UDynamicInputBindingComponent
- Source JSON Path: class/detail/Others/UDynamicInputBindingComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDynamicInputBindingComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionBindingClusters | TArray < FActionBindingCluster > |  |  |
| AxisBindingClusters | TArray < FAxisBindingCluster > |  |  |

## Functions

### BindAction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionName | FName &  |  |  |
| ActorInputEvent | EActorInputEvent  |  |  |
| FunctionName | FName &  |  |  |
| bConsumeInput | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindAxis

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisName | FName &  |  |  |
| FunctionName | FName &  |  |  |
| bConsumeInput | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveActionBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveAxisBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindActionCluster

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindAxisCluster

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveActionClusterBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveAxisClusterBinding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

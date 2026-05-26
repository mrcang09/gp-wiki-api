# UBlackboardComponent

- Symbol Type: class
- Symbol Path: Others / UBlackboardComponent
- Source JSON Path: class/detail/Others/UBlackboardComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BrainComp | UBrainComponent * | cached behavior tree component |  |
| BlackboardAsset | UBlackboardData * | data asset defining entries |  |
| KeyInstances | TArray < UBlackboardKeyType * > | instanced keys with custom data allocations |  |

## Functions

### GetValueAsObject

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### GetValueAsClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  |  |  |

### GetValueAsEnum

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### GetValueAsInt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetValueAsFloat

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetValueAsBool

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetValueAsString

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetValueAsName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### GetValueAsVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetValueAsRotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### SetValueAsObject

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| ObjectValue | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| ClassValue | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsEnum

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| EnumValue | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsInt

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| IntValue | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsFloat

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| FloatValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsBool

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| BoolValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsString

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| StringValue | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| NameValue | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| VectorValue | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetValueAsRotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| VectorValue | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsVectorValueSet

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetLocationFromEntry

return false if call failed (most probably no such entry in BB)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| ResultLocation | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetRotationFromEntry

return false if call failed (most probably no such entry in BB)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName &  |  |  |
| ResultRotation | FRotator & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClearValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyName | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

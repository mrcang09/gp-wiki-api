# UEnvQueryGenerator_BlueprintBase

- Symbol Type: class
- Symbol Path: Others / UEnvQueryGenerator_BlueprintBase
- Source JSON Path: class/detail/Others/UEnvQueryGenerator_BlueprintBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_BlueprintBase.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GeneratorsActionDescription | FText | A short description of what test does, like "Generate pawn named Joe" |  |
| Context | TSubclassOf < UEnvQueryContext > | context |  |
| GeneratedItemType | TSubclassOf < UEnvQueryItemType > | @todo this should show up only in the generator's BP, but <br>	 	due to the way EQS editor is generating widgets it's there as well<br>	 	It's a bug and we'll fix it |  |

## Functions

### DoItemGeneration

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ContextLocations | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddGeneratedVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GeneratedVector | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddGeneratedActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GeneratedActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetQuerier

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject * |  |  |

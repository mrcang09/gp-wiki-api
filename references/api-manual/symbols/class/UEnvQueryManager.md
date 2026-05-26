# UEnvQueryManager

- Symbol Type: class
- Symbol Path: Others / UEnvQueryManager
- Source JSON Path: class/detail/Others/UEnvQueryManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryManager.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceCache | TArray < FEnvQueryInstanceCache > | cache of instances |  |
| LocalContexts | TArray < UEnvQueryContext * > | local cache of context objects for managing BP based objects |  |
| GCShieldedWrappers | TArray < UEnvQueryInstanceBlueprintWrapper * > |  |  |
| MaxAllowedTestingTime | float | how long are we allowed to test per update, in seconds. |  |
| bTestQueriesUsingBreadth | bool | whether we update EQS queries based on:<br>	    or test an entire query before moving to the next one (depth). |  |
| QueryCountWarningThreshold | int32 | if greater than zero, we will warn once when the number of queries is greater than or equal to this number, and log the queries out |  |
| QueryCountWarningInterval | double | how often (in seconds) we will warn about the number of queries (allows us to catch multiple occurrences in a session) |  |

## Functions

### RunEQSQuery

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| QueryTemplate | UEnvQuery *  |  |  |
| Querier | UObject *  |  |  |
| RunMode | TEnumAsByte < EEnvQueryRunMode :: Type >  |  |  |
| WrapperClass | TSubclassOf < UEnvQueryInstanceBlueprintWrapper > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UEnvQueryInstanceBlueprintWrapper *  |  |  |

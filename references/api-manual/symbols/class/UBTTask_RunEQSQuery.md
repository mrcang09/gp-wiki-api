# UBTTask_RunEQSQuery

- Symbol Type: class
- Symbol Path: Others / UBTTask_RunEQSQuery
- Source JSON Path: class/detail/Others/UBTTask_RunEQSQuery.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunEQSQuery.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Description

Run Environment Query System Query task node.
  Runs the specified environment query when executed.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QueryTemplate | UEnvQuery * | query to run |  |
| QueryParams | TArray < FEnvNamedValue > | optional parameters for query |  |
| QueryConfig | TArray < FAIDynamicParam > |  |  |
| RunMode | TEnumAsByte < EEnvQueryRunMode :: Type > | determines which item will be stored (All = only first matching) |  |
| EQSQueryBlackboardKey | FBlackboardKeySelector | blackboard key storing an EQS query template |  |
| bUseBBKey | bool |  |  |
| EQSRequest | FEQSParametrizedQueryExecutionRequest |  |  |

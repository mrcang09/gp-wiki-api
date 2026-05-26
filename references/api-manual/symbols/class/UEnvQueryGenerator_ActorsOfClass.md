# UEnvQueryGenerator_ActorsOfClass

- Symbol Type: class
- Symbol Path: Others / UEnvQueryGenerator_ActorsOfClass
- Source JSON Path: class/detail/Others/UEnvQueryGenerator_ActorsOfClass.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_ActorsOfClass.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SearchedActorClass | TSubclassOf < AActor > |  |  |
| GenerateOnlyActorsInRadius | FAIDataProviderBoolValue | If true, this will only returns actors of the specified class within the SearchRadius of the SearchCenter context.  If false, it will return ALL actors of the specified class in the world. |  |
| SearchRadius | FAIDataProviderFloatValue | Max distance of path between point and context.  NOTE: Zero and negative values will never return any results if<br>	   UseRadius is true.  "Within" requires Distance < Radius.  Actors ON the circle (Distance == Radius) are excluded. |  |
| SearchCenter | TSubclassOf < UEnvQueryContext > | context |  |

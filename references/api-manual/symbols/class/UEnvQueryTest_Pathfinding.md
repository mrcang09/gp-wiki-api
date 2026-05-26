# UEnvQueryTest_Pathfinding

- Symbol Type: class
- Symbol Path: Others / UEnvQueryTest_Pathfinding
- Source JSON Path: class/detail/Others/UEnvQueryTest_Pathfinding.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Pathfinding.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TestMode | TEnumAsByte < EEnvTestPathfinding :: Type > | testing mode |  |
| Context | TSubclassOf < UEnvQueryContext > | context: other end of pathfinding test |  |
| PathFromContext | FAIDataProviderBoolValue | pathfinding direction |  |
| SkipUnreachable | FAIDataProviderBoolValue | if set, items with failed path will be invalidated (PathCost, PathLength) |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > | navigation filter to use in pathfinding |  |

# UEnvQueryGenerator_OnCircle

- Symbol Type: class
- Symbol Path: Others / UEnvQueryGenerator_OnCircle
- Source JSON Path: class/detail/Others/UEnvQueryGenerator_OnCircle.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_OnCircle.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CircleRadius | FAIDataProviderFloatValue | max distance of path between point and context |  |
| SpaceBetween | FAIDataProviderFloatValue | items will be generated on a circle this much apart |  |
| NumberOfPoints | FAIDataProviderIntValue | this many items will be generated on a circle |  |
| PointOnCircleSpacingMethod | EPointOnCircleSpacingMethod | how we are choosing where the points are in the circle |  |
| ArcDirection | FEnvDirection | If you generate items on a piece of circle you define direction of Arc cut here |  |
| ArcAngle | FAIDataProviderFloatValue | If you generate items on a piece of circle you define angle of Arc cut here |  |
| AngleRadians | float |  |  |
| CircleCenter | TSubclassOf < UEnvQueryContext > | context |  |
| bIgnoreAnyContextActorsWhenGeneratingCircle | bool | ignore tracing into context actors when generating the circle |  |
| CircleCenterZOffset | FAIDataProviderFloatValue | context offset |  |
| TraceData | FEnvTraceData | horizontal trace for nearest obstacle |  |
| bDefineArc | uint32 |  |  |

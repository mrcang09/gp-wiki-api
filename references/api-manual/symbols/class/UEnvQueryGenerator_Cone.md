# UEnvQueryGenerator_Cone

- Symbol Type: class
- Symbol Path: Others / UEnvQueryGenerator_Cone
- Source JSON Path: class/detail/Others/UEnvQueryGenerator_Cone.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Cone.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AlignedPointsDistance | FAIDataProviderFloatValue | Distance between each point of the same angle |  |
| ConeDegrees | FAIDataProviderFloatValue | Maximum degrees of the generated cone |  |
| AngleStep | FAIDataProviderFloatValue | The step of the angle increase. Angle step must be >=1<br>	   Smaller values generate less items |  |
| Range | FAIDataProviderFloatValue | Generation distance |  |
| CenterActor | TSubclassOf < UEnvQueryContext > | The actor (or actors) that will generate a cone in their facing direction |  |
| bIncludeContextLocation | uint8 | Whether to include CenterActors' locations when generating items. <br>	 	Note that this option skips the MinAngledPointsDistance parameter. |  |

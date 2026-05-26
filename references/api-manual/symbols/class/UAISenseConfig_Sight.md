# UAISenseConfig_Sight

- Symbol Type: class
- Symbol Path: Others / UAISenseConfig_Sight
- Source JSON Path: class/detail/Others/UAISenseConfig_Sight.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Sight.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Implementation | TSubclassOf < UAISense_Sight > |  |  |
| SightRadius | float | Maximum sight distance to notice a target. |  |
| LoseSightRadius | float | Maximum sight distance to see target that has been already seen. |  |
| PeripheralVisionAngleDegrees | float | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. <br>	 	The value represents the angle measured in relation to the forward vector, not the whole range. |  |
| DetectionByAffiliation | FAISenseAffiliationFilter |  |  |
| AutoSuccessRangeFromLastSeenLocation | float | If not an InvalidRange (which is the default), we will always be able to see the target that has already been seen if they are within this range of their last seen location. |  |

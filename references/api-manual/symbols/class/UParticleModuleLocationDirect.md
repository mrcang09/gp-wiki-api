# UParticleModuleLocationDirect

- Symbol Type: class
- Symbol Path: Others / UParticleModuleLocationDirect
- Source JSON Path: class/detail/Others/UParticleModuleLocationDirect.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationDirect.json
- Mirrored At (UTC): 2026-05-19 08:23:37Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Location | FRawDistributionVector | The location of the particle at a give time. Retrieved using the particle RelativeTime. <br>	 	IMPORTANT: the particle location is set to this value, thereby over-writing any previous module impacts. |  |
| LocationOffset | FRawDistributionVector | An offset to apply to the position retrieved from the Location calculation. <br>	 	The offset is retrieved using the EmitterTime. <br>	 	The offset will remain constant over the life of the particle. |  |
| ScaleFactor | FRawDistributionVector | Scales the velocity of the object at a given point in the time-line. |  |
| Direction | FRawDistributionVector | Currently unused. |  |

# UParticleModuleAcceleration

- Symbol Type: class
- Symbol Path: Others / UParticleModuleAcceleration
- Source JSON Path: class/detail/Others/UParticleModuleAcceleration.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAcceleration.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Acceleration | FRawDistributionVector | The initial acceleration of the particle.<br>	 	Value is obtained using the EmitterTime at particle spawn.<br>	 	Each frame, the current and base velocity of the particle <br>	 	is then updated using the formula <br>	 		velocity += acceleration  DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |  |
| bApplyOwnerScale | uint32 | If true, then apply the particle system components scale <br>	 	to the acceleration value. |  |

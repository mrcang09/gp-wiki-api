# UParticleModuleCollisionGPU

- Symbol Type: class
- Symbol Path: Others / UParticleModuleCollisionGPU
- Source JSON Path: class/detail/Others/UParticleModuleCollisionGPU.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCollisionGPU.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Resilience | FRawDistributionFloat | Dampens the velocity of a particle in the direction normal to the<br>	  collision plane. |  |
| ResilienceScaleOverLife | FRawDistributionFloat | Modulates the resilience of the particle over its lifetime. |  |
| Friction | float | Friction applied to all particles during a collision or while moving<br>	  along a surface. |  |
| RandomSpread | float | Controls how wide the bouncing particles are distributed (0 = disabled). |  |
| RandomDistribution | float | Controls bouncing particles distribution (1 = uniform distribution; 2 = squared distribution). |  |
| RadiusScale | float | Scale applied to the size of the particle to obtain the collision radius. |  |
| RadiusBias | float | Bias applied to the collision radius. |  |
| Response | TEnumAsByte < EParticleCollisionResponse :: Type > | How particles respond to a collision event. |  |
| CollisionMode | TEnumAsByte < EParticleCollisionMode :: Type > |  |  |

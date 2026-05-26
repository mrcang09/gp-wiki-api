# UParticleModuleSpawn

- Symbol Type: class
- Symbol Path: Others / UParticleModuleSpawn
- Source JSON Path: class/detail/Others/UParticleModuleSpawn.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSpawn.json
- Mirrored At (UTC): 2026-05-19 08:23:37Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Rate | FRawDistributionFloat | The rate at which to spawn particles. |  |
| RateScale | FRawDistributionFloat | The scalar to apply to the rate. |  |
| ParticleBurstMethod | TEnumAsByte < EParticleBurstMethod > | The method to utilize when burst-emitting particles. |  |
| BurstList | TArray < FParticleBurst > | The array of burst entries. |  |
| BurstScale | FRawDistributionFloat | Scale all burst entries by this amount. |  |
| bApplyGlobalSpawnRateScale | uint32 | If true, the SpawnRate will be scaled by the global CVar r.EmitterSpawnRateScale |  |

# UParticleLODLevel

- Symbol Type: class
- Symbol Path: Others / UParticleLODLevel
- Source JSON Path: class/detail/Others/UParticleLODLevel.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleLODLevel.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Level | int32 | The index value of the LOD level |  |
| bEnabled | uint32 | True if the LOD level is enabled, meaning it should be updated and rendered. |  |
| RequiredModule | UParticleModuleRequired * | The required module for this LOD level |  |
| Modules | TArray < UParticleModule * > | An array of particle modules that contain the adjusted data for the LOD level |  |
| TypeDataModule | UParticleModuleTypeDataBase * |  |  |
| SpawnModule | UParticleModuleSpawn * | The SpawnRateBurst module - required by all emitters. |  |
| EventGenerator | UParticleModuleEventGenerator * | The optional EventGenerator module. |  |
| SpawningModules | TArray < UParticleModuleSpawnBase * > | SpawningModules - These are called to determine how many particles to spawn. |  |
| SpawnModules | TArray < UParticleModule * > | SpawnModules - These are called when particles are spawned. |  |
| UpdateModules | TArray < UParticleModule * > | UpdateModules - These are called when particles are updated. |  |
| OrbitModules | TArray < UParticleModuleOrbit * > | OrbitModules <br>	 	These are used to do offsets of the sprite from the particle location. |  |
| EventReceiverModules | TArray < UParticleModuleEventReceiverBase * > | Event receiver modules only! |  |
| ConvertedModules | uint32 |  |  |
| PeakActiveParticles | int32 |  |  |
| ActualPeakParticles | int32 |  |  |

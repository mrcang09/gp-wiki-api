# UParticleModuleEventReceiverSpawn

- Symbol Type: class
- Symbol Path: Others / UParticleModuleEventReceiverSpawn
- Source JSON Path: class/detail/Others/UParticleModuleEventReceiverSpawn.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleEventReceiverSpawn.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SpawnCount | FRawDistributionFloat | The number of particles to spawn. |  |
| bUseParticleTime | uint32 | For Death-based event receiving, if this is true, it indicates that the <br>	 	ParticleTime of the event should be used to look-up the SpawnCount.<br>	 	Otherwise (and in all other events received), use the emitter time of <br>	 	the event. |  |
| bUsePSysLocation | uint32 | If true, use the location of the particle system component for spawning.<br>	 	if false (default), use the location of the particle event. |  |
| bInheritVelocity | uint32 | If true, use the velocity of the dying particle as the start velocity of <br>	 	the spawned particle. |  |
| InheritVelocityScale | FRawDistributionVector | If bInheritVelocity is true, scale the velocity with this. |  |
| PhysicalMaterials | TArray < UPhysicalMaterial * > | Array of physical materials that can be used to allow or ban a specific set of materials when receiving collision events. |  |
| bBanPhysicalMaterials | uint32 | When true, the PhysicalMaterials list is used to ban specified materials for collision events but allow all others.<br>		When false, the PhysicalMaterials list is used to allow only specified materials for collision events and ban all others. |  |

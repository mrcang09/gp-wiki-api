# FOrbitOptions

- Symbol Type: struct
- Symbol Path: FOrbitOptions
- Source JSON Path: cppstruct/detail/FOrbitOptions.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FOrbitOptions.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Container struct for holding options on the data updating for the module.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bProcessDuringSpawn | uint32 | Whether to process the data during spawning. |  |
| bProcessDuringUpdate | uint32 | Whether to process the data during updating. |  |
| bUseEmitterTime | uint32 | Whether to use emitter time during data retrieval. |  |
| bUseParticleIDInsteadOfTime | uint32 | Whether to use particle ID instead of time (emitter time or particle time). |  |
| ParticleIDLoop | uint32 | If >0, the distribution input will be ParticleID % ParticleIDLoop |  |

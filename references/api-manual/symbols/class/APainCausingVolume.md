# APainCausingVolume

- Symbol Type: class
- Symbol Path: Others / APainCausingVolume
- Source JSON Path: class/detail/Others/APainCausingVolume.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/APainCausingVolume.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

Volume that causes damage over time to any Actor that overlaps its collision.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bPainCausing | uint32 | Whether volume currently causes damage. |  |
| DamagePerSec | float | Damage done per second to actors in this volume when bPainCausing=true |  |
| DamageType | TSubclassOf < UDamageType > | Type of damage done |  |
| PainInterval | float | If pain causing, time between damage applications. |  |
| bEntryPain | uint32 | if bPainCausing, cause pain when something enters the volume in addition to damage each second |  |
| BACKUP_bPainCausing | uint32 | Checkpointed bPainCausing value |  |
| DamageInstigator | AController * | Controller that gets credit for any damage caused by this volume |  |

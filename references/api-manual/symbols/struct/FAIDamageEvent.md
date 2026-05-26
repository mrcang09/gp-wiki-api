# FAIDamageEvent

- Symbol Type: struct
- Symbol Path: FAIDamageEvent
- Source JSON Path: cppstruct/detail/FAIDamageEvent.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAIDamageEvent.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Amount | float | Damage taken by DamagedActor.<br>	 	@Note 0-damage events do not get ignored |  |
| Location | FVector | Event's "Location", or what will be later treated as the perceived location for this sense.<br>	 	If not set, HitLocation will be used, if that is unset too DamagedActor's location |  |
| HitLocation | FVector | Event's additional spatial information<br>	 	@TODO document |  |
| DamagedActor | AActor * | Damaged actor |  |
| Instigator | AActor * | Actor that instigated damage. Can be None |  |

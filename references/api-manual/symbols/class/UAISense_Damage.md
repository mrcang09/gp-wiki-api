# UAISense_Damage

- Symbol Type: class
- Symbol Path: Others / UAISense_Damage
- Source JSON Path: class/detail/Others/UAISense_Damage.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Damage.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RegisteredEvents | TArray < FAIDamageEvent > |  |  |

## Functions

### ReportDamageEvent

EventLocation will be reported as Instigator's location at the moment of event happening

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| DamagedActor | AActor *  |  |  |
| Instigator | AActor *  |  |  |
| DamageAmount | float  |  |  |
| EventLocation | FVector  |  |  |
| HitLocation | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

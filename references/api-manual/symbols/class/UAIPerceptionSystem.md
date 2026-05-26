# UAIPerceptionSystem

- Symbol Type: class
- Symbol Path: Others / UAIPerceptionSystem
- Source JSON Path: class/detail/Others/UAIPerceptionSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

By design checks perception between hostile teams

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Senses | TArray < UAISense * > |  |  |
| PerceptionAgingRate | float |  |  |

## Functions

### ReportEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PerceptionEvent | UAISenseEvent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReportPerceptionEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PerceptionEvent | UAISenseEvent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RegisterPerceptionStimuliSource

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Sense | TSubclassOf < UAISense >  |  |  |
| Target | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetSenseClassForStimulus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Stimulus | FAIStimulus & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSubclassOf < UAISense >  |  |  |

### OnPerceptionStimuliSourceEndPlay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| EndPlayReason | EEndPlayReason :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

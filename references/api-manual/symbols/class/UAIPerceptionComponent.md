# UAIPerceptionComponent

- Symbol Type: class
- Symbol Path: Others / UAIPerceptionComponent
- Source JSON Path: class/detail/Others/UAIPerceptionComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
 	and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SensesConfig | TArray < UAISenseConfig * > |  |  |
| DominantSense | TSubclassOf < UAISense > | Indicated sense that takes precedence over other senses when determining sensed actor's location. <br>	 	Should be set to one of the senses configured in SensesConfig, or None. |  |
| AIOwner | AAIController * |  |  |

## Functions

### OnOwnerEndPlay

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| EndPlayReason | EEndPlayReason :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RequestStimuliListenerUpdate

Notifies AIPerceptionSystem to update properties for this "stimuli listener"

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetPerceivedHostileActors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentlyPerceivedActors

If SenseToUse is none all actors currently perceived in any way will get fetched

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseToUse | TSubclassOf < UAISense >  |  |  |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetKnownPerceivedActors

If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseToUse | TSubclassOf < UAISense >  |  |  |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPerceivedActors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseToUse | TSubclassOf < UAISense >  |  |  |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorsPerception

Retrieves whatever has been sensed about given actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| Info | FActorPerceptionBlueprintInfo & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetSenseEnabled

Note that this works only if given sense has been already configured for
	 	this component instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseClass | TSubclassOf < UAISense >  |  |  |
| bEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

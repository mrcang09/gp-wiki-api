# UAISense_Blueprint

- Symbol Type: class
- Symbol Path: Others / UAISense_Blueprint
- Source JSON Path: class/detail/Others/UAISense_Blueprint.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Blueprint.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ListenerDataType | TSubclassOf < UUserDefinedStruct > |  |  |
| ListenerContainer | TArray < UAIPerceptionComponent * > |  |  |
| UnprocessedEvents | TArray < UAISenseEvent * > |  |  |

## Functions

### OnUpdate

returns requested amount of time to pass until next frame. 
	 	Return 0 to get update every frame (WARNING: hits performance)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EventsToProcess | TArray < UAISenseEvent * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### OnListenerRegistered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorListener | AActor *  |  |  |
| PerceptionComponent | UAIPerceptionComponent * | is ActorListener's AIPerceptionComponent instance |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnListenerUpdated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorListener | AActor *  |  |  |
| PerceptionComponent | UAIPerceptionComponent * | is ActorListener's AIPerceptionComponent instance |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnListenerUnregistered

called when a listener unregistered from this sense. Most often this is called due to actor's death

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorListener | AActor *  |  |  |
| PerceptionComponent | UAIPerceptionComponent * | is ActorListener's AIPerceptionComponent instance |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllListenerActors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ListenerActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllListenerComponents

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ListenerComponents | TArray < UAIPerceptionComponent * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnNewPawn

called when sense's instance gets notified about new pawn that has just been spawned

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

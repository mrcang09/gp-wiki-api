# UGameplayTask_SpawnActor

- Symbol Type: class
- Symbol Path: Others / UGameplayTask_SpawnActor
- Source JSON Path: class/detail/Others/UGameplayTask_SpawnActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_SpawnActor.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

Convenience task for spawning actors (optionally limiting the spawning to the network authority). If not the net authority, we will not spawn 
 	and Success will not be called. The nice thing this adds is the ability to modify expose on spawn properties while also implicitly checking 
 	network role before spawning.
 
 	Though this task doesn't do much - games can implement similar tasks that carry out game specific rules. For example a 'SpawnProjectile'
 	task that limits the available classes to the games projectile class, and that does game specific stuff on spawn (for example, determining
 	firing position from a weapon attachment).
 	
 	Long term we can also use this task as a sync point. If the executing client could wait execution until the server creates and replicates the 
 	actor down to him. We could potentially also use this to do predictive actor spawning  reconciliation.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClassToSpawn | TSubclassOf < AActor > |  |  |

## Functions

### SpawnActor

Spawn new Actor on the network authority (server)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskOwner | TScriptInterface < IGameplayTaskOwnerInterface >  |  |  |
| SpawnLocation | FVector  |  |  |
| SpawnRotation | FRotator  |  |  |
| Class | TSubclassOf < AActor >  |  |  |
| bSpawnOnlyOnAuthority | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameplayTask_SpawnActor *  |  |  |

### BeginSpawningActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SpawnedActor | AActor * & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FinishSpawningActor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SpawnedActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

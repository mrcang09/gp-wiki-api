# UGameplayTasksComponent

- Symbol Type: class
- Symbol Path: Others / UGameplayTasksComponent
- Source JSON Path: class/detail/Others/UGameplayTasksComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTasksComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

The core ActorComponent for interfacing with the GameplayAbilities System

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SimulatedTasks | TArray < UGameplayTask * > | Tasks that run on simulated proxies |  |
| AutonomousTasks | TArray < UGameplayTask * > |  |  |
| TaskPriorityQueue | TArray < UGameplayTask * > |  |  |
| TickingTasks | TArray < UGameplayTask * > | Array of currently active UGameplayTask that require ticking |  |
| KnownTasks | TArray < UGameplayTask * > | All known tasks (processed by this component) referenced for GC |  |

## Functions

### OnRep_SimulatedTasks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_AutonomousTasks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### K2_RunGameplayTask

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TaskOwner | TScriptInterface < IGameplayTaskOwnerInterface >  |  |  |
| Task | UGameplayTask *  |  |  |
| Priority | uint8  |  |  |
| AdditionalRequiredResources | TArray < TSubclassOf < UGameplayTaskResource > >  |  |  |
| AdditionalClaimedResources | TArray < TSubclassOf < UGameplayTaskResource > > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EGameplayTaskRunResult  |  |  |

# UChildActorComponent

- Symbol Type: class
- Symbol Path: Others / UChildActorComponent
- Source JSON Path: class/detail/Others/UChildActorComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UChildActorComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A component that spawns an Actor when registered, and destroys it when unregistered.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ChildActorClass | TSubclassOf < AActor > | The class of Actor to spawn |  |
| ChildActor | AActor * | The actor that we spawned and own |  |
| bAllowTemplateModification | bool |  |  |
| ChildActorTemplate | AActor * | Property to point to the template child actor for details panel purposes |  |
| IsDestoryChildActor | bool |  |  |
| bKeepChildActorComponet | bool |  |  |
| bEnableReplication | bool |  |  |
| bDumpChildActorLocation | bool |  |  |
| bRedirectComps | uint8 |  |  |
| bPCOnlyComps | uint8 |  |  |

## Functions

### SetChildActorClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InClass | TSubclassOf < AActor > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRep_ChildActor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CreateChildActor

Create the child actor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DestroyChildActor

Kill any currently present child actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNeedInstanceData | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

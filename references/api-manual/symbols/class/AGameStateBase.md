# AGameStateBase

- Symbol Type: class
- Symbol Path: Others / AGameStateBase
- Source JSON Path: class/detail/Others/AGameStateBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AGameStateBase.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

GameStateBase is a class that manages the game's global state, and is spawned by GameModeBase.
  It exists on both the client and the server and is fully replicated.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameModeClass | TSubclassOf < AGameModeBase > | Class of the server's game mode, assigned by GameModeBase. |  |
| AuthorityGameMode | AGameModeBase * | Instance of the current game mode, exists only on the server. For non-authority clients, this will be NULL. |  |
| SpectatorClass | TSubclassOf < ASpectatorPawn > | Class used by spectators, assigned by GameModeBase. |  |
| PlayerArray | TArray < APlayerState * > | Array of all PlayerStates, maintained on both server and clients (PlayerStates are always relevant) |  |
| bReplicatedHasBegunPlay | bool | Replicated when GameModeBase->StartPlay has been called so the client will also start play |  |
| ReplicatedWorldTimeSeconds | float | Server TimeSeconds. Useful for syncing up animation and gameplay. |  |
| ServerWorldTimeSecondsDelta | float | The difference from the local world's TimeSeconds and the server world's TimeSeconds. |  |
| ServerWorldTimeSecondsUpdateFrequency | float | Frequency that the server updates the replicated TimeSeconds from the world. Set to zero to disable periodic updates. |  |
| bRecordControllerReplay | bool | If use rec ctrl in replay |  |
| PauseInfo | bool |  |  |

## Functions

### GetServerWorldTimeSeconds

Returns the simulated TimeSeconds on the server, will be synchronized on client and server

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetServerWorldTimeSecondsForReplay

Returns the simulated TimeSeconds on the server while playing replay, with fastforward skipped time considered

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### HasBegunPlay

Returns true if the world has started play (called BeginPlay on actors)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### HasMatchStarted

Returns true if the world has started match (called MatchStarted callbacks)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetPlayerStartTime

Returns the time that should be used as when a player started

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetPlayerRespawnDelay

Returns how much time needs to be spent before a player can respawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### OnRep_GameModeClass

GameModeBase class notification callback.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_SpectatorClass

Callback when we receive the spectator class

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ReplicatedHasBegunPlay

By default calls BeginPlay and StartMatch

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ReplicatedWorldTimeSeconds

Allows clients to calculate ServerWorldTimeSecondsDelta

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldValue | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRep_RecordControllerReplay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_PauseInfo

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

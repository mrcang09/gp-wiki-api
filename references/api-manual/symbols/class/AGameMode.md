# AGameMode

- Symbol Type: class
- Symbol Path: Others / AGameMode
- Source JSON Path: class/detail/Others/AGameMode.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AGameMode.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

GameMode is a subclass of GameModeBase that behaves like a multiplayer match-based game.
  It has default behavior for picking spawn points and match state.
  If you want a simpler base, inherit from GameModeBase instead.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MatchState | FName | What match state we are currently in |  |
| bDelayedStart | uint32 | Whether the game should immediately start when the first player logs in. Affects the default behavior of ReadyToStartMatch |  |
| NumSpectators | int32 | Current number of spectators. |  |
| NumPlayers | int32 | Current number of human players. |  |
| NumBots | int32 | number of non-human players (AI controlled but participating as a player). |  |
| MinRespawnDelay | float | Minimum time before player can respawn after dying. |  |
| NumTravellingPlayers | int32 | Number of players that are still traveling from a previous map |  |
| EngineMessageClass | TSubclassOf < ULocalMessage > | Contains strings describing localized game agnostic messages. |  |
| InactivePlayerArray | TArray < APlayerState * > | PlayerStates of players who have disconnected from the server (saved in case they reconnect) |  |
| bEnabelPawnPool | bool | Weather to enable Gamemode Pawn Pool |  |
| InactivePlayerStateLifeSpan | float | Time a playerstate will stick around in an inactive state after a player logout |  |
| bHandleDedicatedServerReplays | bool | If true, dedicated servers will record replays when HandleMatchHasStartedHandleMatchHasStopped is called |  |

## Functions

### GetMatchState

Returns the current match state, this is an accessor to protect the state machine flow

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName |  |  |

### IsMatchInProgress

Returns true if the match state is InProgress or other gameplay state

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### HasMatchEnded

Returns true if the match state is WaitingPostMatch or later

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### StartMatch

Transition from WaitingToStart to InProgress. You can call this manually, will also get called if ReadyToStartMatch returns true

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EndMatch

Transition from InProgress to WaitingPostMatch. You can call this manually, will also get called if ReadyToEndMatch returns true

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RestartGame

Restart the game, by default travel to the current map

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AbortMatch

Report that a match has failed due to unrecoverable error

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### K2_OnSetMatchState

Implementable event to respond to match state changes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewState | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReadyToStartMatch

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | True if ready to Start Match. Games should override this |  |

### ReadyToEndMatch

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if ready to End Match. Games should override this |  |

### Say

Exec command to broadcast a string to all players

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Msg | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBandwidthLimit

Alters the synthetic bandwidth limit for a running game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AsyncIOBandwidthLimit | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

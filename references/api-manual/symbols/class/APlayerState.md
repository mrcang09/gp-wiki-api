# APlayerState

- Symbol Type: class
- Symbol Path: Others / APlayerState
- Source JSON Path: class/detail/Others/APlayerState.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/APlayerState.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

A PlayerState is created for every player on a server (or in a standalone game).
  PlayerStates are replicated to all clients, and contain network game relevant information about the player, such as playername, score, etc.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Score | float | Player's current score. |  |
| Ping | uint8 | Replicated compressed ping for this player (holds ping in msec divided by 4) |  |
| PlayerName | FString | Player name, or blank if none. |  |
| PlayerId | int32 | Unique net id number. Actual value varies based on current online subsystem, use it only as a guaranteed unique number per player. |  |
| bIsSpectator | uint32 | Whether this player is currently a spectator |  |
| bOnlySpectator | uint32 | Whether this player can only ever be a spectator |  |
| bIsABot | uint32 | True if this PlayerState is associated with an AIController |  |
| bIsInactive | uint32 | Means this PlayerState came from the GameMode's InactivePlayerArray |  |
| bFromPreviousLevel | uint32 | indicates this is a PlayerState from the previous level of a seamless travel,<br>	  waiting for the player to finish the transition before creating a new one<br>	  this is used to avoid preserving the PlayerState in the InactivePlayerArray if the player leaves |  |
| StartTime | int32 | Elapsed time on server when this PlayerState was first created. |  |
| EngineMessageClass | TSubclassOf < ULocalMessage > | This is used for sending game agnostic messages that can be localized |  |
| SavedNetworkAddress | FString | Used to match up InactivePlayerState with rejoining playercontroller. |  |
| UniqueId | FUniqueNetIdRepl | The id used by the network to uniquely identify a player.<br>	  NOTE: the internals of this property should never be exposed to the player as it's transient<br>	  and opaque in meaning (ie it might mean datetime followed by something else).<br>	  It is OK to use and pass around this property, though. |  |
| PingBucketSize | int32 |  |  |

## Functions

### OnRep_Score

Replication Notification Callbacks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_PlayerName

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_bIsInactive

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_UniqueId

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveOverrideWith

Can be implemented in Blueprint Child to move more properties from old to new PlayerState when reconnecting

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldPlayerState | APlayerState * | Old PlayerState, which we use to fill the new one with |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveCopyProperties

Can be implemented in Blueprint Child to move more properties from old to new PlayerState when traveling to a new level

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayerState | APlayerState * | New PlayerState, which we fill with the current properties |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# AGameState

- Symbol Type: class
- Symbol Path: Others / AGameState
- Source JSON Path: class/detail/Others/AGameState.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AGameState.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

GameState is a subclass of GameStateBase that behaves like a multiplayer match-based game.
  It is tied to functionality in GameMode.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MatchState | FName | What match state we are currently in |  |
| PreviousMatchState | FName | Previous map state, used to handle if multiple transitions happen per frame |  |
| ElapsedTime | int32 | Elapsed game time since match has started. |  |

## Functions

### OnRep_MatchState

Match state has changed

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_ElapsedTime

Gives clients the chance to do something when time gets updates

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetGeneralCampNameByCampID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CampID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetGeneralCampRelation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CampAID | int32  |  |  |
| CampBID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECampRelation  |  |  |

### GetGameModeGeneralDataAsset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameModeGeneralDataAsset * |  |  |

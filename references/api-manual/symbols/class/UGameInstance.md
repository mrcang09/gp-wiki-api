# UGameInstance

- Symbol Type: class
- Symbol Path: Others / UGameInstance
- Source JSON Path: class/detail/Others/UGameInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameInstance.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

GameInstance: high-level manager object for an instance of the running game.
  Spawned at game creation and not destroyed until game instance is shut down.
  Running as a standalone game, there will be one of these.
  Running in PIE (play-in-editor) will generate one of these per PIE instance.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EncryptedLocalPlayers | TArray < int64 > |  |  |
| LocalPlayers | TArray < ULocalPlayer * > |  |  |
| OnlineSession | UOnlineSession * | Class to manage online services |  |
| bUseEncryptLocalPlayerPtr | bool |  |  |
| DSHUD | UObject * |  |  |
| CachedConsoleVariableBunch_Groups | TArray < TArray < uint8 > > |  |  |
| CachedConsoleVariableBunch_BigWorld | TArray < uint8 > |  |  |
| CachedConsoleVariableBunch_Permanent | TArray < uint8 > |  |  |
| SpecialPakResStates | TMap < ESpecialPakID , EPakResState > |  |  |

## Functions

### ReceiveInit

Opportunity for blueprints to handle the game instance being initialized.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveShutdown

Opportunity for blueprints to handle the game instance being shutdown.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### HandleNetworkError

Opportunity for blueprints to handle network errors.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FailureType | ENetworkFailure :: Type  |  |  |
| bIsServer | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HandleTravelError

Opportunity for blueprints to handle travel errors.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FailureType | ETravelFailure :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DebugCreatePlayer

Local player access 
	
	  Debug console command to create a player.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControllerId | int32 | - The controller ID the player should accept input from. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DebugRemovePlayer

Debug console command to remove the player with a given controller ID.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControllerId | int32 | - The controller ID to search for. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetDynaConfigAndDynaCVar

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetDynaConfig

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SendConsoleVariableBunch

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CVarType | ECVarType  |  |  |
| Connection | UNetConnection * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveConsoleVariableBunch_BigWorld

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InConsoleVariablesBunch | TArray < uint8 > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveConsoleVariableBunch_Permanent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InConsoleVariablesBunch | TArray < uint8 > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableConsoleVariableBunch

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CVarType | ECVarType  |  |  |
| bMapIsBigWorld | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearConsoleVariableBunch

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CVarType | ECVarType |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetConsoleVariable

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CVarType | ECVarType |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPakResState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPakID | ESpecialPakID  |  |  |
| InPakState | EPakResState |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPakResState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPakID | ESpecialPakID |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPakResState  |  |  |

### IsPlatformSplitPakRes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPakID | ESpecialPakID |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EPakSplitState  |  |  |

### InitPakResState

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

# AGameModeBase

- Symbol Type: class
- Symbol Path: Others / AGameModeBase
- Source JSON Path: class/detail/Others/AGameModeBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AGameModeBase.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

The GameModeBase defines the game being played. It governs the game rules, scoring, what actors
  are allowed to exist in this game type, and who may enter the game.
 
  It is only instanced on the server and will never exist on the client. 
 
  A GameModeBase actor is instantiated when the level is initialized for gameplay in
  C++ UGameEngine::LoadMap().  
  
  The class of this GameMode actor is determined by (in order) either the URL ?game=xxx, 
  the GameMode Override value set in the World Settings, or the DefaultGameMode entry set 
  in the game's Project Settings.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OptionsString | FString | Save options string and parse it when needed |  |
| GameSessionClass | TSubclassOf < AGameSession > | Class of GameSession, which handles login approval and online game interface |  |
| GameStateClass | TSubclassOf < AGameStateBase > | Class of GameState associated with this GameMode. |  |
| PlayerControllerClass | TSubclassOf < APlayerController > | The class of PlayerController to spawn for players logging in. |  |
| PlayerStateClass | TSubclassOf < APlayerState > | A PlayerState of this class will be associated with every player to replicate relevant player information to all clients. |  |
| HUDClass | TSubclassOf < AHUD > | HUD class this game uses. |  |
| DefaultPawnClass | TSubclassOf < APawn > | The default pawn class used by players. |  |
| SpectatorClass | TSubclassOf < ASpectatorPawn > | The pawn class used by the PlayerController for players when spectating. |  |
| ReplaySpectatorPlayerControllerClass | TSubclassOf < APlayerController > | The PlayerController class used when spectating a network replay. |  |
| GameSession | AGameSession * | Game Session handles login approval, arbitration, online game interface |  |
| GameState | AGameStateBase * | GameState is used to replicate game state relevant properties to all clients. |  |
| DefaultPlayerName | FText | The default player name assigned to players that join with no name specified. |  |
| bUseSeamlessTravel | uint32 | Whether the game perform map travels using SeamlessTravel() which loads in the background and doesn't disconnect clients |  |
| bUnlimitedRegionZ | uint32 |  |  |
| bStartPlayersAsSpectators | uint32 | Whether players should immediately spawn when logging in, or stay as spectators until they manually spawn |  |
| bPauseable | uint32 | Whether the game is pauseable. |  |

## Functions

### GetDefaultPawnClassForController

Returns default pawn class for given controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InController | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  |  |  |

### GetNumPlayers

Returns number of active human players, excluding spectators

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetNumSpectators

Returns number of human players currently spectating

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### StartPlay

Transitions to calls BeginPlay on actors.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### HasMatchStarted

Returns true if the match start callbacks have been called

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ShouldReset

Overridable function to determine whether an Actor should have Reset called when the game has Reset called on it.
	  Default implementation returns true

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorToReset | AActor * | The actor to make a determination for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if ActorToReset should have Reset() called on it while restarting the game, |  |

### ResetLevel

Overridable function called when resetting level. This is used to reset the game state while staying in the same map
	  Default implementation calls Reset() on all actors except GameMode and Controllers

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReturnToMainMenuHost

Return to main menu, and disconnect any players

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### K2_PostLogin

Notification that a player has successfully logged in, and has been given a player controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnLogout

Implementable event when a Controller with a PlayerState leaves the game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ExitingController | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HandleStartingNewPlayer

Signals that a player is ready to enter the game, which may start it up

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MustSpectate

Returns true if NewPlayerController may only join the server as a spectator.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayerController | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CanSpectate

Return whether Viewer is allowed to spectate from the point of view of ViewTarget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Viewer | APlayerController *  |  |  |
| ViewTarget | APlayerState * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ChangeName

Sets the name for a controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Controller | AController *  | The controller of the player to change the name of |  |
| NewName | FString &  | The name to set the player to |  |
| bNameChange | bool | Whether the name is changing or if this is the first time it has been set |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnChangeName

Overridable event for GameMode blueprint to respond to a change name call

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Other | AController *  |  |  |
| NewName | FString &  | The name to set the player to |  |
| bNameChange | bool | Whether the name is changing or if this is the first time it has been set |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ChoosePlayerStart

Return the 'best' player start for this player to spawn from
	  Default implementation looks for a random unoccupied spot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | AController * | is the controller for whom we are choosing a playerstart |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  AActor chosen as player start (usually a PlayerStart) |  |

### FindPlayerStart

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | AController *  | The AController for whom we are choosing a Player Start |  |
| IncomingName | FString & | Specifies the tag of a Player Start to use |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  Actor chosen as player start (usually a PlayerStart) |  |

### K2_FindPlayerStart

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | AController *  | The AController for whom we are choosing a Player Start |  |
| IncomingName | FString & | Specifies the tag of a Player Start to use |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor *  |  Actor chosen as player start (usually a PlayerStart) |  |

### PlayerCanRestart

Returns true if it's valid to call RestartPlayer. By default will call Player->CanRestartPlayer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RestartPlayer

Tries to spawn the player's pawn, at the location returned by FindPlayerStart

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RestartPlayerAtPlayerStart

Tries to spawn the player's pawn at the specified actor's location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController *  |  |  |
| StartSpot | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RestartPlayerAtTransform

Tries to spawn the player's pawn at a specific location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController *  |  |  |
| SpawnTransform | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SpawnDefaultPawnFor

Called during RestartPlayer to actually spawn the player's pawn, when using a start spot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController *  | - Controller for whom this pawn is spawned |  |
| StartSpot | AActor * | - Actor at which to spawn pawn |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn *  | a pawn of the default pawn class |  |

### SpawnDefaultPawnAtTransform

Called during RestartPlayer to actually spawn the player's pawn, when using a transform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController *  | - Controller for whom this pawn is spawned |  |
| SpawnTransform | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn *  | a pawn of the default pawn class |  |

### InitStartSpot

Called from RestartPlayerAtPlayerStart, can be used to initialize the start spawn actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartSpot | AActor *  |  |  |
| NewPlayer | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnRestartPlayer

Implementable event called at the end of RestartPlayer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | AController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitializeHUDForPlayer

Initialize the AHUD object for a player. Games can override this to do something different

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_OnSwapPlayerControllers

Called when a PlayerController is swapped to a new one during seamless travel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldPC | APlayerController *  |  |  |
| NewPC | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UGameViewportClient

- Symbol Type: class
- Symbol Path: Others / UGameViewportClient
- Source JSON Path: class/detail/Others/UGameViewportClient.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameViewportClient.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

A game viewport (FViewport) is a high-level abstract interface for the
  platform specific rendering, audio, and input subsystems.
  GameViewportClient is the engine's interface to a game viewport.
  Exactly one GameViewportClient is created for each instance of the game.  The
  only case (so far) where you might have a single instance of Engine, but
  multiple instances of the game (and thus multiple GameViewportClients) is when
  you have more than one PIE window running.
 
  Responsibilities:
  propagating input events to the global interactions list
 
  @see UGameViewportClient

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ViewportConsole | UConsole * | The viewport's console.   Might be null on consoles |  |
| DebugProperties | TArray < struct FDebugDisplayProperty > | @todo document |  |
| World | UWorld * | The relative world context for this viewport |  |
| GameInstance | UGameInstance * |  |  |

## Functions

### SSSwapControllers

Rotates controller ids among gameplayers, useful for testing splitscreen with only one controller.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ShowTitleSafeArea

Exec for toggling the display of the title safe area

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetConsoleTarget

Sets the player which console commands will be executed in the context of.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

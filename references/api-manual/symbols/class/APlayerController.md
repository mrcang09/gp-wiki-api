# APlayerController

- Symbol Type: class
- Symbol Path: Others / APlayerController
- Source JSON Path: class/detail/Others/APlayerController.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/APlayerController.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

PlayerControllers are used by human players to control Pawns.
 
  ControlRotation (accessed via GetControlRotation()), determines the aiming
  orientation of the controlled Pawn.
 
  In networked games, PlayerControllers exist on the server for every player-controlled pawn,
  and also on the controlling client's machine. They do NOT exist on a client's
  machine for pawns controlled by remote players elsewhere on the network.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Player | UPlayer * | UPlayer associated with this PlayerController.  Could be a local player or a net connection. |  |
| AcknowledgedPawn | APawn * | Used in net games so client can acknowledge it possessed a specific pawn. |  |
| ControllingDirTrackInst | UInterpTrackInstDirector * | Director track that's currently possessing this player controller, or none if not possessed. |  |
| MyHUD | AHUD * | Heads up display associated with this PlayerController. |  |
| PlayerCameraManager | APlayerCameraManager * | Camera manager associated with this Player Controller. |  |
| PlayerCameraManagerClass | TSubclassOf < APlayerCameraManager > | PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used |  |
| bAutoManageActiveCameraTarget | bool | True to allow this player controller to manage the camera target for you,<br>	  typically by using the possessed pawn as the camera target. Set to false<br>	  if you want to manually control the camera target. |  |
| SmoothTargetViewRotationSpeed | float | Interp speed for blending remote view rotation for smoother client updates |  |
| HiddenActors | TArray < AActor * > | The actors which the camera shouldn't see - e.g. used to hide actors which the camera penetrates |  |
| HiddenPrimitiveComponents | TArray < TWeakObjectPtr < UPrimitiveComponent > > | Explicit components the camera shouldn't see (helpful for external systems to hide a component from a single player) |  |
| LastSpectatorStateSynchTime | float | Used to make sure the client is kept synchronized when in a spectator state |  |
| LastSpectatorSyncLocation | FVector | Last location synced on the server for a spectator. |  |
| LastSpectatorSyncRotation | FRotator | Last rotation synced on the server for a spectator. |  |
| ClientCap | int32 | Cap set by server on bandwidth from client to server in bytessec (only has impact if >=2600) |  |
| CheatManager | UCheatManager * | Object that manages "cheat" commands.  Not instantiated in shipping builds. |  |
| CheatClass | TSoftClassPtr < UCheatManager > | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |  |
| CheatManagerExtras | TArray < UCheatManager * > | Object that manages "cheat" commands.  Not instantiated in shipping builds. |  |
| CheatClassExtras | TArray < TSoftClassPtr < UCheatManager > > | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |  |
| PlayerInput | UPlayerInput * | Object that manages player input. |  |
| ActiveForceFeedbackEffects | TArray < FActiveForceFeedbackEffect > |  |  |
| bPlayerIsWaiting | uint32 | True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state. |  |
| NetPlayerIndex | uint8 | index identifying players using the same base connection (splitscreen clients)<br>	  Used by netcode to match replicated PlayerControllers to the correct splitscreen viewport and child connection<br>	  replicated via special internal code, not through normal variable replication |  |
| PendingSwapConnection | UNetConnection * | this is set on the OLD PlayerController when performing a swap over a network connection<br>	  so we know what connection we're waiting on acknowledgment from to finish destroying this PC<br>	  (or when the connection is closed)<br>	  @see GameModeBase::SwapPlayerControllers() |  |
| NetConnection | UNetConnection * | The net connection this controller is communicating on, NULL for local players on server |  |
| RotationInput | FRotator |  |  |
| InputYawScale | float | Yaw input speed scaling |  |
| InputPitchScale | float | Pitch input speed scaling |  |
| InputRollScale | float | Roll input speed scaling |  |
| bShowMouseCursor | uint32 | Whether the mouse cursor should be displayed. |  |
| bEnableClickEvents | uint32 | Whether actorcomponent click events should be generated. |  |
| bEnableTouchEvents | uint32 | Whether actorcomponent touch events should be generated. |  |
| bEnableMouseOverEvents | uint32 | Whether actorcomponent mouse over events should be generated. |  |
| bEnableTouchOverEvents | uint32 | Whether actorcomponent touch over events should be generated. |  |
| bForceFeedbackEnabled | uint32 |  |  |
| ForceFeedbackScale | float | Scale applied to force feedback values |  |
| ClickEventKeys | TArray < FKey > |  |  |
| DefaultMouseCursor | TEnumAsByte < EMouseCursor :: Type > |  |  |
| CurrentMouseCursor | TEnumAsByte < EMouseCursor :: Type > |  |  |
| DefaultClickTraceChannel | TEnumAsByte < ECollisionChannel > | Default trace channel used for determining what world object was clicked on. |  |
| CurrentClickTraceChannel | TEnumAsByte < ECollisionChannel > | Trace channel currently being used for determining what world object was clicked on. |  |
| HitResultTraceDistance | float |  |  |
| bPauseUpdateStreamingState | uint32 |  |  |
| bActiveReplayViewer | uint8 | true means this controller is active now as a replay viewer |  |
| bEnableReplayRecord | uint8 | true means this controller is enable to record for replay |  |
| IsBlockingInput | bool |  |  |
| InputWhiteListWhenBlocked | TSet < FName > |  |  |
| InputBlackList | TSet < FName > |  |  |
| PriorityActionSet | TSet < FName > |  |  |
| PriorityActionClusters | TArray < FActionCluster > |  |  |
| ActionExecuteState | int32 |  |  |
| InactiveStateInputComponent | UInputComponent * | InputComponent we use when player is in Inactive state. |  |
| bShouldPerformFullTickWhenPaused | uint32 | Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick. |  |
| CurrentTouchInterface | UTouchInterface * | The currently set touch interface |  |
| SpectatorPawn | ASpectatorPawn * | The pawn used when spectating (NULL if not spectating). |  |
| SpawnLocation | FVector | The location used internally when there is no pawn or spectator, to know where to spawn the spectator or focus the camera on death. |  |
| bIsActorChannelOpen | bool |  |  |
| bIsDemoViewController | bool |  |  |
| bIsLocalPlayerController | bool | Set during SpawnActor once and never again to indicate the intent of this controller instance (SERVER ONLY) |  |
| SeamlessTravelCount | uint16 | Counter for this players seamless travels (used along with the below value, to restrict ServerNotifyLoadedWorld) |  |
| LastCompletedSeamlessTravelCount | uint16 | The value of SeamlessTravelCount, upon the last call to GameModeBase::HandleSeamlessTravelPlayer; used to detect seamless travel |  |
| bNeedResetCameraOnPossess | bool | Restart Player by plane do not reset camera!  Engine Modification by czcheng, 2021.6.8 |  |
| bNeedResetControlRotator | bool |  |  |
| LevelVisibilityInfoList | TArray < FLevelVisibilityInfo > |  |  |
| bClientRetryClientRestartFailedProcess | bool |  |  |

## Functions

### ServerSetSpectatorWaiting

Indicate that the Spectator is waiting to joinrespawn.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bWaiting | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetSpectatorWaiting

Indicate that the Spectator is waiting to joinrespawn.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bWaiting | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetActionExecuteState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bSuccess | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActionExecuteState

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### EnableCheats

Enables cheats within the game

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### FOV

Set the field of view to NewFOV

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFOV | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RestartLevel

Restarts the current level

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### LocalTravel

Causes the client to travel to the given URL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientReturnToMainMenu

Return the client to the main menu gracefully

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ReturnReason | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientRepObjRef

Development RPC for testing object reference replication

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Pause

Command to try to pause the game.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetPauseByBlueprint

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bPaused | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetName

Trys to set the player's name to the given name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| S | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SwitchLevel

SwitchLevel to the given MapURL.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetHitResultUnderCursor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TraceChannel | ECollisionChannel  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetHitResultUnderCursorByChannel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TraceChannel | ETraceTypeQuery  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetHitResultUnderCursorForObjects

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetHitResultUnderFinger

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type  |  |  |
| TraceChannel | ECollisionChannel  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetHitResultUnderFingerByChannel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type  |  |  |
| TraceChannel | ETraceTypeQuery  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetHitResultUnderFingerForObjects

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type  |  |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  |  |  |
| bTraceComplex | bool  |  |  |
| HitResult | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### DeprojectMousePositionToWorld

Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector &  |  |  |
| WorldDirection | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### DeprojectScreenPositionToWorld

Convert 2D screen position to World Space 3D position and direction. Returns false if unable to determine value.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ScreenX | float  |  |  |
| ScreenY | float  |  |  |
| WorldLocation | FVector &  |  |  |
| WorldDirection | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ProjectWorldLocationToScreen

Convert a World Space 3D position into a 2D Screen Space position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector  |  |  |
| ScreenLocation | FVector2D &  |  |  |
| bPlayerViewportRelative | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the world coordinate was successfully projected to the screen. |  |

### SetMouseLocation

Positions the mouse cursor in screen space, in pixels.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | int  |  |  |
| Y | int |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StartFire

Fire the player's currently selected weapon with the optional fire mode.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FireModeNum | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientEnableNetworkVoice

Tell the client to enable or disable voice chat (not muting)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool | enable or disable voice chat |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ToggleSpeaking

Toggle voice chat on and off

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInSpeaking | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientVoiceHandshakeComplete

Tells the client that the server has all the information it needs and that it
	  is ok to start sending voice packets. The server will already send voice packets
	  when this function is called, since it is set server side and then forwarded
	 
	  NOTE: This is done as an RPC instead of variable replication because ordering matters

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerMutePlayer

Tell the server to mute a player for this controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerId | FUniqueNetIdRepl | player id to mute |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUnmutePlayer

Tell the server to unmute a player for this controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerId | FUniqueNetIdRepl | player id to unmute |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientMutePlayer

Tell the client to mute a player for this controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerId | FUniqueNetIdRepl | player id to mute |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientUnmutePlayer

Tell the client to unmute a player for this controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerId | FUniqueNetIdRepl | player id to unmute |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ConsoleKey

Console control commands, useful when remote debugging so you can't touch the console the normal way

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SendToConsole

Sends a command to the console to execute if not shipping version

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Command | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientAddTextureStreamingLoc

Adds a location to the texture streaming system for the specified duration.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLoc | FVector  |  |  |
| Duration | float  |  |  |
| bOverrideLocation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientCancelPendingMapChange

Tells client to cancel any pending map change.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientCapBandwidth

Set CurrentNetSpeed to the lower of its current value and Cap.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Cap | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientCommitMapChange

Actually performs the level transition prepared by PrepareMapChange().

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientFlushLevelStreaming

Tells the client to block until all pending level streaming actions are complete
	  happens at the end of the tick
	  primarily used to force update the client ASAP at join time

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientForceGarbageCollection

Forces GC at the end of the tick on the client

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientGameEnded

Replicated function called by GameHasEnded().

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EndGameFocus | AActor *  | - actor to view with camera |  |
| bIsWinner | bool | - true if this controller is on winning team |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientGotoState

Server uses this to force client into NewState .

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewState | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientIgnoreLookInput

calls IgnoreLookInput on client

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIgnore | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientIgnoreMoveInput

calls IgnoreMoveInput on client

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIgnore | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientMessage

Outputs a message to HUD

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| S | FString &  | - message to display |  |
| Type | FName  | - @todo document |  |
| MsgLifeTime | float | - Optional length of time to display 0 = default time |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlayCameraAnim

Play the indicated CameraAnim on this camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimToPlay | UCameraAnim *  | - Camera animation to play |  |
| Scale | float  | - "Intensity" scalar. This is the scale at which the anim was first played. |  |
| Rate | float  | - Multiplier for playback rate. 1.0 = normal. |  |
| BlendInTime | float  | - Time to interpolate in from zero, for smooth starts |  |
| BlendOutTime | float  | - Time to interpolate out to zero, for smooth finishes |  |
| bLoop | bool  | - True if the animation should loop, false otherwise |  |
| bRandomStartTime | bool  | - Whether or not to choose a random time to start playing. Only really makes sense for bLoop = true |  |
| Space | ECameraAnimPlaySpace :: Type  | - Animation play area |  |
| CustomPlaySpace | FRotator | - Matrix used when Space = CAPS_UserDefined |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlayCameraShake

Play Camera Shake

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Shake | TSubclassOf < UCameraShake >  | - Camera shake animation to play |  |
| Scale | float  | - Scalar defining how "intense" to play the anim |  |
| PlaySpace | ECameraAnimPlaySpace :: Type  | - Which coordinate system to play the shake in (used for CameraAnims within the shake). |  |
| UserPlaySpaceRot | FRotator | - Matrix used when PlaySpace = CAPS_UserDefined |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlayCameraShakeWithWorldLocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Shake | TSubclassOf < UCameraShake >  |  |  |
| WorldLocation | FVector  |  |  |
| Scale | float  |  |  |
| PlaySpace | ECameraAnimPlaySpace :: Type  |  |  |
| UserPlaySpaceRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlaySound

Play sound client-side (so only the client will hear it)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sound | USoundBase *  | - Sound to play |  |
| VolumeMultiplier | float  | - Volume multiplier to apply to the sound |  |
| PitchMultiplier | float | - Pitch multiplier to apply to the sound |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlaySoundAtLocation

Play sound client-side at the specified location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sound | USoundBase *  | - Sound to play |  |
| Location | FVector  | - Location to play the sound at |  |
| VolumeMultiplier | float  | - Volume multiplier to apply to the sound |  |
| PitchMultiplier | float | - Pitch multiplier to apply to the sound |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPrepareMapChange

Asynchronously loads the given level in preparation for a streaming map transition.
	  the server sends one function per level name since dynamic arrays can't be replicated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LevelName | FName  |  |  |
| bFirst | bool  | - whether this is the first item in the list (so clear the list first) |  |
| bLast | bool | - whether this is the last item in the list (so start preparing the change after receiving it) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPrestreamTextures

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ForcedActor | AActor *  | - The actor whose textures should be forced into memory. |  |
| ForceDuration | float  | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |  |
| bEnableStreaming | bool  | - Whether to start (true) or stop (false) streaming |  |
| CinematicTextureGroups | int32 | - Bitfield indicating which texture groups that use extra high-resolution mips |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientReset

Tell client to reset the PlayerController

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientRestart

Tell client to restart the level

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetBlockOnAsyncLoading

Tells the client to block until all pending level streaming actions are complete.
	  Happens at the end of the tick primarily used to force update the client ASAP at join time.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientSetCameraFade

Tell client to fade camera

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnableFading | bool  |  |  |
| FadeColor | FColor  |  |  |
| FadeAlpha | FVector2D  |  |  |
| FadeTime | float  |  |  |
| bFadeAudio | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetCameraMode

Replicated function to set camera style on client

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewCamMode | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetCinematicMode

Called by the server to synchronize cinematic transitions with the client

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInCinematicMode | bool  |  |  |
| bAffectsMovement | bool  |  |  |
| bAffectsTurning | bool  |  |  |
| bAffectsHUD | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetForceMipLevelsToBeResident

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface *  | - The material whose textures should be forced into memory. |  |
| ForceDuration | float  | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |  |
| CinematicTextureGroups | int32 | - Bitfield indicating which texture groups that use extra high-resolution mips |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetHUD

Set the client's class of HUD and spawns a new instance of it. If there was already a HUD active, it is destroyed.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewHUDClass | TSubclassOf < AHUD > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetViewportSize

Helper to get the size of the HUD canvas for this player controller.  Returns 0 if there is no HUD

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SizeX | int32 &  |  |  |
| SizeY | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetHUD

Gets the HUD currently being used by this player controller

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AHUD * |  |  |

### SetMouseCursorWidget

Sets the Widget for the Mouse Cursor to display

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Cursor | EMouseCursor :: Type  | - the cursor to set the widget for |  |
| CursorWidget | UUserWidget * | - the widget to set the cursor to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetViewTarget

Set the view target

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | AActor *  | - new actor to set as view target |  |
| TransitionParams | FViewTargetTransitionParams | - parameters to use for controlling the transition |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSpawnCameraLensEffect

Spawn a camera lens effect (e.g. blood).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LensEffectEmitterClass | TSubclassOf < AEmitterCameraLensEffectBase > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientClearCameraLensEffects

Removes all Camera Lens Effects.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientStopCameraAnim

Stop camera animation on client.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimToStop | UCameraAnim * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientStopCameraShake

Stop camera shake on client.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Shake | TSubclassOf < UCameraShake >  |  |  |
| bImmediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientPlayForceFeedback

Play a force feedback pattern on the player's controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ForceFeedbackEffect | UForceFeedbackEffect *  | The force feedback pattern to play |  |
| bLooping | bool  |  Whether the pattern should be played repeatedly or be a single one shot |  |
| bIgnoreTimeDilation | bool  | Whether the pattern should ignore time dilation |  |
| Tag | FName |   A tag that allows stopping of an effect. If another effect with this Tag is playing, it will be stopped and replaced |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientStopForceFeedback

Stops a playing force feedback pattern

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ForceFeedbackEffect | UForceFeedbackEffect *  | If set only patterns from that effect will be stopped |  |
| Tag | FName |   If not none only the pattern with this tag will be stopped |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayDynamicForceFeedback

Latent action that controls the playing of force feedback
	  Begins playing when Start is called.  Calling Update or Stop if the feedback is not active will have no effect.
	  Completed will execute when Stop is called or the duration ends.
	  When Update is called the Intensity, Duration, and affect values will be updated with the current inputs

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Intensity | float  |  How strong the feedback should be. Valid values are between 0.0 and 1.0 |  |
| Duration | float  |  How long the feedback should play for. If the value is negative it will play until stopped |  |
| bAffectsLeftLarge | bool  |  |  |
| bAffectsLeftSmall | bool  |  |  |
| bAffectsRightLarge | bool  |  |  |
| bAffectsRightSmall | bool  |  |  |
| Action | TEnumAsByte < EDynamicForceFeedbackAction :: Type >  |  |  |
| LatentInfo | FLatentActionInfo |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayHapticEffect

Play a haptic feedback curve on the player's controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HapticEffect | UHapticFeedbackEffect_Base *  |  The haptic effect to play |  |
| Hand | EControllerHand  |   Which hand to play the effect on |  |
| Scale | float  |   Scale between 0.0 and 1.0 on the intensity of playback |  |
| bLoop | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopHapticEffect

Stops a playing haptic feedback curve

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hand | EControllerHand |   Which hand to stop the effect for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHapticsByValue

Sets the value of the haptics for the specified hand directly, using frequency and amplitude.  NOTE:  If a curve is already
	 playing for this hand, it will be cancelled in favour of the specified values.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Frequency | float  |  The normalized frequency [0.0, 1.0] to play through the haptics system |  |
| Amplitude | float  |  The normalized amplitude [0.0, 1.0] to set the haptic feedback to |  |
| Hand | EControllerHand |   Which hand to play the effect on |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetControllerLightColor

Sets the light color of the player's controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Color | FColor |   The color for the light to be |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientTravel

Travel to a different map or IP address. Calls the PreClientTravel event before doing anything.
	  NOTE: This is implemented as a locally executed wrapper for ClientTravelInternal, to avoid API compatability breakage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString &  |  A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |  |
| TravelType | ETravelType  |  specifies whether the client should append URL options used in previous travels; if true is specified |  |
| bSeamless | bool  |  Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |  |
| MapPackageGuid | FGuid | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientTravelInternal

Internal clientside implementation of ClientTravel - use ClientTravel to call this

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString &  |  A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |  |
| TravelType | ETravelType  |  specifies whether the client should append URL options used in previous travels; if true is specified |  |
| bSeamless | bool  |  Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |  |
| MapPackageGuid | FGuid | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientUpdateLevelStreamingStatus

Replicated Update streaming status

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName | FName  | - Name of the level package name used for loading. |  |
| bNewShouldBeLoaded | bool  | - Whether the level should be loaded |  |
| bNewShouldBeVisible | bool  | - Whether the level should be visible if it is loaded |  |
| bNewShouldBlockOnLoad | bool  | - Whether we want to force a blocking load |  |
| LODIndex | int32 |  - Current LOD index for a streaming level |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientWasKicked

Notify client they were kicked from the server

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KickReason | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientStartOnlineSession

Notify client that the session is starting

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientEndOnlineSession

Notify client that the session is about to start

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ClientRetryClientRestart

Assign Pawn to player, but avoid calling ClientRestart if we have already accepted this pawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPawn | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientReceiveLocalizedMessage

send client localized message id

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Message | TSubclassOf < ULocalMessage >  |  |  |
| Switch | int32  |  |  |
| RelatedPlayerState_1 | APlayerState *  |  |  |
| RelatedPlayerState_2 | APlayerState *  |  |  |
| OptionalObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerAcknowledgePossession

acknowledge possession of pawn

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| P | APawn * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerCamera

change mode of camera

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMode | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerChangeName

Change name of server

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| S | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerNotifyLoadedWorld

Called to notify the server when the client has loaded a new world via seamless traveling

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldPackageName | FName | the name of the world package that was loaded |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerNotifyStreamLevelDisFactor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFactor | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerPause

Replicate pause request to the server

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerRestartPlayer

Attempts to restart this player, generally called from the client upon respawn request.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerSetSpectatorLocation

When spectating, updates spectator locationrotation and pings the server to make sure spectating should continue.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLoc | FVector  |  |  |
| NewRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerCheckClientPossession

Tells the server to make sure the possessed pawn is in sync with the client.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerCheckClientPossessionReliable

Reliable version of ServerCheckClientPossession to be used when there is no likely danger of spamming the network.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerShortTimeout

Notifies the server that the client has ticked gameplay code, and should no longer get the extended "still loading" timeout grace period

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerUpdateCamera

If PlayerCamera.bUseClientSideCameraUpdates is set, client will replicate camera positions to the server.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CamLoc | FVector_NetQuantize  |  |  |
| CamPitchAndYaw | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUpdateCameraLocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CamLoc | FVector_NetQuantize |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUpdateLevelVisibility

Called when the client addsremoves a streamed level
	  the server will only replicate references to Actors in visible levels so that it's impossible to send references to
	  Actors the client has not initialized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName | FName  | the name of the package for the level whose status changed |  |
| bIsVisible | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUpdateLevelListVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageNames | TArray < FName > &  |  |  |
| bIsVisible | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUpdateLevelListPackageVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageInfo | TArray < FLevelVisibilityInfo > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerUpdateLevelIndexListPackageVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageInfo | TArray < FLevelIndexVisibilityInfo > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerVerifyViewTarget

Used by client to request server to confirm current viewtarget (server will respond with ClientSetViewTarget() ).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerViewNextPlayer

Move camera to next player on round ended or spectating

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerViewPrevPlayer

Move camera to previous player on round ended or spectating

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerViewSelf

Move camera to current user

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TransitionParams | FViewTargetTransitionParams |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientTeamMessage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenderPlayerState | APlayerState *  |  |  |
| S | FString &  |  |  |
| Type | FName  |  |  |
| MsgLifeTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ServerToggleAILogging

Used by UGameplayDebuggingControllerComponent to replicate messages for AI debugging in network games.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddPitchInput

Add Pitch (look up) input. This value is multiplied by InputPitchScale.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Val | float | Amount to add to Pitch. This value is multiplied by InputPitchScale. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddYawInput

Add Yaw (turn) input. This value is multiplied by InputYawScale.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Val | float | Amount to add to Yaw. This value is multiplied by InputYawScale. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddRollInput

Add Roll input. This value is multiplied by InputRollScale.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Val | float | Amount to add to Roll. This value is multiplied by InputRollScale. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsInputKeyDown

Returns true if the given keybutton is pressed on the input of the controller (if present)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### WasInputKeyJustPressed

Returns true if the given keybutton was up last frame and down this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### WasInputKeyJustReleased

Returns true if the given keybutton was down last frame and up this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetInputAnalogKeyState

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInputVectorKeyState

Returns the vector value for the given keybutton.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetInputTouchState

Retrieves the X and Y screen coordinates of the specified touch key. Returns false if the touch index is not down

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | ETouchIndex :: Type  |  |  |
| LocationX | float &  |  |  |
| LocationY | float &  |  |  |
| bIsCurrentlyPressed | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInputMotionState

Retrieves the current motion state of the player's input device

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Tilt | FVector &  |  |  |
| RotationRate | FVector &  |  |  |
| Gravity | FVector &  |  |  |
| Acceleration | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetMousePosition

Retrieves the X and Y screen coordinates of the mouse cursor. Returns false if there is no associated mouse device

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LocationX | float &  |  |  |
| LocationY | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetInputKeyTimeDown

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetInputMouseDelta

Retrieves how far the mouse moved this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaX | float &  |  |  |
| DeltaY | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInputAnalogStickState

Retrieves the X and Y displacement of the given analog stick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WhichStick | EControllerAnalogStick :: Type  |  |  |
| StickX | float &  |  |  |
| StickY | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ActivateTouchInterface

Activates a new touch interface for this player controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTouchInterface | UTouchInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVirtualJoystickVisibility

Set the virtual joystick visibility.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bVisible | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FadeInVirtualJoystick

Fade in the virtual joystick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FadeDuration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FadeOutVirtualJoystick

Fade out the virtual joystick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FadeDuration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitVirtualJoystickBySetting

Set the virtual joystick visibility.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetViewportCacheGeometryScale

获取Viewport的缓存几何缩放

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### Camera

Change Camera mode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMode | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetViewTargetWithBlend

Set the view target blending with variable control

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewViewTarget | AActor *  | - new actor to set as view target |  |
| BlendTime | float  | - time taken to blend |  |
| BlendFunc | EViewTargetBlendFunction  | - Cubic, Linear etc functions for blending |  |
| BlendExp | float  | - Exponent, used by certain blend functions to control the shape of the curve. |  |
| bLockOutgoing | bool | - If true, lock outgoing viewtarget to last frame's camera position for the remainder of the blend. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushPressedKeys

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### FlushPressedKeysImmediate

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### FlushPressedMouseKeys

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetAudioListenerOverride

Used to override the default positioning of the audio listener

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AttachToComponent | USceneComponent *  | Optional component to attach the audio listener to |  |
| Location | FVector  | Depending on whether Component is attached this is either an offset from its location or an absolute position |  |
| Rotation | FRotator | Depending on whether Component is attached this is either an offset from its rotation or an absolute rotation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAudioListenerOverride

Clear any overrides that have been applied to audio listener

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ConsumeResidualNonAxisInput

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetCinematicMode

ServerSP only function for changing whether the player is in cinematic mode.  Updates values of various state variables, then replicates the call to the client
	  to sync the current cinematic mode.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInCinematicMode | bool  | specify true if the player is entering cinematic mode; false if the player is leaving cinematic mode. |  |
| bHidePlayer | bool  |  specify true to hide the player's pawn (only relevant if bInCinematicMode is true) |  |
| bAffectsHUD | bool  |  specify true if we should showhide the HUD to match the value of bCinematicMode |  |
| bAffectsMovement | bool  | specify true to disable movement in cinematic mode, enable it when leaving |  |
| bAffectsTurning | bool | specify true to disable turning in cinematic mode or enable it when leaving |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnServerStartedVisualLogger

Notify from server that Visual Logger is recording, to show that information on client about possible performance issues

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bIsLogging | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSpectatorPawn

Get the Pawn used when spectating. NULL when not spectating.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ASpectatorPawn * |  |  |

### GetFocalLocation

Returns the location the PlayerController is focused on.
	   If there is a possessed Pawn, returns the Pawn's location.
	   If there is a spectator Pawn, returns that Pawn's location.
	   Otherwise, returns the PlayerController's spawn location (usually the last known Pawn location after it has died).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### StartTouchEventRecord

开始记录Touch事件，将信息保存在TouchEventRecordData中，给定一个文件名存盘

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RecordFileName | FString & | 记录保存到的文件名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 是否一切正常 |  |

### StopTouchEventRecord

停止记录Touch事件，将TouchEventRecordData中的数据保存到文件

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 保存是否成功 |  |

### ReplayTouchEventRecord

从文件中加载Touch事件，并进行重放

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RecordFileName | FString & | 记录文件名 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetTouchRecordStartAndEndRotation

获取Touch记录中保存的起始和终止旋转角

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartRotation | FRotator &  | 起始旋转角，引用，在函数内赋值 |  |
| EndRotation | FRotator & | 终止旋转角，引用，在函数内赋值 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

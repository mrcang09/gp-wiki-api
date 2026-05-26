# UCheatManager

- Symbol Type: class
- Symbol Path: Others / UCheatManager
- Source JSON Path: class/detail/Others/UCheatManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCheatManager.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DebugCameraControllerRef | ADebugCameraController * | Debug camera - used to have independent camera without stopping gameplay |  |
| DebugCameraControllerClass | TSubclassOf < ADebugCameraController > | Debug camera - used to have independent camera without stopping gameplay |  |

## Functions

### FreezeFrame

Pause the game for Delay seconds.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delay | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Teleport

Teleport to surface player is looking at.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ChangeSize

Scale the player's size to be F  default size.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| F | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Fly

Pawn can fly.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Walk

Return to walking movement mode from Fly or Ghost cheat.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Ghost

Pawn no longer collides with the world, and can fly

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### God

Invulnerability cheat.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Slomo

Modify time dilation to change apparent speed of passage of time. e.g. "Slomo 0.1" makes everything move very slowly, while "Slomo 10" makes everything move very fast.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTimeDilation | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DamageTarget

Damage the actor you're looking at (sourced from the player).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DamageAmount | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DestroyTarget

Destroy the actor you're looking at.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DestroyAll

Destroy all actors of class aClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| aClass | TSubclassOf < AActor > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DestroyAllPawnsExceptTarget

Destroy all pawns except for the (pawn) target.  If no (pawn) target is found we don't destroy anything.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DestroyPawns

Destroys (by calling destroy directly) all non-player pawns of class aClass in the level

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| aClass | TSubclassOf < APawn > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Summon

Load Classname and spawn an actor of that class

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClassName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayersOnly

Freeze everything in the level except for players.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ViewSelf

Make controlled pawn the viewtarget again.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ViewPlayer

View from the point of view of player with PlayerName S.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| S | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ViewActor

View from the point of view of AActor with Name ActorName.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActorName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ViewClass

View from the point of view of an AActor of class DesiredClass.  Each subsequent ViewClass cycles through the list of actors of that class.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DesiredClass | TSubclassOf < AActor > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StreamLevelIn

Stream in the given level.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnlyLoadLevel

Load the given level.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StreamLevelOut

Stream out the given level.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PackageName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ToggleDebugCamera

Toggle between debug cameraplayer camera without locking gameplay and with locking local player controller input.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ToggleAILogging

toggles AI logging

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ServerToggleAILogging

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DebugCapsuleSweep

Toggle capsule trace debugging. Will trace a capsule from current view point and show where it hits the world

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DebugCapsuleSweepSize

Change Trace capsule size

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HalfHeight | float  |  |  |
| Radius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DebugCapsuleSweepChannel

Change Trace Channel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Channel | ECollisionChannel |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DebugCapsuleSweepComplex

Change Trace Complex setting

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bTraceComplex | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DebugCapsuleSweepCapture

Capture current trace and add to persistent list

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DebugCapsuleSweepPawn

Capture current local PC's pawn's location and add to persistent list

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DebugCapsuleSweepClear

Clear persistent list for trace capture

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### TestCollisionDistance

Test all volumes in the world to the player controller's view location

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RebuildNavigation

Builds the navigation mesh (or rebuilds it).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetNavDrawDistance

Sets navigation drawing distance. Relevant only in non-editor modes.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DrawDistance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DumpOnlineSessionState

Dump online session information

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DumpPartyState

Dump known party information

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DumpChatState

Dump known chat information

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DumpVoiceMutingState

Dump current state of voice chat

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BugItGo

This will move the player and set their rotation to the passed in values.
	  We have this version of the BugIt family as it is easier to type in just raw numbers in the console.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | float  |  |  |
| Y | float  |  |  |
| Z | float  |  |  |
| Pitch | float  |  |  |
| Yaw | float  |  |  |
| Roll | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BugIt

This function is used to print out the BugIt location.  It prints out copy and paste versions for both IMing someone to type in
	 and also a gameinfo ?options version so that you can append it to your launching url and be taken to the correct place.
	 Additionally, it will take a screen shot so reporting bugs is a one command action!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ScreenShotDescription | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BugItStringCreator

This will create a BugItGo string for us.  Nice for calling form c++ where you just want the string and no Screenshots

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ViewLocation | FVector  |  |  |
| ViewRotation | FRotator  |  |  |
| GoString | FString &  |  |  |
| LocString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushLog

This will force a flush of the output log to file

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### LogLoc

Logs the current location in bugit format without taking screenshot and further routing.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetWorldOrigin

Translate world origin to this player position

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMouseSensitivityToDefault

Exec function to return the mouse sensitivity to its default value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### InvertMouse

Backwards compatibility exec function for people used to it instead of using InvertAxisKey

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CheatScript

Executes commands listed in CheatScript.ScriptName ini section of DefaultGame.ini

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ScriptName | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReceiveInitCheatManager

BP implementable event for when CheatManager is created to allow any needed initialization.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveEndPlay

This is the End Play event for the CheatManager

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EnableDebugCamera

Switch controller to debug camera without locking gameplay and with locking local player controller input

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DisableDebugCamera

Switch controller from debug camera back to normal controller

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

# AController

- Symbol Type: class
- Symbol Path: Others / AController
- Source JSON Path: class/detail/Others/AController.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AController.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

Controllers are non-physical actors that can possess a Pawn to control
  its actions.  PlayerControllers are used by human players to control pawns, while
  AIControllers implement the artificial intelligence for the pawns they control.
  Controllers take control of a pawn using their Possess() method, and relinquish
  control of the pawn by calling UnPossess().
 
  Controllers receive notifications for many of the events occurring for the Pawn they
  are controlling.  This gives the controller the opportunity to implement the behavior
  in response to this event, intercepting the event and superseding the Pawn's default
  behavior.
 
  ControlRotation (accessed via GetControlRotation()), determines the viewingaiming
  direction of the controlled Pawn and is affected by input such as from a mouse or gamepad.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pawn | APawn * | Pawn currently being controlled by this controller.  Use Pawn.Possess() to take control of a pawn |  |
| Character | ACharacter * | Character currently being controlled by this controller.  Value is same as Pawn if the controlled pawn is a character, otherwise NULL |  |
| PlayerState | APlayerState * | PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs). |  |
| TransformComponent | USceneComponent * | Component to give controllers a transform and enable attachment if desired. |  |
| ControlRotation | FRotator | The control rotation of the Controller. See GetControlRotation. |  |
| bAttachToPawn | uint32 | If true, the controller location will match the possessed Pawn's location. If false, it will not be updated. Rotation will match ControlRotation in either case.<br>	  Since a Controller's location is normally inaccessible, this is intended mainly for purposes of being able to attach<br>	  an Actor that follows the possessed Pawn location, but that still has the full aim rotation (since a Pawn might<br>	  update only some components of the rotation). |  |
| bIsPlayerController | uint32 | Whether this controller is a PlayerController. |  |
| IgnoreMoveInput | uint8 | Ignores movement input. Stacked state storage, Use accessor function IgnoreMoveInput() |  |
| IgnoreLookInput | uint8 | Ignores look input. Stacked state storage, use accessor function IgnoreLookInput(). |  |
| StateName | FName |  |  |

## Functions

### GetControlRotation

Get the control rotation. This is the full aim rotation, which may be different than a camera orientation (for example in a third person view),
	   and may differ from the rotation of the controlled Pawn (which may choose not to visually pitch or roll, for example).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator |  |  |

### SetControlRotation

Set the control rotation. The RootComponent's rotation will also be updated to match it if RootComponent->bAbsoluteRotation is true.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRotation | FRotator & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInitialLocationAndRotation

Set the initial location and rotation of the controller, as well as the control rotation. Typically used when the controller is first created.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector &  |  |  |
| NewRotation | FRotator & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStartSpot

Set the StartSpot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearStartSpot

Clear the StartSpot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetStartSpot

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### LineOfSightTo

Checks line to center and top of other actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Other | AActor *  | is the actor whose visibility is being checked. |  |
| ViewPoint | FVector  | is eye position visibility is being checked from. If vect(0,0,0) passed in, uses current viewtarget's eye position. |  |
| bAlternateChecks | bool | used only in AIController implementation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if controller's pawn can see Other actor. |  |

### OnRep_Pawn

Replication Notification Callbacks

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnRep_PlayerState

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CastToPlayerController

DEPRECATED! Use the standard "Cast To" node instead. Casts this Controller to a Player Controller, if possible.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController * |  |  |

### ClientSetLocation

Replicated function to set the pawn location and rotation, allowing server to force (ex. teleports).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector  |  |  |
| NewRotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClientSetRotation

Replicated function to set the pawn rotation, allowing the server to force.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewRotation | FRotator  |  |  |
| bResetCamera | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_GetPawn

Return the Pawn that is currently 'controlled' by this PlayerController

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn * |  |  |

### GetViewTarget

Get the actor the controller is looking at

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * |  |  |

### GetDesiredRotation

Get the desired pawn target rotation

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator |  |  |

### IsPlayerController

Returns whether this Controller is a PlayerController.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsLocalPlayerController

Returns whether this Controller is a locally controlled PlayerController.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsLocalController

Returns whether this Controller is a local controller.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### Possess

Handles attaching this controller to the specified pawn.
	  Only runs on the network authority (where HasAuthority() returns true).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPawn | APawn * | The Pawn to be possessed. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnPossess

Called to unpossess our pawn for any reason that is not the pawn being destroyed (destruction handled by PawnDestroyed()).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### StopMovement

Aborts the move the controller is currently performing

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetIgnoreMoveInput

Locks or unlocks movement input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreMoveInput.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewMoveInput | bool | If true, move input is ignored. If false, input is not ignored. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetIgnoreMoveInput

Stops ignoring move input by resetting the ignore move input state.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsMoveInputIgnored

Returns true if movement input is ignored.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetIgnoreLookInput

Locks or unlocks look input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreLookInput.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewLookInput | bool | If true, look input is ignored. If false, input is not ignored. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetIgnoreLookInput

Stops ignoring look input by resetting the ignore look input state.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsLookInputIgnored

Returns true if look input is ignored.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ResetIgnoreInputFlags

Reset move and look input ignore flags.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ReceiveInstigatedAnyDamage

Event when this controller instigates ANY damage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Damage | float  |  |  |
| DamageType | UDamageType *  |  |  |
| DamagedActor | AActor *  |  |  |
| DamageCauser | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

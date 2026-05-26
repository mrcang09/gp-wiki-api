# UInputComponent

- Symbol Type: class
- Symbol Path: Others / UInputComponent
- Source JSON Path: class/detail/Others/UInputComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInputComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

Implement an Actor component for input bindings.
 
  An Input Component is a transient component that enables an Actor to bind various forms of input events to delegate functions.  
  Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
  Each binding can consume the input event preventing other components on the input stack from processing the input.

## Functions

### IsControllerKeyDown

Returns true if the given keybutton is pressed on the input of the controller (if present)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### WasControllerKeyJustPressed

Returns true if the given keybutton was up last frame and down this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### WasControllerKeyJustReleased

Returns true if the given keybutton was down last frame and up this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetControllerAnalogKeyState

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetControllerVectorKeyState

Returns the vector value for the given keybutton.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetTouchState

Returns the location of a touch, and if it's held down

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FingerIndex | int32  |  |  |
| LocationX | float &  |  |  |
| LocationY | float &  |  |  |
| bIsCurrentlyPressed | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetControllerKeyTimeDown

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | FKey |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetControllerMouseDelta

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

### GetControllerAnalogStickState

Retrieves the X and Y displacement of the given analog stick.  For WhickStick, 0 = left, 1 = right.

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

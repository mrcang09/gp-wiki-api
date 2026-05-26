# UInputSettings

- Symbol Type: class
- Symbol Path: Others / UInputSettings
- Source JSON Path: class/detail/Others/UInputSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInputSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

Project wide settings for input handling

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisConfig | TArray < struct FInputAxisConfigEntry > | Properties of Axis controls |  |
| bAltEnterTogglesFullscreen | uint32 |  |  |
| bF11TogglesFullscreen | uint32 |  |  |
| bUseMouseForTouch | uint32 |  |  |
| bEnableMouseSmoothing | uint32 |  |  |
| bEnableFOVScaling | uint32 |  |  |
| FOVScale | float |  |  |
| DoubleClickTime | float | If a key is pressed twice in this amount of time it is considered a "double click" |  |
| bCaptureMouseOnLaunch | bool | Controls if the viewport will capture the mouse on Launch of the application |  |
| DefaultViewportMouseCaptureMode | EMouseCaptureMode | The default mouse capture mode for the game viewport |  |
| bDefaultViewportMouseLock_DEPRECATED | bool | The default mouse lock state when the viewport acquires capture |  |
| DefaultViewportMouseLockMode | EMouseLockMode | The default mouse lock state behavior when the viewport acquires capture |  |
| ActionMappings | TArray < struct FInputActionKeyMapping > | List of Action Mappings |  |
| AxisMappings | TArray < struct FInputAxisKeyMapping > | List of Axis Mappings |  |
| bAlwaysShowTouchInterface | bool | Should the touch input interface be shown always, or only when the platform has a touch screen? |  |
| bShowConsoleOnFourFingerTap | bool | Whether or not to show the console on 4 finger tap, on mobile platforms |  |
| DefaultTouchInterface | FSoftObjectPath | The default on-screen touch input interface for the game (can be null to disable the onscreen interface) |  |
| ConsoleKey_DEPRECATED | FKey | The key which opens the console. |  |
| ConsoleKeys | TArray < FKey > | The keys which open the console. |  |

## Functions

### GetInputSettings

Returns the game local input settings (action mappings, axis mappings, etc...)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UInputSettings * |  |  |

### AddActionMapping

Programmatically add an action mapping to the project defaults

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyMapping | FInputActionKeyMapping &  |  |  |
| bForceRebuildKeymaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActionMappingByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActionName | FName  |  |  |
| OutMappings | TArray < FInputActionKeyMapping > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveActionMapping

Programmatically remove an action mapping to the project defaults

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyMapping | FInputActionKeyMapping &  |  |  |
| bForceRebuildKeymaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddAxisMapping

Programmatically add an axis mapping to the project defaults

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyMapping | FInputAxisKeyMapping &  |  |  |
| bForceRebuildKeymaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAxisMappingByName

Retrieve all axis mappings by a certain name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAxisName | FName  |  |  |
| OutMappings | TArray < FInputAxisKeyMapping > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveAxisMapping

Programmatically remove an axis mapping to the project defaults

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| KeyMapping | FInputAxisKeyMapping &  |  |  |
| bForceRebuildKeymaps | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SaveKeyMappings

Flush the current mapping values to the config file

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetActionNames

Populate a list of all defined action names

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionNames | TArray < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAxisNames

Populate a list of all defined axis names

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AxisNames | TArray < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ForceRebuildKeymaps

When changes are made to the default mappings, push those changes out to PlayerInput key maps

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ApplySettings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetToDefaultEditorSettings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SaveToConfig

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetActionMappings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < struct FInputActionKeyMapping > |  |  |

### GetAxisMappings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < struct FInputAxisKeyMapping > |  |  |

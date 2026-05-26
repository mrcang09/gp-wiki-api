# UKismetSystemLibrary

- Symbol Type: class
- Symbol Path: 引擎 / 常用全局类 / UKismetSystemLibrary
- Source JSON Path: class/detail/引擎/常用全局类/UKismetSystemLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UKismetSystemLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Functions

### StackTrace

Prints a stack trace to the log, so you can see how a blueprint got to this node

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsValid

对象是否可用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true可用，false不可用 |  |

### IsRecycled

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValidClass

类型是否可用

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Class | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true可用，false不可用 |  |

### GetObjectName

获取对象名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 对象实际名称 |  |

### GetPathName

获取对象路径

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 对象完整路径 |  |

### GetDisplayName

获取对象展示名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 对象展示名称 |  |

### GetClassDisplayName

获取类展示名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Class | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | 类展示名称 |  |

### StripObjectClass

If there is an object class, strips it off.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PathName | FString &  |  |  |
| bAssertOnBadPath | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetEngineVersion

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetGameName

Get the name of the current game

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetGameBundleId

Retrieves the game's platform-specific bundle identifier or package name of the game

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The game's bundle identifier or package name. |  |

### GetPlatformUserName

Get the current user name from the OS

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### DoesImplementInterface

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TestObject | UObject *  |  |  |
| Interface | TSubclassOf < UInterface > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetGameTimeInSeconds

Get the current game time, in seconds. This stops when the game is paused and is affected by slomo.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * | World context |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### IsServer

Returns whether the world this object is in is the host or not

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsDedicatedServer

Returns whether this is running on a dedicated server

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsStandalone

Returns whether this game instance is stand alone (no networking).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsPackagedForDistribution

Returns whether this is a build that is packaged for distribution

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetUniqueDeviceId

Returns the platform specific unique device id

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetDeviceId

Returns the platform specific unique device id

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### Conv_InterfaceToObject

Converts an interfance into an object

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Interface | FScriptInterface & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### MakeSoftObjectPath

将路径字符串转换为SoftObjectPath

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PathString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath  | SoftObjectPath | cppstruct/detail/FSoftObjectPath.json |

### BreakSoftObjectPath

将SoftObjectPath转换为路径字符串

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSoftObjectPath | FSoftObjectPath  |  | cppstruct/detail/FSoftObjectPath.json |
| PathString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | PathString |  |

### BreakSoftClassPath

将SoftClassPath转换为路径字符串

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSoftClassPath | FSoftClassPath  |  |  |
| PathString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | PathString |  |

### IsValidSoftObjectReference

SoftObjectPath是否有效

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftObjectReference | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true为有效 |  |

### Conv_SoftObjectReferenceToString

Converts a Soft Object Reference to a string. The other direction is not provided because it cannot be validated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftObjectReference | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### EqualEqual_SoftObjectReference

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | TSoftObjectPtr < UObject > &  |  |  |
| B | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_SoftObjectReference

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | TSoftObjectPtr < UObject > &  |  |  |
| B | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValidSoftClassReference

Returns true if the Soft Class Reference is not null

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftClassReference | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_SoftClassReferenceToString

Converts a Soft Class Reference to a string. The other direction is not provided because it cannot be validated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftClassReference | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### EqualEqual_SoftClassReference

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | TSoftClassPtr < UObject > &  |  |  |
| B | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_SoftClassReference

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | TSoftClassPtr < UObject > &  |  |  |
| B | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_SoftObjectReferenceToObject

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftObject | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### Conv_SoftClassReferenceToClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftClass | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSubclassOf < UObject >  |  |  |

### Conv_ObjectToSoftObjectReference

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSoftObjectPtr < UObject >  |  |  |

### Conv_ClassToSoftClassReference

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Class | TSubclassOf < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSoftClassPtr < UObject >  |  |  |

### LoadAsset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Asset | TSoftObjectPtr < UObject >  |  |  |
| OnLoaded | FOnAssetLoaded  |  |  |
| LatentInfo | FLatentActionInfo |  | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### LoadAssetClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| AssetClass | TSoftClassPtr < UObject >  |  |  |
| OnLoaded | FOnAssetClassLoaded  |  |  |
| LatentInfo | FLatentActionInfo |  | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeLiteralInt

Creates a literal integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 | value to set the integer to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The literal integer |  |

### MakeLiteralInt64

Creates a literal integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int64 | value to set the integer to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  | The literal integer |  |

### MakeLiteralFloat

Creates a literal float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float | value to set the float to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The literal float |  |

### MakeLiteralBool

Creates a literal bool

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | bool | value to set the bool to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | The literal bool |  |

### MakeLiteralName

Creates a literal name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FName | value to set the name to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | The literal name |  |

### MakeLiteralByte

Creates a literal byte

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | uint8 | value to set the byte to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  | The literal byte |  |

### MakeLiteralString

Creates a literal string

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FString & | value to set the string to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | The literal string |  |

### MakeLiteralText

Creates a literal FText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FText | value to set the FText to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  | The literal FText |  |

### PrintString

Prints a string to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InString | FString &  | The string to log out |  |
| bPrintToScreen | bool  | Whether or not to print the output to the screen |  |
| bPrintToLog | bool  | Whether or not to print the output to the log |  |
| TextColor | FLinearColor  | Whether or not to print the output to the console | cppstruct/detail/FLinearColor.json |
| Duration | float | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PrintText

Prints text to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InText | FText  |  The text to log out |  |
| bPrintToScreen | bool  | Whether or not to print the output to the screen |  |
| bPrintToLog | bool  | Whether or not to print the output to the log |  |
| TextColor | FLinearColor  | Whether or not to print the output to the console | cppstruct/detail/FLinearColor.json |
| Duration | float | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PrintWarning

Prints a warning string to the log and the screen. Meant to be used as a way to inform the user that they misused the node.
	 
	  WARNING!! Don't change the signature of this function without fixing up all nodes using it in the compiler

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InString | FString & | The string to log out |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetWindowTitle

Sets the game window title

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Title | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ExecuteConsoleCommand

Executes a console command, optionally on a specific controller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Command | FString &  |  Command to send to the console |  |
| SpecificPlayer | APlayerController *  | If specified, the console command will be routed through the specified player |  |
| bDisableCheck | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ExecuteConsoleCommandDisableCheck

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Command | FString &  |  |  |
| SpecificPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetConsoleVariableFloatValue

Attempts to retrieve the value of the specified float console variable, if it exists.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VariableName | FString & | Name of the console variable to find. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The value if found, 0 otherwise. |  |

### GetConsoleVariableIntValue

Attempts to retrieve the value of the specified integer console variable, if it exists.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VariableName | FString & | Name of the console variable to find. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The value if found, 0 otherwise. |  |

### GetConsoleVariableBoolValue

Evaluates, if it exists, whether the specified integer console variable has a non-zero value (true) or not (false).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VariableName | FString & | Name of the console variable to find. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if found and has a non-zero value, false otherwise. |  |

### QuitGame

Exit the current game

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SpecificPlayer | APlayerController *  | The specific player to quit the game. If not specified, player 0 will quit. |  |
| QuitPreference | TEnumAsByte < EQuitPreference :: Type > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Delay

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Duration | float  |  length of delay (in seconds). |  |
| LatentInfo | FLatentActionInfo | The latent action. | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DelayUntilNextTick

Perform a latent action with a delay of one tick.  Calling again while it is counting down will be ignored.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LatentInfo | FLatentActionInfo | The latent action. | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DelayReplacePreDuration

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Duration | float  |  length of delay (in seconds). |  |
| IsReplacePreDuration | bool  | replace previous action Duration |  |
| LatentInfo | FLatentActionInfo | The latent action. | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RetriggerableDelay

Perform a latent action with a retriggerable delay (specified in seconds).  Calling again while it is counting down will reset the countdown to Duration.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Duration | float  |  length of delay (in seconds). |  |
| LatentInfo | FLatentActionInfo | The latent action. | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MoveComponentTo

Interpolate a component to the specified relative location and rotation over the course of OverTime seconds.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | USceneComponent *  |   Component to interpolate |  |
| TargetRelativeLocation | FVector  | Relative target location | cppstruct/detail/FVector.json |
| TargetRelativeRotation | FRotator  | Relative target rotation | cppstruct/detail/FRotator.json |
| bEaseOut | bool  |   if true we will ease out (ie end slowly) during interpolation |  |
| bEaseIn | bool  |   if true we will ease in (ie start slowly) during interpolation |  |
| OverTime | float  |   duration of interpolation |  |
| bForceShortestRotationPath | bool  | if true we will always use the shortest path for rotation |  |
| MoveAction | TEnumAsByte < EMoveComponentAction :: Type >  |   required movement behavior @see EMoveComponentAction |  |
| LatentInfo | FLatentActionInfo |   The latent action | cppstruct/detail/FLatentActionInfo.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_SetTimerDelegate

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate  |  |  |
| Time | float  |  How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |  |
| bLooping | bool | True to keep executing the delegate every Time seconds, false to execute delegate only once. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimerHandle  | 			The timer handle to pass to other timer functions to manipulate this timer. | cppstruct/detail/FTimerHandle.json |

### K2_SetTimerForNextTickDelegate

Set a timer to execute a delegate next tick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | 						The timer handle to pass to other timer functions to manipulate this timer. |  |

### K2_SetTimerTickDelegate

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicParamDelegate  |  |  |
| Time | float  |  How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |  |
| InExeFirst | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimerHandle  | 			The timer handle to pass to other timer functions to manipulate this timer. | cppstruct/detail/FTimerHandle.json |

### K2_SetTimerDelegateForLua

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate  |  |  |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| Time | float  |  How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |  |
| bLooping | bool | True to keep executing the delegate every Time seconds, false to execute delegate only once. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimerHandle  | 			The timer handle to pass to other timer functions to manipulate this timer. | cppstruct/detail/FTimerHandle.json |

### K2_ClearTimerDelegate

Clears a set timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_PauseTimerDelegate

Pauses a set timer at its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_UnPauseTimerDelegate

Resumes a paused timer from its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_IsTimerActiveDelegate

Returns true if a timer exists and is active for the given delegate, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is active. |  |

### K2_IsTimerPausedDelegate

Returns true if a timer exists and is paused for the given delegate, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is paused. |  |

### K2_TimerExistsDelegate

Returns true is a timer for the given delegate exists, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists. |  |

### K2_GetTimerElapsedTimeDelegate

Returns elapsed time for the given delegate (time since current countdown iteration began).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long has elapsed since the current iteration of the timer began. |  |

### K2_GetTimerRemainingTimeDelegate

Returns time until the timer will next execute its delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Delegate | FTimerDynamicDelegate |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long is remaining in the current iteration of the timer. |  |

### K2_IsValidTimerHandle

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Handle | FTimerHandle | The handle of the timer to check validity of. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			Whether the timer handle is valid. |  |

### K2_InvalidateTimerHandle

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Handle | FTimerHandle & | The handle of the timer to check validity of. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimerHandle  | 			Return the invalidated timer handle for convenience. | cppstruct/detail/FTimerHandle.json |

### K2_ClearTimerHandle

Clears a set timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to clear. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_ClearAndInvalidateTimerHandle

Clears a set timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle & | The handle of the timer to clear. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_PauseTimerHandle

Pauses a set timer at its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to pause. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_UnPauseTimerHandle

Resumes a paused timer from its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to unpause. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_IsTimerActiveHandle

Returns true if a timer exists and is active for the given handle, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to check whether it is active. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is active. |  |

### K2_IsTimerPausedHandle

Returns true if a timer exists and is paused for the given handle, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to check whether it is paused. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is paused. |  |

### K2_TimerExistsHandle

Returns true is a timer for the given handle exists, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle to check whether it exists. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists. |  |

### K2_GetTimerElapsedTimeHandle

Returns elapsed time for the given handle (time since current countdown iteration began).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to get the elapsed time of. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long has elapsed since the current iteration of the timer began. |  |

### K2_GetTimerRemainingTimeHandle

Returns time until the timer will next execute its handle.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Handle | FTimerHandle | The handle of the timer to time remaining of. | cppstruct/detail/FTimerHandle.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long is remaining in the current iteration of the timer. |  |

### K2_SetTimer

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString  | Delegate function name. Can be a K2 function or a Custom Event. |  |
| Time | float  |  How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |  |
| bLooping | bool | true to keep executing the delegate every Time seconds, false to execute delegate only once. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimerHandle  | 			The timer handle to pass to other timer functions to manipulate this timer. | cppstruct/detail/FTimerHandle.json |

### K2_SetTimerForNextTick

Set a timer to execute a delegate on the next tick.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |   Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString |  Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | 						The timer handle to pass to other timer functions to manipulate this timer. |  |

### K2_ClearTimer

Clears a set timer.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_PauseTimer

Pauses a set timer at its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_UnPauseTimer

Resumes a paused timer from its current elapsed time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_IsTimerActive

Returns true if a timer exists and is active for the given delegate, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is active. |  |

### K2_IsTimerPaused

Returns true if a timer exists and is paused for the given delegate, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists and is paused. |  |

### K2_TimerExists

Returns true is a timer for the given delegate exists, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if the timer exists. |  |

### K2_GetTimerElapsedTime

Returns elapsed time for the given delegate (time since current countdown iteration began).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long has elapsed since the current iteration of the timer began. |  |

### K2_GetTimerRemainingTime

Returns time until the timer will next execute its delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  | Object that implements the delegate function. Defaults to self (this blueprint) |  |
| FunctionName | FString | Delegate function name. Can be a K2 function or a Custom Event. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 			How long is remaining in the current iteration of the timer. |  |

### SetIntPropertyByName

Set an int32 property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInt64PropertyByName

Set an int64 property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUInt64PropertyByName

Set an uint64 property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBytePropertyByName

Set an uint8 or enum property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetObjectPropertyByName

Set an OBJECT property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFloatPropertyByName

Set a float property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBoolPropertyByName

Set a bool property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetClassPropertyByName

Set a CLASS property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | TSubclassOf < UObject > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInterfacePropertyByName

Set an INTERFACE property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FScriptInterface & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNamePropertyByName

Set a NAME property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSoftObjectPropertyByName

Set a SOFTOBJECT property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | TSoftObjectPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSoftClassPropertyByName

Set a SOFTCLASS property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | TSoftClassPtr < UObject > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStringPropertyByName

Set a STRING property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTextPropertyByName

Set a TEXT property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVectorPropertyByName

Set a VECTOR property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FVector & |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRotatorPropertyByName

Set a ROTATOR property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FRotator & |  | cppstruct/detail/FRotator.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLinearColorPropertyByName

Set a LINEAR COLOR property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FLinearColor & |  | cppstruct/detail/FLinearColor.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTransformPropertyByName

Set a TRANSFORM property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FTransform & |  | cppstruct/detail/FTransform.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCollisionProfileNameProperty

Set a CollisionProfileName property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FCollisionProfileName & |  | cppstruct/detail/FCollisionProfileName.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStructurePropertyByName

Set a custom structure property by name

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | FGenericStruct & |  | cppstruct/detail/FGenericStruct.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SphereOverlapActors

返回一组跟指定球体范围发生重叠的Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| SpherePos | FVector  | 球心位置 | cppstruct/detail/FVector.json |
| SphereRadius | float  | 球体半径 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ActorClassFilter | UClass *  | 对象类型过滤，只检测指定类型的Actor |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutActors | TArray < AActor * > & | 输出的产生碰撞的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### SphereOverlapComponents

返回一组跟指定球体范围发生重叠的Component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| SpherePos | FVector  | 球心位置 | cppstruct/detail/FVector.json |
| SphereRadius | float  | 球体半径 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ComponentClassFilter | UClass *  | 组件类型过滤，只检测指定类型的组件 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutComponents | TArray < UPrimitiveComponent * > & | 输出的产生碰撞的组件列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### BoxOverlapAnyTest

检测指定Box范围是否发生重叠

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| BoxPos | FVector  | Box中心位置 | cppstruct/detail/FVector.json |
| Rotator | FRotator  | Box旋转量 | cppstruct/detail/FRotator.json |
| BoxExtent | FVector  | Box范围 | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ActorClassFilter | UClass *  | 对象类型过滤，只检测指定类型的Actor |  |
| ActorsToIgnore | TArray < AActor * > & | 需要忽略的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### BoxOverlapActors

返回一组跟指定Box范围发生重叠的Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| BoxPos | FVector  | Box中心位置 | cppstruct/detail/FVector.json |
| BoxRotation | FRotator  |  | cppstruct/detail/FRotator.json |
| BoxExtent | FVector  | Box范围 | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ActorClassFilter | UClass *  | 对象类型过滤，只检测指定类型的Actor |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutActors | TArray < AActor * > & | 输出的产生碰撞的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### BoxOverlapOBBActors

Returns an array of actors that overlap the given axis-aligned box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| BoxPos | FVector &  | Center of box. | cppstruct/detail/FVector.json |
| BoxRot | FRotator &  | Rotator of box. | cppstruct/detail/FRotator.json |
| BoxExtent | FVector &  | Extents of box. | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  |  |  |
| ActorClassFilter | UClass *  |  |  |
| ActorsToIgnore | TArray < AActor * > &  | Ignore these actors in the list |  |
| OutActors | TArray < AActor * > & | Returned array of actors. Unsorted. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### BoxOverlapComponents

返回一组跟指定Box范围发生重叠的Component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| BoxPos | FVector  | Box中心位置 | cppstruct/detail/FVector.json |
| BoxRotation | FRotator  |  | cppstruct/detail/FRotator.json |
| Extent | FVector  |  | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ComponentClassFilter | UClass *  |  |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutComponents | TArray < UPrimitiveComponent * > & | 输出的产生碰撞的组件列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### BoxOverlapOBBComponents

Returns an array of components that overlap the given axis-aligned box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| BoxPos | FVector &  | Center of box. | cppstruct/detail/FVector.json |
| BoxRot | FRotator &  | Rotator of box. | cppstruct/detail/FRotator.json |
| Extent | FVector &  |  | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  |  |  |
| ComponentClassFilter | UClass *  |  |  |
| ActorsToIgnore | TArray < AActor * > &  | Ignore these actors in the list |  |
| OutComponents | TArray < UPrimitiveComponent * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### CapsuleOverlapActors

返回一组跟指定胶囊体范围发生重叠的Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| CapsulePos | FVector  | 胶囊体中心位置 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半高 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ActorClassFilter | UClass *  | 对象类型过滤，只检测指定类型的Actor |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutActors | TArray < AActor * > & | Returned array of actors. Unsorted. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### CapsuleOverlapComponents

返回一组跟指定胶囊体范围发生重叠的Component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | world上下文对象 |  |
| CapsulePos | FVector  | 胶囊体中心位置 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半高 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ComponentClassFilter | UClass *  |  |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutComponents | TArray < UPrimitiveComponent * > & | 输出的产生碰撞的组件列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			true if there was an overlap that passed the filters, false otherwise. |  |

### ComponentOverlapActors

返回一组跟指定Component发生重叠的Actor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  | Component对象 |  |
| ComponentTransform | FTransform &  | Component的Transform | cppstruct/detail/FTransform.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ActorClassFilter | UClass *  | 对象类型过滤，只检测指定类型的Actor |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutActors | TArray < AActor * > & | 输出的产生碰撞的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 					true if there was an overlap that passed the filters, false otherwise. |  |

### ComponentOverlapComponents

返回一组跟指定Component发生重叠的Component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  | Component对象 |  |
| ComponentTransform | FTransform &  | Component的Transform | cppstruct/detail/FTransform.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 将结果限制为仅静态或仅动态的选项 |  |
| ComponentClassFilter | UClass *  |  |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| OutComponents | TArray < UPrimitiveComponent * > & | 输出的产生碰撞的组件列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 					true if there was an overlap that passed the filters, false otherwise. |  |

### LineTraceSingle

返回第一个跟射线碰撞的物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### LineTraceMulti

返回所有跟射线碰撞的物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### SphereTraceSingle

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### SphereTraceMulti

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### BoxTraceSingle

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### BoxTraceMulti

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### CapsuleTraceSingle

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### CapsuleTraceMulti

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| TraceChannel | ETraceTypeQuery  | 轨迹检测通道 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### LineTraceSingleForObjects

返回第一个跟射线碰撞的物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### LineTraceSingleByObjectType

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  |  | cppstruct/detail/FVector.json |
| End | FVector  |  | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < ECollisionChannel > > &  |  |  |
| bTraceComplex | bool  |  |  |
| ActorsToIgnore | TArray < AActor * > &  |  |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  |  | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LineTraceMultiForObjects

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### SphereTraceSingleForObjects

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### SphereTraceMultiForObjects

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### BoxTraceSingleForObjects

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### BoxTraceMultiForObjects

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### CapsuleTraceSingleForObjects

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### CapsuleTraceMultiForObjects

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| ObjectTypes | TArray < TEnumAsByte < EObjectTypeQuery > > &  | 对象类型列表 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### LineTraceSingleByProfile

返回第一个跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### LineTraceMultiByProfile

返回所有跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### SphereTraceSingleByProfile

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### SphereTraceMultiByProfile

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 球体半径 |  |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### BoxTraceSingleByProfile

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### BoxTraceMultiByProfile

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| HalfSize | FVector  | Box边的半长尺寸 | cppstruct/detail/FVector.json |
| Orientation | FRotator  | Box的朝向 | cppstruct/detail/FRotator.json |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### CapsuleTraceSingleByProfile

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHit | FHitResult &  | 输出的HitResult | cppstruct/detail/FHitResult.json |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a hit, false otherwise. |  |

### CapsuleTraceMultiByProfile

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  | 射线检测起点 | cppstruct/detail/FVector.json |
| End | FVector  | 射线检测终点 | cppstruct/detail/FVector.json |
| Radius | float  | 胶囊体半径 |  |
| HalfHeight | float  | 胶囊体半长高度 |  |
| ProfileName | FName  | 预设名称 |  |
| bTraceComplex | bool  | true为复杂碰撞检测，false为简单碰撞检测 |  |
| ActorsToIgnore | TArray < AActor * > &  | 需要忽略的Actor列表 |  |
| DrawDebugType | EDrawDebugTrace :: Type  |  |  |
| OutHits | TArray < FHitResult > &  | 输出的HitResult列表 |  |
| bIgnoreSelf | bool  |  |  |
| TraceColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TraceHitColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 			True if there was a blocking hit, false otherwise. |  |

### GetActorListFromComponentList

Returns an array of unique actors represented by the given list of components.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ComponentList | TArray < UPrimitiveComponent * > &  | List of components. |  |
| ActorClassFilter | UClass *  |  |  |
| OutActorList | TArray < AActor * > & | Start of line segment. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PrintToScreen

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InString | FString &  |  |  |
| TextColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| TextScale | FVector2D  |  | cppstruct/detail/FVector2D.json |
| Duration | float  |  |  |
| bIsUGC | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushOnScreenDebugMessages

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DrawDebugLine

Draw a debug line

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LineStart | FVector  |  | cppstruct/detail/FVector.json |
| LineEnd | FVector  |  | cppstruct/detail/FVector.json |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCircle

Draw a debug circle!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Center | FVector  |  | cppstruct/detail/FVector.json |
| Radius | float  |  |  |
| NumSegments | int32  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float  |  |  |
| YAxis | FVector  |  | cppstruct/detail/FVector.json |
| ZAxis | FVector  |  | cppstruct/detail/FVector.json |
| bDrawAxis | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugPoint

Draw a debug point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Position | FVector  |  | cppstruct/detail/FVector.json |
| Size | float  |  |  |
| PointColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugArrow

Draw directional arrow, pointing from LineStart to LineEnd.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| LineStart | FVector  |  | cppstruct/detail/FVector.json |
| LineEnd | FVector  |  | cppstruct/detail/FVector.json |
| ArrowSize | float  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugBox

Draw a debug box

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Center | FVector  |  | cppstruct/detail/FVector.json |
| Extent | FVector  |  | cppstruct/detail/FVector.json |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Rotation | FRotator  |  | cppstruct/detail/FRotator.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCoordinateSystem

Draw a debug coordinate system.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| AxisLoc | FVector  |  | cppstruct/detail/FVector.json |
| AxisRot | FRotator  |  | cppstruct/detail/FRotator.json |
| Scale | float  |  |  |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugSphere

Draw a debug sphere

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Center | FVector  |  | cppstruct/detail/FVector.json |
| Radius | float  |  |  |
| Segments | int32  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCylinder

Draw a debug cylinder

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Start | FVector  |  | cppstruct/detail/FVector.json |
| End | FVector  |  | cppstruct/detail/FVector.json |
| Radius | float  |  |  |
| Segments | int32  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCone

Draw a debug cone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector  |  | cppstruct/detail/FVector.json |
| Direction | FVector  |  | cppstruct/detail/FVector.json |
| Length | float  |  |  |
| AngleWidth | float  |  |  |
| AngleHeight | float  |  |  |
| NumSides | int32  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugConeInDegrees

Draw a debug cone
	  Angles are specified in degrees

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Origin | FVector  |  | cppstruct/detail/FVector.json |
| Direction | FVector  |  | cppstruct/detail/FVector.json |
| Length | float  |  |  |
| AngleWidth | float  |  |  |
| AngleHeight | float  |  |  |
| NumSides | int32  |  |  |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCapsule

Draw a debug capsule

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Center | FVector  |  | cppstruct/detail/FVector.json |
| HalfHeight | float  |  |  |
| Radius | float  |  |  |
| Rotation | FRotator  |  | cppstruct/detail/FRotator.json |
| LineColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugString

Draw a debug string at a 3d world location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| TextLocation | FVector  |  | cppstruct/detail/FVector.json |
| Text | FString &  |  |  |
| TestBaseActor | AActor *  |  |  |
| TextColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushDebugStrings

Removes all debug strings.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugPlane

Draws a debug plane.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PlaneCoordinates | FPlane &  |  | cppstruct/detail/FPlane.json |
| Location | FVector  |  | cppstruct/detail/FVector.json |
| Size | float  |  |  |
| PlaneColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FlushPersistentDebugLines

Flush all persistent debug lines and shapes.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugFrustum

Draws a debug frustum.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| FrustumTransform | FTransform &  |  | cppstruct/detail/FTransform.json |
| FrustumColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugCamera

Draw a debug camera shape.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CameraActor | ACameraActor *  |  |  |
| CameraColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugFloatHistoryTransform

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawTransform for the position in the world.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| FloatHistory | FDebugFloatHistory &  |  |  |
| DrawTransform | FTransform &  |  | cppstruct/detail/FTransform.json |
| DrawSize | FVector2D  |  | cppstruct/detail/FVector2D.json |
| DrawColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugFloatHistoryLocation

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawLocation for the location in the world, rotation will face camera of first player.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| FloatHistory | FDebugFloatHistory &  |  |  |
| DrawLocation | FVector  |  | cppstruct/detail/FVector.json |
| DrawSize | FVector2D  |  | cppstruct/detail/FVector2D.json |
| DrawColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddFloatHistorySample

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| FloatHistory | FDebugFloatHistory & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDebugFloatHistory  |  |  |

### DrawDebugActorMoveTrack

绘制Actor运动轨迹

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| LinearColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugActorName

绘制Actor名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| Offset | FVector  |  | cppstruct/detail/FVector.json |
| LinearColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugDistance

绘制Self到Tartget的连线与距离

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Self | FVector  |  | cppstruct/detail/FVector.json |
| Target | FVector  |  | cppstruct/detail/FVector.json |
| LinearColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugTargetAimedAt

绘制准心瞄准物体名称

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Length | float  |  |  |
| DrawTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugActorCollision

绘制碰撞盒

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| LinearColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawDebugActorBounds

绘制Actor的包围盒

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| LinearColor | FLinearColor  |  | cppstruct/detail/FLinearColor.json |
| Duration | float  |  |  |
| Thickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CreateCopyForUndoBuffer

Mark as modified.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectToModify | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetComponentBounds

Get bounds

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | USceneComponent *  |  |  |
| Origin | FVector &  |  | cppstruct/detail/FVector.json |
| BoxExtent | FVector &  |  | cppstruct/detail/FVector.json |
| SphereRadius | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetActorBounds

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| Origin | FVector &  |  | cppstruct/detail/FVector.json |
| BoxExtent | FVector & |  | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetRenderingDetailMode

Get the clamped state of r.DetailMode, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low, show only object with DetailMode low or higher
	  1: medium, show all object with DetailMode medium or higher
	  2: high, show all objects

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetRenderingMaterialQualityLevel

Get the clamped state of r.MaterialQualityLevel, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low
	  1: high
	  2: medium
	  3: ultimatehigh

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetSupportedFullscreenResolutions

Gets the list of support fullscreen resolutions.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Resolutions | TArray < FIntPoint > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if successfully queried the device for available resolutions. |  |

### GetConvenientWindowedResolutions

Gets the list of windowed resolutions which are convenient for the current primary display size.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Resolutions | TArray < FIntPoint > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if successfully queried the device for available resolutions. |  |

### GetMinYResolutionForUI

Gets the smallest Y resolution we want to support in the UI, clamped within reasons

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | value in pixels |  |

### GetMinYResolutionFor3DView

Gets the smallest Y resolution we want to support in the 3D view, clamped within reasons

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | value in pixels |  |

### LaunchURL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CanLaunchURL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### CollectGarbage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bFullPurge | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTimeSinceLastPendingKillPurge

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### ShowAdBanner

Will show an ad banner (iAd on iOS, or AdMob on Android) on the top or bottom of screen, on top of the GL view (doesn't resize the view)
	  (iOS and Android only)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AdIdIndex | int32  | The index of the ID to select for the ad to show |  |
| bShowOnBottomOfScreen | bool | If true, the iAd will be shown at the bottom of the screen, top otherwise |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAdIDCount

Retrieves the total number of Ad IDs that can be selected between

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### HideAdBanner

Hides the ad banner (iAd on iOS, or AdMob on Android). Will force close the ad if it's open
	  (iOS and Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ForceCloseAdBanner

Forces closed any displayed ad. Can lead to loss of revenue
	  (iOS and Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### LoadInterstitialAd

Will load a fullscreen interstitial AdMob ad. Call this before using ShowInterstitialAd
	 (Android only)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AdIdIndex | int32 | The index of the ID to select for the ad to show |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsInterstitialAdAvailable

Returns true if the requested interstitial ad is loaded and ready
	 (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsInterstitialAdRequested

Returns true if the requested interstitial ad has been successfully requested (false if load request fails)
	 (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ShowInterstitialAd

Shows the loaded interstitial ad (loaded with LoadInterstitialAd)
	 (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ShowPlatformSpecificLeaderboardScreen

Displays the built-in leaderboard GUI (iOS and Android only; this function may be renamed or moved in a future release)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CategoryName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ShowPlatformSpecificAchievementsScreen

Displays the built-in achievements GUI (iOS and Android only; this function may be renamed or moved in a future release)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SpecificPlayer | APlayerController * | Specific player's achievements to show. May not be supported on all platforms. If null, defaults to the player with ControllerId 0 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsLoggedIn

Returns whether the player is logged in to the currently active online subsystem.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SpecificPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ControlScreensaver

Allows or inhibits screensaver

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAllowScreenSaver | bool | If false, don't allow screensaver if possible, otherwise allow default behavior |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVolumeButtonsHandledBySystem

Allows or inhibits system default handling of volume up and volume down buttons (Android only)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool |  If true, allow Android to handle volume up and down events |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetVolumeButtonsHandledBySystem

Returns true if system default handling of volume up and volume down buttons enabled (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ResetGamepadAssignments

Resets the gamepad to player controller id assignments (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetGamepadAssignmentToController

Resets the gamepad assignment to player controller id (Android only)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControllerId | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsControllerAssignedToGamepad

Returns true if controller id assigned to a gamepad (Android only)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControllerId | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetSuppressViewportTransitionMessage

Sets the state of the transition message rendered by the viewport. (The blue text displayed when the game is paused and so forth.)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  | World context |  |
| bState | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPreferredLanguages

Returns an array of the user's preferred languages in order of preference

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FString > | An array of language IDs ordered from most preferred to least |  |

### GetDefaultLanguage

Get the default language (for localization) used by this platform

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The language as an IETF language tag (eg, "zh-Hans-CN") |  |

### GetDefaultLocale

Get the default locale (for internationalization) used by this platform

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The locale as an IETF language tag (eg, "zh-Hans-CN") |  |

### GetLocalCurrencyCode

Returns the currency code associated with the device's locale

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | the currency code associated with the device's locale |  |

### GetLocalCurrencySymbol

Returns the currency symbol associated with the device's locale

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | the currency symbol associated with the device's locale |  |

### RegisterForRemoteNotifications

Requests permission to send remote notifications to the user's device.
	  (Android and iOS only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UnregisterForRemoteNotifications

Requests Requests unregistering from receiving remote notifications to the user's device.
	 (Android only)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetUserActivity

Tells the engine what the user is doing for debug, analytics, etc.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UserActivity | FUserActivity & |  | cppstruct/detail/FUserActivity.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCommandLine

Returns the command line that the process was launched with.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### GetObjectFromPrimaryAssetId

Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### GetClassFromPrimaryAssetId

Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSubclassOf < UObject >  |  |  |

### GetSoftObjectReferenceFromPrimaryAssetId

Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSoftObjectPtr < UObject >  |  |  |

### GetSoftClassReferenceFromPrimaryAssetId

Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TSoftClassPtr < UObject >  |  |  |

### GetPrimaryAssetIdFromObject

Returns the Primary Asset Id for an Object, this can return an invalid one if not registered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |

### GetPrimaryAssetIdFromClass

Returns the Primary Asset Id for a Class, this can return an invalid one if not registered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Class | TSubclassOf < UObject > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |

### GetPrimaryAssetIdFromSoftObjectReference

Returns the Primary Asset Id for a Soft Object Reference, this can return an invalid one if not registered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftObjectReference | TSoftObjectPtr < UObject > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |

### GetPrimaryAssetIdFromSoftClassReference

Returns the Primary Asset Id for a Soft Class Reference, this can return an invalid one if not registered

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoftClassReference | TSoftClassPtr < UObject > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |

### GetPrimaryAssetIdList

Returns list of PrimaryAssetIds for a PrimaryAssetType

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetType | FPrimaryAssetType  |  | cppstruct/detail/FPrimaryAssetType.json |
| OutPrimaryAssetIdList | TArray < FPrimaryAssetId > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsValidPrimaryAssetId

Returns true if the Primary Asset Id is valid

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_PrimaryAssetIdToString

Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### EqualEqual_PrimaryAssetId

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |
| B | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_PrimaryAssetId

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |
| B | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValidPrimaryAssetType

Returns list of Primary Asset Ids for a PrimaryAssetType

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetType | FPrimaryAssetType |  | cppstruct/detail/FPrimaryAssetType.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_PrimaryAssetTypeToString

Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetType | FPrimaryAssetType |  | cppstruct/detail/FPrimaryAssetType.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### EqualEqual_PrimaryAssetType

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FPrimaryAssetType  |  | cppstruct/detail/FPrimaryAssetType.json |
| B | FPrimaryAssetType |  | cppstruct/detail/FPrimaryAssetType.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_PrimaryAssetType

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FPrimaryAssetType  |  | cppstruct/detail/FPrimaryAssetType.json |
| B | FPrimaryAssetType |  | cppstruct/detail/FPrimaryAssetType.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UnloadPrimaryAsset

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId |  | cppstruct/detail/FPrimaryAssetId.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnloadPrimaryAssetList

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetIdList | TArray < FPrimaryAssetId > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentBundleState

Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
	  If ForceCurrentState is true it will return the current state even if a load is in process

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PrimaryAssetId | FPrimaryAssetId  |  | cppstruct/detail/FPrimaryAssetId.json |
| bForceCurrentState | bool  |  |  |
| OutBundles | TArray < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetPrimaryAssetsWithBundleState

Returns the list of assets that are in a given bundle state. Required Bundles must be specified
	  If ExcludedBundles is not empty, it will not return any assets in those bundle states
	  If ValidTypes is not empty, it will only return assets of those types
	  If ForceCurrentState is true it will use the current state even if a load is in process

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RequiredBundles | TArray < FName > &  |  |  |
| ExcludedBundles | TArray < FName > &  |  |  |
| ValidTypes | TArray < FPrimaryAssetType > &  |  |  |
| bForceCurrentState | bool  |  |  |
| OutPrimaryAssetIdList | TArray < FPrimaryAssetId > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddResMapping

Functions for Asset Redirect

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPackageNameRemap | TMap < FName , FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddResPathMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPackagePathRemap | TMap < FString , FString > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddResARMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InARPaths | TSet < FString > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IterateAddResARMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InARRoot | FString &  |  |  |
| InARPaths | TSet < FString > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IterateRemoveResARMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InARRoot | FString &  |  |  |
| InARPaths | TSet < FString > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsResARMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InARPath | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RemoveResMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PathKeys | TArray < FString > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EmptyResMapping

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### AddBlackResMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPackageNames | TSet < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveBlackResMapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPackageNames | TSet < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EmptyBlackResMapping

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BindPackageNameResolver

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UnBindPackageNameResolver

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsPackageNameResolverBinded

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsARPathActivated

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InARPath | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetOriginalPath

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Path | FName &  |  |  |
| OriginalPath | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetDelegateResolvedPackagePath

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSourcePackagePath | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

# UBlueprintPlatformLibrary

- Symbol Type: class
- Symbol Path: Others / UBlueprintPlatformLibrary
- Source JSON Path: class/detail/Others/UBlueprintPlatformLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintPlatformLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Functions

### ClearAllLocalNotifications

Clear all pending local notifications. Typically this will be done before scheduling new notifications when going into the background

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ScheduleLocalNotificationAtTime

Schedule a local notification at a specific time, inLocalTime specifies the current local time or if UTC time should be used

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FireDateTime | FDateTime &  | The time at which to fire the local notification |  |
| LocalTime | bool  | If true the provided time is in the local timezone, if false it is in UTC |  |
| Title | FText &  | The title of the notification |  |
| Body | FText &  | The more detailed description of the notification |  |
| Action | FText &  | The text to be displayed on the slider controller |  |
| ActivationEvent | FString & | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScheduleLocalNotificationFromNow

Schedule a local notification to fire inSecondsFromNow from now

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| inSecondsFromNow | int32  | The seconds until the notification should fire |  |
| Title | FText &  | The title of the notification |  |
| Body | FText &  | The more detailed description of the notification |  |
| Action | FText &  | The text to be displayed on the slider controller |  |
| ActivationEvent | FString & | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScheduleLocalNotificationBadgeAtTime

Schedule a local notification badge at a specific time, inLocalTime specifies the current local time or if UTC time should be used

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FireDateTime | FDateTime &  | The time at which to fire the local notification |  |
| LocalTime | bool  | If true the provided time is in the local timezone, if false it is in UTC |  |
| ActivationEvent | FString & | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ScheduleLocalNotificationBadgeFromNow

Schedule a local notification badge to fire inSecondsFromNow from now

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| inSecondsFromNow | int32  | The seconds until the notification should fire |  |
| ActivationEvent | FString & | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CancelLocalNotification

Cancel a local notification given the ActivationEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActivationEvent | FString & | The string passed into the Schedule call for the notification to be cancelled |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLaunchNotification

Get the local notification that was used to launch the app

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NotificationLaunchedApp | bool &  | Return true if a notification was used to launch the app |  |
| ActivationEvent | FString &  | Returns the name of the ActivationEvent if a notification was used to launch the app |  |
| FireDate | int32 & | Returns the time the notification was activated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

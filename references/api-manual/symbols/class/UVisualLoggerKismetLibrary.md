# UVisualLoggerKismetLibrary

- Symbol Type: class
- Symbol Path: Others / UVisualLoggerKismetLibrary
- Source JSON Path: class/detail/Others/UVisualLoggerKismetLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UVisualLoggerKismetLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Functions

### LogText

Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Text | FString  |  |  |
| LogCategory | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### LogLocation

Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Location | FVector  |  |  |
| Text | FString  |  |  |
| ObjectColor | FLinearColor  |  |  |
| Radius | float  |  |  |
| LogCategory | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### LogBox

Logs box shape - recording for Visual Logs has to be enabled to record this data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| BoxShape | FBox  |  |  |
| Text | FString  |  |  |
| ObjectColor | FLinearColor  |  |  |
| LogCategory | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

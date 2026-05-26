# UKismetGuidLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetGuidLibrary
- Source JSON Path: class/detail/Others/UKismetGuidLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetGuidLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### EqualEqual_GuidGuid

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGuid &  |  |  |
| B | FGuid & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_GuidGuid

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGuid &  |  |  |
| B | FGuid & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsValid_Guid

Checks whether the given GUID is valid

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InGuid | FGuid & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Invalidate_Guid

Invalidates the given GUID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InGuid | FGuid & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### NewGuid

Returns a new unique GUID

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGuid |  |  |

### Conv_GuidToString

Converts a GUID value to a string, in the form 'A-B-C-D'

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InGuid | FGuid & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### Parse_StringToGuid

Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GuidString | FString &  |  |  |
| OutGuid | FGuid &  |  |  |
| Success | bool & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

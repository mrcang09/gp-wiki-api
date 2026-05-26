# UPlatformInterfaceWebResponse

- Symbol Type: class
- Symbol Path: Others / UPlatformInterfaceWebResponse
- Source JSON Path: class/detail/Others/UPlatformInterfaceWebResponse.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPlatformInterfaceWebResponse.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OriginalURL | FString | This holds the original requested URL |  |
| ResponseCode | int32 | Result code from the response (200=OK, 404=Not Found, etc) |  |
| Tag | int32 | A user-specified tag specified with the request |  |
| StringResponse | FString | For string results, this is the response |  |
| BinaryResponse | TArray < uint8 > | For non-string results, this is the response |  |

## Functions

### GetNumHeaders

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | the number of headervalue pairs |  |

### GetHeader

Retrieve the header and value for the given index of headervalue pair

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HeaderIndex | int32  |  |  |
| Header | FString &  |  |  |
| Value | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetHeaderValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HeaderName | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | the value for the given header (or "" if no matching header) |  |

# UKismetStringTableLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetStringTableLibrary
- Source JSON Path: class/detail/Others/UKismetStringTableLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetStringTableLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### IsRegisteredTableId

Returns true if the given table ID corresponds to a registered string table.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsRegisteredTableEntry

Returns true if the given table ID corresponds to a registered string table, and that table has.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName  |  |  |
| Key | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetTableNamespace

Returns the namespace of the given string table.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetTableEntrySourceString

Returns the source string of the given string table entry (or an empty string).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName  |  |  |
| Key | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetTableEntryMetaData

Returns the specified meta-data of the given string table entry (or an empty string).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName  |  |  |
| Key | FString &  |  |  |
| MetaDataId | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetRegisteredStringTables

Returns an array of all registered string table IDs

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FName > |  |  |

### GetKeysFromStringTable

Returns an array of all keys within the given string table

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FString >  |  |  |

### GetMetaDataIdsFromStringTableEntry

Returns an array of all meta-data IDs within the given string table entry

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName  |  |  |
| Key | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FName >  |  |  |

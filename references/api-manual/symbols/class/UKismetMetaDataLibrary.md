# UKismetMetaDataLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetMetaDataLibrary
- Source JSON Path: class/detail/Others/UKismetMetaDataLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetMetaDataLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### HasMetaData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Field | UField *  |  |  |
| Key | FName  |  |  |
| NameIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetMetaData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Field | UField *  |  |  |
| Key | FName  |  |  |
| NameIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const FString &  |  |  |

### GetEnum

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EnumProperty | UEnumProperty * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UEnum *  |  |  |

### GetEnumFromByte

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ByteProperty | UByteProperty * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UEnum *  |  |  |

### GetNumOfEnum

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetEnumName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  |  |  |
| NameIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### GetEnumValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  |  |  |
| NameIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### GetEnumIndexByValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  |  |  |
| Value | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetScriptStructOfStructProperty

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StructProperty | UStructProperty * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UScriptStruct *  |  |  |

### GetClassOfObjectPropertyBase

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectPropertyBase | UObjectPropertyBase * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  |  |  |

### GetObjectsWithOuter

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Outer | UObject *  |  |  |
| bIncludeNestedObjects | bool  |  |  |
| ExclusionFlags | int32  |  |  |
| ExclusionInternalFlags | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UObject * >  |  |  |

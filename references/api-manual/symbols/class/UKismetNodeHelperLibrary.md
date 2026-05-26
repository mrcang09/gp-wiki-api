# UKismetNodeHelperLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetNodeHelperLibrary
- Source JSON Path: class/detail/Others/UKismetNodeHelperLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetNodeHelperLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### BitIsMarked

Returns whether the bit at index "Index" is set or not in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The integer containing the bits that are being tested against |  |
| Index | int32 | - The bit index into the Data that we are inquiring |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  - Whether the bit at index "Index" is set or not |  |

### MarkBit

Sets the bit at index "Index" in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32 &  | - The integer containing the bits that are being set |  |
| Index | int32 | - The bit index into the Data that we are setting |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearBit

Clears the bit at index "Index" in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32 &  | - The integer containing the bits that are being cleared |  |
| Index | int32 | - The bit index into the Data that we are clearing |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAllBits

Clears all of the bit in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32 & | - The integer containing the bits that are being cleared |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HasUnmarkedBit

Returns whether there exists an unmarked bit in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The data being tested against |  |
| NumBits | int32 | - The logical number of bits we want to track |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | - Whether there is a bit not marked in the data |  |

### HasMarkedBit

Returns whether there exists a marked bit in the data

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The data being tested against |  |
| NumBits | int32 | - The logical number of bits we want to track |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | - Whether there is a bit marked in the data |  |

### GetUnmarkedBit

Gets an already unmarked bit and returns the bit index selected

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The integer containing the bits that are being set |  |
| StartIdx | int32  | - The index to start with when determining the selection' |  |
| NumBits | int32  | - The logical number of bits we want to track |  |
| bRandom | bool | - Whether to select a random index or not |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |  |

### GetRandomUnmarkedBit

Gets a random not already marked bit and returns the bit index selected

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The integer containing the bits that are being set |  |
| StartIdx | int32  |  |  |
| NumBits | int32 | - The logical number of bits we want to track |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |  |

### GetFirstUnmarkedBit

Gets the first index not already marked starting from a specific index and returns the bit index selected

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | int32  | - The integer containing the bits that are being set |  |
| StartIdx | int32  | - The index to start looking for an available index from |  |
| NumBits | int32 | - The logical number of bits we want to track |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |  |

### GetEnumeratorName

Gets enumerator name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  | - Enumeration |  |
| EnumeratorValue | uint8 | - Value of searched enumeration |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | - name of the searched enumerator, or NAME_None |  |

### GetEnumeratorUserFriendlyName

Gets enumerator name as FString. Use DeisplayName when possible.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  | - Enumeration |  |
| EnumeratorValue | uint8 | - Value of searched enumeration |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | - name of the searched enumerator, or NAME_None |  |

### GetValidValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  | - Enumeration |  |
| EnumeratorValue | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  | - if EnumeratorIndex is valid return EnumeratorIndex, otherwise return MAX value of Enum |  |

### GetEnumeratorValueFromIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Enum | UEnum *  | - Enumeration |  |
| EnumeratorIndex | uint8 | - Input index |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  | - The value of the enumerator, or INDEX_NONE |  |

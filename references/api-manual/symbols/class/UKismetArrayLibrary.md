# UKismetArrayLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetArrayLibrary
- Source JSON Path: class/detail/Others/UKismetArrayLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetArrayLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### Array_Add

Add item to array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to add item to |  |
| NewItem | int32 & |  The item to add to the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The index of the newly added item |  |

### Array_AddUnique

Add item to array (unique)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to add item to |  |
| NewItem | int32 & |  The item to add to the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The index of the newly added item, or INDEX_NONE if the item is already present in the array |  |

### Array_Shuffle

Shuffle (randomize) the elements of an array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > & | The array to shuffle |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Append

Append an array to another array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to add the source array to |  |
| SourceArray | TArray < int32 > & | The array to add to the target array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Insert

Insert item at the given index into the array.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to insert into |  |
| NewItem | int32 &  |  The item to insert into the array |  |
| Index | int32 |  The index at which to insert the item into the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Remove

Remove item at the given index from the array.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to remove from |  |
| IndexToRemove | int32 | The index into the array to remove from |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_RemoveItem

Remove all instances of item from array.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to remove from |  |
| Item | int32 & |  The item to remove from the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if one or more items were removed |  |

### Array_Clear

Clear an array, removes all content

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > & | The array to clear |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Resize

Resize Array to specified size.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to resize |  |
| Size | int32 |  The new size of the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Length

Get the number of items in an array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > & | The array to get the length of |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The length of the array |  |

### Array_LastIndex

Get the last valid index into an array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > & | The array to perform the operation on |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The last valid index of the array |  |

### Array_Get

Given an array and an index, returns a copy of the item found at that index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to get an item from |  |
| Index | int32  |  The index in the array to get an item from |  |
| Item | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | A copy of the item stored at the index |  |

### Array_Set

Given an array and an index, assigns the item to that array element

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to perform the operation on |  |
| Index | int32  |  The index to assign the item to |  |
| Item | int32 &  |  The item to assign to the index of the array |  |
| bSizeToFit | bool | If true, the array will expand if Index is greater than the current size of the array |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Swap

Swaps the elements at the specified positions in the specified array
	 If the specified positions are equal, invoking this method leaves the array unchanged

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to perform the operation on |  |
| FirstIndex | int32  |  |  |
| SecondIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_Find

Finds the index of the first instance of the item within the array

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to search for the item |  |
| ItemToFind | int32 & | The item to look for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The index the item was found at, or -1 if not found |  |

### Array_Contains

Returns true if the array contains the given item

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | The array to search for the item |  |
| ItemToFind | int32 & | The item to look for |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the item was found within the array |  |

### FilterArray

Filter an array based on a Class derived from Actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < AActor * > &  | The array to filter from |  |
| FilterClass | TSubclassOf < AActor >  | The Actor sub-class type that acts as the filter, only objects derived from it will be returned. |  |
| FilteredArray | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | An array containing only those objects which are derived from the class specified. |  |

### SetArrayPropertyByName

Not exposed to users. Supports setting an array property on an object by name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Object | UObject *  |  |  |
| PropertyName | FName  |  |  |
| Value | TArray < int32 > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Array_IsValidIndex

Tests if IndexToTest is valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TargetArray | TArray < int32 > &  | Array to use for the IsValidIndex test |  |
| IndexToTest | int32 | The Index, that we want to test for being valid |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the Index is Valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray. |  |

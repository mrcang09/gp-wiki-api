# UKismetPackageNameLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetPackageNameLibrary
- Source JSON Path: class/detail/Others/UKismetPackageNameLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetPackageNameLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### IsValidLongPackageName

Helper function for converting short to long script package name (InputCore -> ScriptInputCore)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLongPackageName | FString &  | Long Package Name |  |
| bIncludeReadOnlyRoots | bool  | If true, will include roots that you should not save to. (Temp, Script) |  |
| OutReason | FText & |   When returning false, this will provide a description of what was wrong with the name. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 						true if a valid long package name |  |

### IsValidObjectPath

Returns true if the path starts with a valid root (i.e. Game, Engine, etc) and contains no illegal characters.
	  This validates that the packagename is valid, and also makes sure the object after package name is also correct.
	  This will return false if passed a path starting with Classname'

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InObjectPath | FString &  |  The object path to test |  |
| OutReason | FText & |   When returning false, this will provide a description of what was wrong with the name. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 						true if a valid object path |  |

### DoesPackageExist

Checks if the given string is a long package name or not.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LongPackageName | FString &  | Package name. |  |
| Guid | FGuid &  |  |  |
| OutFilename | FString & | Package filename on disk. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if the specified package name points to an existing package, false otherwise. |  |

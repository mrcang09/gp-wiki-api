# UAssetRegistryHelpers

- Symbol Type: class
- Symbol Path: Others / UAssetRegistryHelpers
- Source JSON Path: class/detail/Others/UAssetRegistryHelpers.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAssetRegistryHelpers.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Functions

### GetAssetRegistry

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TScriptInterface < IAssetRegistry > |  |  |

### CreateAssetData

Creates asset data from a UObject.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAsset | UObject *  | The asset to create asset data for |  |
| bAllowBlueprintClass | bool | By default trying to create asset data for a blueprint class will create one for the UBlueprint instead |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FAssetData  |  |  |

### IsValid

Checks to see if this AssetData refers to an asset or is NULL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsUAsset

Returns true if this asset was found in a UAsset file

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsRedirector

Returns true if the this asset is a redirector.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetFullName

Returns the full name for the asset in the form: Class ObjectPath

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### ToSoftObjectPath

Convert to a SoftObjectPath for loading

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath  |  |  |

### GetClass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  |  |  |

### GetAsset

Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### IsAssetLoaded

Returns true if the asset is loaded

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetExportTextName

Returns the name for the asset in the form: Class'ObjectPath'

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetTagValue < FName >

Gets the value associated with the given tag as a string

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAssetData | FAssetData &  |  |  |
| InTagName | FName &  |  |  |
| OutTagValue | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetFilterTagsAndValues

Populates the FARFilters tags and values map with the passed in tags and values

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFilter | FARFilter &  |  |  |
| InTagsAndValues | TArray < FTagAndValue > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FARFilter  |  |  |

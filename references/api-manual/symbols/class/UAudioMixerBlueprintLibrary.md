# UAudioMixerBlueprintLibrary

- Symbol Type: class
- Symbol Path: Others / UAudioMixerBlueprintLibrary
- Source JSON Path: class/detail/Others/UAudioMixerBlueprintLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAudioMixerBlueprintLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Functions

### AddMasterSubmixEffect

Adds a submix effect preset to the master submix.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SubmixEffectPreset | USoundEffectSubmixPreset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveMasterSubmixEffect

Removes a submix effect preset from the master submix.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SubmixEffectPreset | USoundEffectSubmixPreset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMasterSubmixEffects

Clears all master submix effects.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddSourceEffectToPresetChain

Adds source effect entry to preset chain. Only effects the instance of the preset chain

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PresetChain | USoundEffectSourcePresetChain *  |  |  |
| Entry | FSourceEffectChainEntry |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveSourceEffectFromPresetChain

Adds source effect entry to preset chain. Only affects the instance of preset chain.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PresetChain | USoundEffectSourcePresetChain *  |  |  |
| EntryIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBypassSourceEffectChainEntry

Set whether or not to bypass the effect at the source effect chain index.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PresetChain | USoundEffectSourcePresetChain *  |  |  |
| EntryIndex | int32  |  |  |
| bBypassed | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNumberOfEntriesInSourceEffectChain

Returns the number of effect chain entries in the given source effect chain.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| PresetChain | USoundEffectSourcePresetChain * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

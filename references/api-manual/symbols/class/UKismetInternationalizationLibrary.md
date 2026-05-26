# UKismetInternationalizationLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetInternationalizationLibrary
- Source JSON Path: class/detail/Others/UKismetInternationalizationLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetInternationalizationLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Functions

### SetCurrentCulture

Set the current culture.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Culture | FString &  | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the culture was set, false otherwise. |  |

### GetCurrentCulture

Get the current culture as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The culture as an IETF language tag (eg, "zh-Hans-CN"). |  |

### SetCurrentLanguage

Set only the current language (for localization).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Culture | FString &  | The language to set, as an IETF language tag (eg, "zh-Hans-CN"). |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the language was set, false otherwise. |  |

### GetCurrentLanguage

Get the current language (for localization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The language as an IETF language tag (eg, "zh-Hans-CN"). |  |

### SetCurrentLocale

Set only the current locale (for internationalization).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Culture | FString &  | The locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the locale was set, false otherwise. |  |

### GetCurrentLocale

Get the current locale (for internationalization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | The locale as an IETF language tag (eg, "zh-Hans-CN"). |  |

### SetCurrentLanguageAndLocale

Set the current language (for localization) and locale (for internationalization).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Culture | FString &  | The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the language and locale were set, false otherwise. |  |

### SetCurrentAssetGroupCulture

Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetGroup | FName  | The asset group to set the culture for. |  |
| Culture | FString &  | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the culture was set, false otherwise. |  |

### GetCurrentAssetGroupCulture

Get the given asset group category culture.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetGroup | FName | The asset group to get the culture for. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | The culture as an IETF language tag (eg, "zh-Hans-CN"). |  |

### ClearCurrentAssetGroupCulture

Clear the given asset group category culture.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AssetGroup | FName  | The asset group to clear the culture for. |  |
| SaveToConfig | bool | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

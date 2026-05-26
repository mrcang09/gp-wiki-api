# ULocalizedOverlays

- Symbol Type: class
- Symbol Path: Others / ULocalizedOverlays
- Source JSON Path: class/detail/Others/ULocalizedOverlays.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULocalizedOverlays.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

Implements an asset that contains a set of Basic Overlays that will be displayed in accordance with
  the current locale, or a default set if an appropriate locale is not found

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefaultOverlays | UBasicOverlays * | The overlays to use if no overlays are found for the current culture |  |
| LocaleToOverlaysMap | TMap < FString , UBasicOverlays * > | Maps a set of cultures to specific BasicOverlays assets.<br>	  Cultures are comprised of three hyphen-separated parts:<br>	 		A two-letter ISO 639-1 language code (e.g., "zh")<br>	 		An optional four-letter ISO 15924 script code (e.g., "Hans")<br>	 		An optional two-letter ISO 3166-1 country code  (e.g., "CN") |  |
| AssetImportData | UAssetImportData * | The import data used to make this overlays asset |  |

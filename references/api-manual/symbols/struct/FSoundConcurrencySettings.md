# FSoundConcurrencySettings

- Symbol Type: struct
- Symbol Path: FSoundConcurrencySettings
- Source JSON Path: cppstruct/detail/FSoundConcurrencySettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSoundConcurrencySettings.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaxCount | int32 | The max number of allowable concurrent active voices for voices playing in this concurrency group. |  |
| bLimitToOwner | uint32 | Whether or not to limit the concurrency to per sound owner (i.e. the actor that plays the sound). If the sound doesn't have an owner, it falls back to global concurrency. |  |
| ResolutionRule | TEnumAsByte < enum EMaxConcurrentResolutionRule :: Type > | Which concurrency resolution policy to use if max voice count is reached. |  |
| VolumeScale | float | The amount of attenuation to apply to older voice instances in this concurrency group. This reduces volume of older voices in a concurrency group as new voices play.<br>	 <br>	  AppliedVolumeScale = Math.Pow(DuckingScale, VoiceGeneration) |  |

# UPlatformMediaSource

- Symbol Type: class
- Symbol Path: Others / UPlatformMediaSource
- Source JSON Path: class/detail/Others/UPlatformMediaSource.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPlatformMediaSource.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

A media source that selects other media sources based on target platform.
 
  Use this asset to override media sources on a per-platform basis.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MediaSource | UMediaSource * | Default media source.<br>	 <br>	  This media source will be used if no source was specified for a target platform. |  |
| PlatformMediaSources | TMap < FString , UMediaSource * > | Media sources per platform. |  |

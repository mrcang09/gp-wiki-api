# FCameraCacheEntry

- Symbol Type: struct
- Symbol Path: FCameraCacheEntry
- Source JSON Path: cppstruct/detail/FCameraCacheEntry.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCameraCacheEntry.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Cached camera POV info, stored as optimization so we only
  need to do a full camera update once per tick.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TimeStamp | float | World time this entry was created. |  |
| POV | FMinimalViewInfo | Camera POV to cache. |  |

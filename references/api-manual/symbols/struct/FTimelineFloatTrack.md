# FTimelineFloatTrack

- Symbol Type: struct
- Symbol Path: FTimelineFloatTrack
- Source JSON Path: cppstruct/detail/FTimelineFloatTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTimelineFloatTrack.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

Struct that contains one entry for each vector interpolation performed by the timeline

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FloatCurve | UCurveFloat * | Float curve to be evaluated |  |
| TrackName | FName | Name of track, usually set in Timeline Editor. Used by SetInterpFloatCurve function. |  |
| FloatPropertyName | FName | Name of property that we should update from this curve |  |
| FloatProperty | UFloatProperty * | Cached float property pointer |  |

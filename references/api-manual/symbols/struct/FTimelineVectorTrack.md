# FTimelineVectorTrack

- Symbol Type: struct
- Symbol Path: FTimelineVectorTrack
- Source JSON Path: cppstruct/detail/FTimelineVectorTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTimelineVectorTrack.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

Struct that contains one entry for each vector interpolation performed by the timeline

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VectorCurve | UCurveVector * | Vector curve to be evaluated |  |
| TrackName | FName | Name of track, usually set in Timeline Editor. Used by SetInterpVectorCurve function. |  |
| VectorPropertyName | FName | Name of property that we should update from this curve |  |
| VectorProperty | UStructProperty * | Cached vector struct property pointer |  |

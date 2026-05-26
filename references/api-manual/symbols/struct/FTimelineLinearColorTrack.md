# FTimelineLinearColorTrack

- Symbol Type: struct
- Symbol Path: FTimelineLinearColorTrack
- Source JSON Path: cppstruct/detail/FTimelineLinearColorTrack.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTimelineLinearColorTrack.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

Struct that contains one entry for each linear color interpolation performed by the timeline

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LinearColorCurve | UCurveLinearColor * | Float curve to be evaluated |  |
| TrackName | FName | Name of track, usually set in Timeline Editor. Used by SetInterpLinearColorCurve function. |  |
| LinearColorPropertyName | FName | Name of property that we should update from this curve |  |
| LinearColorProperty | UStructProperty * | Cached linear color struct property pointer |  |

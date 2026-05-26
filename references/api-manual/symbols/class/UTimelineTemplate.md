# UTimelineTemplate

- Symbol Type: class
- Symbol Path: Others / UTimelineTemplate
- Source JSON Path: class/detail/Others/UTimelineTemplate.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTimelineTemplate.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TimelineLength | float | Length of this timeline |  |
| LengthMode | TEnumAsByte < ETimelineLengthMode > | How we want the timeline to determine its own length (e.g. specified length, last keyframe) |  |
| bAutoPlay | uint32 | If we want the timeline to auto-play |  |
| bLoop | uint32 | If we want the timeline to loop |  |
| bReplicated | uint32 | If we want the timeline to loop |  |
| bValidatedAsWired | uint32 | Compiler Validated As Wired up |  |
| bIgnoreTimeDilation | uint32 | If we want the timeline to ignore global time dilation |  |
| EventTracks | TArray < struct FTTEventTrack > | Set of event tracks |  |
| FloatTracks | TArray < struct FTTFloatTrack > | Set of float interpolation tracks |  |
| VectorTracks | TArray < struct FTTVectorTrack > | Set of vector interpolation tracks |  |
| LinearColorTracks | TArray < struct FTTLinearColorTrack > | Set of linear color interpolation tracks |  |
| MetaDataArray | TArray < struct FBPVariableMetaDataEntry > | Metadata information for this timeline |  |
| TimelineGuid | FGuid |  |  |

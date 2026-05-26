# ALevelStreamingVolume

- Symbol Type: class
- Symbol Path: Others / ALevelStreamingVolume
- Source JSON Path: class/detail/Others/ALevelStreamingVolume.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ALevelStreamingVolume.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StreamingLevelNames | TArray < FName > | Levels names affected by this level streaming volume. |  |
| bEditorPreVisOnly | uint32 | If true, this streaming volume should only be used for editor streaming level previs. |  |
| bDisabled | uint32 | If true, this streaming volume is ignored by the streaming volume code.  Used to either<br>	  disable a level streaming volume without disassociating it from the level, or to toggle<br>	  the control of a level's streaming between Kismet and volume streaming. |  |
| StreamingUsage | TEnumAsByte < enum EStreamingVolumeUsage > | Determines what this volume is used for, e.g. whether to control loading, loading and visibility or just visibilty (blocking on load) |  |

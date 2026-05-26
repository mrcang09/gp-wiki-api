# UInterpTrackDirector

- Symbol Type: class
- Symbol Path: Others / UInterpTrackDirector
- Source JSON Path: class/detail/Others/UInterpTrackDirector.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackDirector.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CutTrack | TArray < struct FDirectorTrackCut > | Array of cuts between cameras. |  |
| bSimulateCameraCutsOnClients | uint32 | True to allow clients to simulate their own camera cuts.  Can help with latency-induced timing issues. |  |
| PreviewCamera | ACameraActor * | The camera actor which the track is currently focused on. Only valid if this track or it's group is selected |  |

# UParticleModuleSubUVMovie

- Symbol Type: class
- Symbol Path: Others / UParticleModuleSubUVMovie
- Source JSON Path: class/detail/Others/UParticleModuleSubUVMovie.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSubUVMovie.json
- Mirrored At (UTC): 2026-05-19 08:23:37Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseEmitterTime | uint32 | If true, use the emitter time to look up the frame rate.<br>	 	If false (default), use the particle relative time. |  |
| FrameRate | FRawDistributionFloat | The frame rate the SubUV images should be 'flipped' thru at. |  |
| StartingFrame | int32 | The starting image index for the SubUV (1 = the first frame).<br>	 	Assumes order of Left->Right, Top->Bottom<br>	 	If greater than the last frame, it will clamp to the last one.<br>	 	If 0, then randomly selects a starting frame. |  |
| bUseSmallImageIndex | uint32 | If true, ImageIndex will be limited in 0~NumFrames.<br>	 	If false (default), ImageIndex will increase all the time. |  |

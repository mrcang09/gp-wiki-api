# FCameraPreviewInfo

- Symbol Type: struct
- Symbol Path: FCameraPreviewInfo
- Source JSON Path: cppstruct/detail/FCameraPreviewInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCameraPreviewInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Preview APawn class for this track

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PawnClass | TSubclassOf < APawn > |  |  |
| AnimSeq | UAnimSequence * |  |  |
| Location | FVector | for now this is read-only. It has maintenance issue to be resolved if I enable this. |  |
| Rotation | FRotator |  |  |
| PawnInst | APawn * | APawn Inst - CameraAnimInst doesn't really exist in editor |  |

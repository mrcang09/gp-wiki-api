# FTViewTarget

- Symbol Type: struct
- Symbol Path: FTViewTarget
- Source JSON Path: cppstruct/detail/FTViewTarget.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTViewTarget.json
- Mirrored At (UTC): 2026-05-19 08:24:48Z

---

## Description

A ViewTarget is the primary actor the camera is associated with.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | AActor * | Target Actor used to compute POV |  |
| POV | FMinimalViewInfo | Computed point of view |  |
| PlayerState | APlayerState * | PlayerState (used to follow same player through pawn transitions, etc., when spectating) |  |

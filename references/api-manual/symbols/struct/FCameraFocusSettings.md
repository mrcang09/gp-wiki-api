# FCameraFocusSettings

- Symbol Type: struct
- Symbol Path: FCameraFocusSettings
- Source JSON Path: cppstruct/detail/FCameraFocusSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCameraFocusSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Settings to control camera focus

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FocusMethod | ECameraFocusMethod | Which method to use to handle camera focus |  |
| ManualFocusDistance | float | Manually-controlled focus distance (manual focus mode only) |  |
| TrackingFocusSettings | FCameraTrackingFocusSettings | Settings to control tracking focus (tracking focus mode only) |  |
| bDrawDebugFocusPlane | uint8 | True to draw a translucent plane at the current focus depth, for easy tweaking. |  |
| DebugFocusPlaneColor | FColor | For customizing the focus plane color, in case the default doesn't show up well in your scene. |  |
| bSmoothFocusChanges | uint8 | True to use interpolation to smooth out changes in focus distance, false for focus distance changes to be instantaneous. |  |
| FocusSmoothingInterpSpeed | float | Controls interpolation speed when smoothing focus distance changes. Ignored if bSmoothFocusChanges is false. |  |
| FocusOffset | float | Additional focus depth offset, used for manually tweaking if your chosen focus method needs adjustment |  |

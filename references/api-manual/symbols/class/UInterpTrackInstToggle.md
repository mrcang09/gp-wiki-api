# UInterpTrackInstToggle

- Symbol Type: class
- Symbol Path: Others / UInterpTrackInstToggle
- Source JSON Path: class/detail/Others/UInterpTrackInstToggle.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstToggle.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Action | TEnumAsByte < enum ETrackToggleAction > |  |  |
| LastUpdatePosition | float | Position we were in last time we evaluated.<br>	 	During UpdateTrack, toggles between this time and the current time will be processed. |  |
| bSavedActiveState | uint32 | Cached 'active' state for the toggleable actor before we possessed it; restored when Matinee exits |  |

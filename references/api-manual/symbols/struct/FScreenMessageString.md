# FScreenMessageString

- Symbol Type: struct
- Symbol Path: FScreenMessageString
- Source JSON Path: cppstruct/detail/FScreenMessageString.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FScreenMessageString.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Description

On-screen debug message handling 
 Helper struct for tracking on screen messages.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Key | uint64 | The 'key' for this message. |  |
| ScreenMessage | FString | The message to display. |  |
| DisplayColor | FColor | The color to display the message in. |  |
| TimeToDisplay | float | The number of frames to display it. |  |
| CurrentTimeDisplayed | float | The number of frames it has been displayed so far. |  |
| TextScale | FVector2D | Scale of text |  |
| IsUGCMsg | bool | Is ugc message |  |

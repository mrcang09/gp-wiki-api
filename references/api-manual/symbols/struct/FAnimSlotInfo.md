# FAnimSlotInfo

- Symbol Type: struct
- Symbol Path: FAnimSlotInfo
- Source JSON Path: cppstruct/detail/FAnimSlotInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSlotInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Struct used for passing information from Matinee to an Actor for blending animations during a sequence.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SlotName | FName | Name of slot that we want to play the animtion in. |  |
| ChannelWeights | TArray < float > | Strength of each Channel within this Slot. Channel indexs are determined by track order in Matinee. |  |

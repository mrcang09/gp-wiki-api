# UChannel

- Symbol Type: class
- Symbol Path: Others / UChannel
- Source JSON Path: class/detail/Others/UChannel.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UChannel.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

Base class of communication channels.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Connection | UNetConnection * |  |  |
| OpenAcked | uint32 |  |  |
| Closing | uint32 |  |  |
| Dormant | uint32 |  |  |
| bIsReplicationPaused | uint32 |  |  |
| OpenTemporary | uint32 |  |  |
| Broken | uint32 |  |  |
| bTornOff | uint32 |  |  |
| bPendingDormancy | uint32 |  |  |
| bPausedUntilReliableACK | uint32 |  |  |
| ChIndex | int32 |  |  |
| OpenedLocally | int32 |  |  |
| OpenPacketId | FPacketIdRange |  |  |
| ChType | EChannelType |  |  |
| NumInRec | int32 |  |  |
| NumOutRec | int32 |  |  |
| InRec | FInBunch * |  |  |
| OutRec | FOutBunch * |  |  |
| InPartialBunch | FInBunch * |  |  |
| bEnableSendBunchOpt | bool |  |  |

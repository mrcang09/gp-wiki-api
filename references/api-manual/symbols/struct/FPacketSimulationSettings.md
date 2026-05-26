# FPacketSimulationSettings

- Symbol Type: struct
- Symbol Path: FPacketSimulationSettings
- Source JSON Path: cppstruct/detail/FPacketSimulationSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FPacketSimulationSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Holds the packet simulation settings in one place

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PktLoss | int32 | When set, will cause calls to FlushNet to drop packets.<br>	  Value is treated as % of packets dropped (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br>	 <br>	  Works with all other settings. |  |
| PktOrder | int32 | When set, will cause calls to FlushNet to change ordering of packets at random.<br>	  Value is treated as a bool (i.e. 0 = False, anything else = True).<br>	  This works by randomly selecting packets to be delayed until a subsequent call to FlushNet.<br>	 <br>	  Takes precedence over PktDup and PktLag. |  |
| PktDup | int32 | When set, will cause calls to FlushNet to duplicate packets.<br>	  Value is treated as % of packets duplicated (i.e. 0 = None, 100 = All).<br>	  No general pattern  ordering is guaranteed.<br>	  Clamped between 0 and 100.<br>	 <br>	  Cannot be used with PktOrder or PktLag. |  |
| PktLag | int32 | When set, will cause calls to FlushNet to delay packets.<br>	  Value is treated as millisecond lag.<br>	 <br>	  Cannot be used with PktOrder. |  |
| PktIncomingLoss | int32 | The ratio of incoming packets that will be dropped<br>	  to simulate packet loss |  |
| PktLagVariance | int32 | When set, will cause PktLag to use variable lag instead of constant.<br>	  Value is treated as millisecond lag range (e.g. -GivenVariance <= 0 <= GivenVariance).<br>	  Clamped between 0 and 100.<br>	 <br>	  Can only be used when PktLag is enabled. |  |

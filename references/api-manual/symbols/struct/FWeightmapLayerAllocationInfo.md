# FWeightmapLayerAllocationInfo

- Symbol Type: struct
- Symbol Path: FWeightmapLayerAllocationInfo
- Source JSON Path: cppstruct/detail/FWeightmapLayerAllocationInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FWeightmapLayerAllocationInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

Stores information about which weightmap texture and channel each layer is stored

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LayerInfo | ULandscapeLayerInfoObject * |  |  |
| WeightmapTextureIndex | uint8 |  |  |
| WeightmapTextureChannel | uint8 |  |  |
| bUseForWeightmapPCOnly | TEnumAsByte < ELandscapeWeightmapUsage > |  |  |
| WeightmapTextureIndex_ForPC | uint8 |  |  |
| WeightmapTextureChannel_ForPC | uint8 |  |  |
| CustomWeightName | FName |  |  |
| CustomWeightChannelCount | int32 |  |  |

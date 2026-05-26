# FAnimSetMeshLinkup

- Symbol Type: struct
- Symbol Path: FAnimSetMeshLinkup
- Source JSON Path: cppstruct/detail/FAnimSetMeshLinkup.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimSetMeshLinkup.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

This is a mapping table between each bone in a particular skeletal mesh and the tracks of this animation set.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneToTrackTable | TArray < int32 > | Mapping table. Size must be same as size of SkelMesh reference skeleton. <br>	  No index should be more than the number of tracks in this AnimSet.<br>	  -1 indicates no track for this bone - will use reference pose instead. |  |

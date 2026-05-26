# FHLODProxyMesh

- Symbol Type: struct
- Symbol Path: FHLODProxyMesh
- Source JSON Path: cppstruct/detail/FHLODProxyMesh.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FHLODProxyMesh.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

A mesh proxy entry

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODActor | TLazyObjectPtr < ALODActor > | The ALODActor that we were generated from |  |
| StaticMesh | UStaticMesh * | The mesh used to display this proxy |  |
| Key | FName | The key generated from an ALODActor. If this differs from that generated from the ALODActor, then the mesh needs regenerating. |  |

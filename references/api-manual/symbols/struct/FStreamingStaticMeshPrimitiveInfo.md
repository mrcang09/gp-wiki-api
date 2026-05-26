# FStreamingStaticMeshPrimitiveInfo

- Symbol Type: struct
- Symbol Path: FStreamingStaticMeshPrimitiveInfo
- Source JSON Path: cppstruct/detail/FStreamingStaticMeshPrimitiveInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FStreamingStaticMeshPrimitiveInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:48Z

---

## Description

Information about a streaming StaticMesh that a primitive uses for rendering.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMesh | UStaticMesh * |  |  |
| Bounds | FBoxSphereBounds | The streaming bounds of the StaticMesh, usually the component material bounds. <br>	  Usually only valid for registered component, as component bounds are only updated when the components are registered.<br>	  otherwise only PackedRelativeBox can be used.Irrelevant when the component is not registered, as the component could be moved by ULevel::ApplyWorldOffset()<br>	  In that case, only PackedRelativeBox is meaningful. |  |

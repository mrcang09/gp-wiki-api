# FTextureLODGroup

- Symbol Type: struct
- Symbol Path: FTextureLODGroup
- Source JSON Path: cppstruct/detail/FTextureLODGroup.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FTextureLODGroup.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

LOD settings for a single texture group.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Group | TEnumAsByte < TextureGroup > | Minimum LOD mip count below which the code won't bias. |  |
| LODBias | int32 | Group LOD bias. |  |
| NumStreamedMips | int32 | Number of mip-levels that can be streamed. -1 means all mips can stream. |  |
| MipGenSettings | TEnumAsByte < TextureMipGenSettings > | Defines how the the mip-map generation works, e.g. sharpening |  |
| MinLODSize | int32 |  |  |
| MaxLODSize | int32 |  |  |
| MinMagFilter | FName |  |  |
| MipFilter | FName |  |  |

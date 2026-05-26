# UMaterialInterface

- Symbol Type: class
- Symbol Path: Others / UMaterialInterface
- Source JSON Path: class/detail/Others/UMaterialInterface.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInterface.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubsurfaceProfile | USubsurfaceProfile * | SubsurfaceProfile, for Screen Space Subsurface Scattering |  |
| LightmassSettings | FLightmassMaterialInterfaceSettings | The Lightmass settings for this object. |  |
| TextureStreamingData | TArray < FMaterialTextureInfo > | Data used by the texture streaming to know how each texture is sampled by the material. Sorted by names for quick access. |  |

## Functions

### GetBaseMaterial

Walks up parent chain and finds the base Material that this is an instance of. Just calls the virtual GetMaterial()

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API UMaterial * |  |  |

### GetPhysicalMaterial

Return a pointer to the physical material used by this material instance.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPhysicalMaterial * | The physical material. |  |

### SetForceMipLevelsToBeResident

Force the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by this material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverrideForceMiplevelsToBeResident | bool  | - Whether to use (true) or ignore (false) the bForceMiplevelsToBeResidentValue parameter. |  |
| bForceMiplevelsToBeResidentValue | bool  | - true forces all mips to stream in. false lets other factors decide what to do with the mips. |  |
| ForceDuration | float  |    - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. Negative value turns it off. |  |
| CinematicTextureGroups | int32 |  - Bitfield indicating texture groups that should use extra high-resolution mips |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API virtual void  |  |  |

### SetStreamingTextureMipOffset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMipOffset | int32  |  |  |
| SizeLimited | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API virtual void  |  |  |

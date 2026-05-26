# UMeshComponent

- Symbol Type: class
- Symbol Path: Others / UMeshComponent
- Source JSON Path: class/detail/Others/UMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

MeshComponent is an abstract base for any component that is an instance of a renderable collection of triangles.
 
  @see UStaticMeshComponent
  @see USkeletalMeshComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverrideMaterials | TArray < UMaterialInterface * > | Per-Component material overrides.  These must NOT be set directly or a race condition can occur between GC and the rendering thread. |  |
| OverlayMaterial | UMaterialInterface * | Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material |  |
| IndexedOverlayMaterials | TArray < UMaterialInterface * > | Overlay materials applied to each material slot. |  |
| IndexedOverrideOutlineMaterials | TArray < UMaterialInterface * > | Override overlay outline materials applied to each material slot. |  |
| bUseIndexedOverlayMaterials | bool | Whether to use IndexedOverlayMaterials (or OverlayMaterial). |  |
| bUseOverlayMaterials | bool | Whether to render overlay materials. (Indexed or not) |  |
| OverlayMaterialMaxDrawDistance | float | The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance. |  |
| bIsEnableRetrieveDefaultMat | bool |  |  |

## Functions

### GetMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < class UMaterialInterface * > |  |  |

### GetMaterialIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMaterialSlotNames

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < FName > |  |  |

### IsMaterialSlotNameValid

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialSlotName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EnableMeshClipPlane

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClipPlane | FPlane &  |  |  |
| PlaneIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableMeshClipPlane

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlaneIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableMeshClipArc

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClipPlane | FPlane &  |  |  |
| ClipSphere | FVector4 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableMeshClipArc

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### EnableMeshClip4Planes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ClipPlanes | TArray < FPlane > &  |  |  |
| bBox | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DisableMeshClip4Planes

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetOverlayMaterial

Get the overlay material used by this instance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface * |  |  |

### SetOverlayMaterial

Change the overlay material used by this instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewOverlayMaterial | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetUseIndexedOverlayMaterials

Get UseIndexedOverlayMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetUseIndexedOverlayMaterials

Set UseIndexedOverlayMaterials

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewUseIndexedOverlayMaterials | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetUseOverlayMaterials

Get UseOverlayMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetUseOverlayMaterials

Set UseOverlayMaterials

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewUseOverlayMaterials | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetIndexedOverlayMaterials

Get IndexedOverlayMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < class UMaterialInterface * > |  |  |

### SetIndexedOverlayMaterial

Set IndexedOverlayMaterials

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32  |  |  |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOverlayMaterialMaxDrawDistance

Change the overlay material max draw distance used by this instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaxDrawDistance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetIndexedOverrideOutlineMaterials

Get IndexedOverrideOutlineMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < class UMaterialInterface * > |  |  |

### SetIndexedOverrideOutlineMaterials

Set IndexedOverrideOutlineMaterials

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32  |  |  |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PrestreamTextures

Tell the streaming system to start loading all textures with all mip-levels.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Seconds | float  |    Number of seconds to force all mip-levels to be resident |  |
| bPrioritizeCharacterTextures | bool  | Whether character textures should be prioritized for a while by the streaming system |  |
| CinematicTextureGroups | int32 |  Bitfield indicating which texture groups that use extra high-resolution mips |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScalarParameterValueOnMaterials

Material parameter setting and caching 
	 Set all occurrences of Scalar Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| ParameterValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVectorParameterValueOnMaterials

Set all occurrences of Vector Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ParameterName | FName  |  |  |
| ParameterValue | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

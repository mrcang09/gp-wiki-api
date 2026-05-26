# UDecalComponent

- Symbol Type: class
- Symbol Path: Others / UDecalComponent
- Source JSON Path: class/detail/Others/UDecalComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDecalComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

A material that is rendered onto the surface of a mesh. A kind of 'bumper sticker' for a model.
 
  @see UDecalActor

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DecalMaterial | UMaterialInterface * | Decal material. |  |
| SortOrder | int32 | Controls the order in which decal elements are rendered.  Higher values draw later (on top). <br>	  Setting many different sort orders on many different decals prevents sorting by state and can reduce performance. |  |
| FadeScreenSize | float |  |  |
| FadeStartDelay | float | Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent. |  |
| FadeDuration | float | Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game. |  |
| bDestroyOwnerAfterFade | uint8 | Automatically destroys the owning actor after fully fading out. |  |
| bDrawToTerrainVT | uint8 |  |  |
| DecalSize | FVector | Decal size in local space (does not include the component scale), technically redundant but there for convenience |  |
| bBakeWithLandscape | uint8 | Whether bake decal to the landscape flatten material |  |

## Functions

### SetDrawToTerrainVT

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DrawToTerrainVT | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFadeStartDelay

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetFadeDuration

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetFadeOut

Sets the decal's fade start time, duration and if the owning actor should be destroyed after the decal is fully faded out.
	 The default value of 0 for FadeStartDelay and FadeDuration makes the decal persistent. See DecalLifetimeOpacity material 
	 node to control the look of "fading out."

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartDelay | float  | - Time in seconds to wait before beginning to fade out the decal. |  |
| Duration | float  | - Time in second for the decal to fade out. |  |
| DestroyOwnerAfterFade | bool | - Should the owning actor automatically be destroyed after it is completely faded out. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFadeScreenSize

Set the FadeScreenSize for this decal component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFadeScreenSize | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSortOrder

Sets the sort order for the decal component. Higher values draw later (on top). This will force the decal to reattach

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDecalMaterial

setting decal material on decal component. This will force the decal to reattach

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDecalMaterial | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDecalMaterial

Accessor for decal material

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface * |  |  |

### CreateDynamicMaterialInstance

Utility to allocate a new Dynamic Material Instance, set its parent to the currently applied material, and assign it

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic * |  |  |

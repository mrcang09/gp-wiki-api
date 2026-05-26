# UPaperGroupedSpriteComponent

- Symbol Type: class
- Symbol Path: Others / UPaperGroupedSpriteComponent
- Source JSON Path: class/detail/Others/UPaperGroupedSpriteComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperGroupedSpriteComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

A component that handles rendering and collision for many instances of one or more UPaperSprite assets.
 
  @see UPrimitiveComponent, UPaperSprite

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceMaterials | TArray < UMaterialInterface * > | Array of materials used by the instances |  |
| PerInstanceSpriteData | TArray < FSpriteInstanceData > | Array of instances |  |

## Functions

### AddInstance

Add an instance to this component. Transform can be given either in the local space of this component or world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Transform | FTransform &  |  |  |
| Sprite | UPaperSprite *  |  |  |
| bWorldSpace | bool  |  |  |
| Color | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetInstanceTransform

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32  |  |  |
| OutInstanceTransform | FTransform &  |  |  |
| bWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UpdateInstanceTransform

Update the transform for the instance specified. Instance is given in local space of this component unless bWorldSpace is set.  Returns True on success.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32  |  |  |
| NewInstanceTransform | FTransform &  |  |  |
| bWorldSpace | bool  |  |  |
| bMarkRenderStateDirty | bool  |  |  |
| bTeleport | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### UpdateInstanceColor

Update the color for the instance specified. Returns True on success.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32  |  |  |
| NewInstanceColor | FLinearColor  |  |  |
| bMarkRenderStateDirty | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RemoveInstance

Remove the instance specified. Returns True on success.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClearInstances

Clear all instances being rendered by this component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetInstanceCount

Get the number of instances in this component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SortInstancesAlongAxis

Sort all instances by their world space position along the specified axis

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldSpaceSortAxis | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# UCustomInstancedStaticMeshComponent

- Symbol Type: class
- Symbol Path: Others / UCustomInstancedStaticMeshComponent
- Source JSON Path: class/detail/Others/UCustomInstancedStaticMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCustomInstancedStaticMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

A custom component that efficiently renders multiple instances of the same StaticMesh.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseCustomBounds | bool |  |  |
| PerInstanceSMData | TArray < FInstancedStaticMeshInstanceData > | Array of instances, bulk serialized. |  |
| PerInstanceSMCustomData | TArray < FVector4 > | Array of custom data for instances. This will contains NumCustomDataFloatsInstanceCount entries. The entries are represented sequantially, in instance order. Can be read in a material and manipulated through Blueprints.<br>	 	Example: If NumCustomDataFloats is 1, then each entry will belong to an instance. Custom data 0 will belong to Instance 0. Custom data 1 will belong to Instance 1 etc.<br>	 	Example: If NumCustomDataFloats is 2, then each pair of sequential entries belong to an instance. Custom data 0 and 1 will belong to Instance 0. Custom data 2 and 3 will belong to Instance 2 etc. |  |
| PerInstanceSMCustomDataAdd | TArray < FVector4 > |  |  |
| InstancingRandomSeed | int32 | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |  |
| InstanceStartCullDistance | int32 | Distance from camera at which each instance begins to fade out. |  |
| InstanceEndCullDistance | int32 | Distance from camera at which each instance completely fades out. |  |
| InstanceNearCullDistance | int32 | Distance from camera at which each instance. |  |
| InstanceReorderTable | TArray < int32 > | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |  |
| RemovedInstances | TArray < int32 > |  |  |
| InstanceVisibilityMapping | TMap < int32 , FInstanceVisibilityData > |  |  |
| UseDynamicInstanceBuffer | bool | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |  |
| KeepInstanceBufferCPUAccess | bool | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |  |
| PhysicsSerializer | UPhysicsSerializer * | Serialization of all the InstanceBodies. Helps speed up physics creation time. |  |
| StashInstanceTransform | TMap < int32 , FMatrix > |  |  |
| NumPendingLightmaps | int32 | Number of pending lightmaps still to be calculated (Apply()'d). |  |

## Functions

### AddInstance

Add an instance to this component. Transform is given in local space of this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceTransform | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### AddInstanceWorldSpace

Add an instance to this component. Transform is given in world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldTransform | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### SetCustomDataValue

Update custom data for specific instance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32  |  |  |
| CustomDataValue | FVector4  |  |  |
| CustomDataAddValue | FVector4  |  |  |
| bMarkRenderStateDirty | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

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

Update the transform for the instance specified.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32  |  The index of the instance to update |  |
| NewInstanceTransform | FTransform &  | The new transform |  |
| bWorldSpace | bool  |  If true, the new transform interpreted as a World Space transform, otherwise it is interpreted as Local Space |  |
| bMarkRenderStateDirty | bool  | If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance. |  |
| bTeleport | bool |  Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 					True on success. |  |

### BatchUpdateInstancesData

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartInstanceIndex | int32  |  |  |
| NumInstances | int32  |  |  |
| StartCustomData | TArray < FVector4 > &  |  |  |
| StartCustomDataAdd | TArray < FVector4 > &  |  |  |
| bMarkRenderStateDirty | bool  |  |  |
| bTeleport | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RemoveInstance

Remove the instance specified. Returns True on success. Note that this will leave the array in order, but may shrink it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClearInstances

Clear all instances being rendered by this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetInstanceCount

Get the number of instances in this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetCullDistances

Sets the fading start and culling end distances for this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StartCullDistance | int32  |  |  |
| EndCullDistance | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNearCullDistance

Sets the cull near distance for this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CullDistance | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInstancesOverlappingSphere

Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Center | FVector &  |  |  |
| Radius | float  |  |  |
| bSphereInWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < int32 >  |  |  |

### GetInstancesOverlappingBox

Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Box | FBox &  |  |  |
| bBoxInWorldSpace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < int32 >  |  |  |

### HideInstance

Update the transform for the instance specified.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndices | TArray < int32 > &  |  |  |
| bForceLocalLocation | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 					True on success. |  |

### ShowInstance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceIndices | TArray < int32 > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

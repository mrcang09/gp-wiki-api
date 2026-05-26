# UInstancedStaticMeshComponent

- Symbol Type: class
- Symbol Path: Others / UInstancedStaticMeshComponent
- Source JSON Path: class/detail/Others/UInstancedStaticMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInstancedStaticMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

A component that efficiently renders multiple instances of the same StaticMesh.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PerInstanceSMData | TArray < FInstancedStaticMeshInstanceData > | Array of instances, bulk serialized. |  |
| InstancingRandomSeed | int32 | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |  |
| InstanceStartCullDistance | int32 | Distance from camera at which each instance begins to fade out. |  |
| InstanceEndCullDistance | int32 | Distance from camera at which each instance completely fades out. |  |
| InstanceNearCullDistance | int32 | Distance from camera at which each instance. |  |
| bIsFlyType | bool |  |  |
| bIsFoliage | bool |  |  |
| bIsPCFoliage | bool |  |  |
| InstanceReorderTable | TArray < int32 > | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |  |
| RemovedInstances | TArray < int32 > |  |  |
| InstanceVisibilityMapping | TMap < int32 , FInstanceVisibilityData > |  |  |
| UseDynamicInstanceBuffer | bool | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |  |
| KeepInstanceBufferCPUAccess | bool | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |  |
| DynamicInstancingParametersValue | TArray < FVector4 > |  |  |
| PerInstanceDynamicInstancingParameterCount | int32 | PerInstanceDynamicInstancingParameterCount |  |
| PhysicsSerializer | UPhysicsSerializer * | Serialization of all the InstanceBodies. Helps speed up physics creation time. |  |
| StashInstanceTransform | TMap < int32 , FMatrix > |  |  |
| NumPendingLightmaps | int32 | Number of pending lightmaps still to be calculated (Apply()'d). |  |
| CachedMappings | TArray < FInstancedStaticMeshMappingInfo > | The mappings for all the instances of this component. |  |

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
| InstanceIndices | TArray < int32 > & |  |  |

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

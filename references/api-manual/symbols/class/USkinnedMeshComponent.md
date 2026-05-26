# USkinnedMeshComponent

- Symbol Type: class
- Symbol Path: Others / USkinnedMeshComponent
- Source JSON Path: class/detail/Others/USkinnedMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USkinnedMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SkeletalMesh | USkeletalMesh * | The skeletal mesh used by this component. |  |
| MasterPoseComponent | TWeakObjectPtr < USkinnedMeshComponent > | If set, this SkeletalMeshComponent will not use its SpaceBase for bone transform, but will<br>	 	use the component space transforms from the MasterPoseComponent. This is used when constructing a character using multiple skeletal meshes sharing the same<br>	 	skeleton within the same Actor. |  |
| ComponentSpaceBoneExtraTransform | TArray < FTransform > |  |  |
| bUseBoundsFromMasterPoseComponent | uint32 | When true, we will just using the bounds from our MasterPoseComponent.  This is useful for when we have a Mesh Parented<br>	  to the main SkelMesh (e.g. outline mesh or a full body overdraw effect that is toggled) that is always going to be the same<br>	  bounds as parent.  We want to do no calculations in that case. |  |
| PhysicsAssetOverride | UPhysicsAsset * | PhysicsAsset is set in SkeletalMesh by default, but you can override with this value |  |
| bOverrideMinLod | uint8 | Whether we should use the min lod specified in MinLodModel for this component instead of the min lod in the mesh |  |
| ForcedLodModel | int32 | If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1). |  |
| MinLodModel | int32 | This is the min LOD that this component will use.  (e.g. if set to 2 then only 2+ LOD Models will be used.) This is useful to set on<br>	  meshes which are known to be a certain distance away and still want to have better LODs when zoomed in on them. |  |
| MaxLodModel | int32 |  |  |
| LODDynamicMask | TArray < bool > |  |  |
| LODInfo | TArray < struct FSkelMeshComponentLODInfo > | LOD array info. Each index will correspond to the LOD index |  |
| StreamingDistanceMultiplier | float | Allows adjusting the desired streaming distance of streaming textures that uses UV 0.<br>	  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.<br>	  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).<br>	  Value can be < 0 (from legcay content, or code changes) |  |
| WireframeColor | FColor | Wireframe color |  |
| bForceWireframe | uint32 | Forces the mesh to draw in wireframe mode. |  |
| bDisplayBones_DEPRECATED | uint32 | Draw the skeleton hierarchy for this skel mesh. |  |
| bDisableMorphTarget | uint32 | Disable Morphtarget for this component. |  |
| bHideSkin | uint32 | Don't bother rendering the skin. |  |
| bPerBoneMotionBlur | uint32 | If true, use per-bone motion blur on this skeletal mesh (requires additional rendering, can be disabled to save performance). |  |
| UpdateBoundsRate | uint8 |  |  |
| bComponentUseFixedSkelBounds | uint32 | When true, skip using the physics asset etc. and always use the fixed bounds defined in the SkeletalMesh. |  |
| bConsiderAllBodiesForBounds | uint32 | If true, when updating bounds from a PhysicsAsset, consider _all_ BodySetups, not just those flagged with bConsiderForBounds. |  |
| bFixCachedLocalBoundsIssue | uint32 | If true, cache correct local bounds. Otherwise cache a bounds transformed twice. See USkeletalMeshComponent::CalcBounds() --lyonarzhang |  |
| MeshComponentUpdateFlag | TEnumAsByte < EMeshComponentUpdateFlag :: Type > | This is update frequency flag even when our Owner has not been rendered recently |  |
| NeedUpdateEveryFrame | bool |  |  |
| NeedRateTickWhenNoRender | bool |  |  |
| bIndirectLightingCachePositionUsingActorPosition | uint32 | If true, IndirectLightingCache will use actor postion to sample |  |
| bForceMeshObjectUpdate | uint32 | If true, UpdateTransform will always result in a call to MeshObject->Update. |  |
| bCanHighlightSelectedSections | uint32 | Whether or not we can highlight selected sections - this should really only be done in the editor |  |
| bRecentlyRendered | uint32 | true if mesh has been recently rendered, false otherwise |  |
| CustomSortAlternateIndexMode | uint8 | Editor only. Used for manually selecting the alternate indices for<br>	   TRISORT_CustomLeftRight sections. |  |
| bCastCapsuleDirectShadow | uint32 | Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for direct shadowing from lights.<br>	  This type of shadowing is approximate but handles extremely wide area shadowing well.  The softness of the shadow depends on the light's LightSourceAngle  SourceRadius.<br>	  This flag will force bCastInsetShadow to be enabled. |  |
| bCastCapsuleIndirectShadow | uint32 | Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for shadowing indirect lighting (from lightmaps or skylight). |  |
| CapsuleIndirectShadowMinVisibility | float | Controls how dark the capsule indirect shadow can be. |  |
| bCPUSkinning | uint32 | Whether or not to CPU skin this component, requires render data refresh after changing |  |
| CachedLocalBounds | FBoxSphereBounds | LocalBounds cached, so they're computed just once. |  |
| bCachedLocalBoundsUpToDate | bool | true when CachedLocalBounds is up to date. |  |
| bEnableUpdateRateOptimizations | bool | if TRUE, Owner will determine how often animation will be updated and evaluated. See AnimUpdateRateTick()<br>	  This allows to skip frames for performance. (For example based on visibility and size on screen). |  |
| bDisplayDebugUpdateRateOptimizations | bool | Enable on screen debugging of update rate optimization.<br>	  Red = Skipping 0 frames, Green = skipping 1 frame, Blue = skipping 2 frames, black = skipping more than 2 frames.<br>	  @todo: turn this into a console command. |  |
| bRenderStatic | uint8 | If true, render as static in reference pose. |  |
| bUseBoneVisibilityPropagateFeature | bool | Engine modify Start +++++++++ |  |
| bOverrideAnimUpdateRateParameters | bool |  |  |
| bOverrideAnimUpdateRateParameters_ByComponent | bool |  |  |
| bRunWithOverrideAnimUpdateRateParameters | bool |  |  |
| CustomAnimUpdateRateParams | FAnimUpdateRateParameters |  |  |

## Functions

### SetPhysicsAsset

Override the Physics Asset of the mesh. It uses SkeletalMesh.PhysicsAsset, but if you'd like to override use this function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPhysicsAsset | UPhysicsAsset *  | New PhysicsAsset |  |
| bForceReInit | bool | Force reinitialize |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNumLODs

Get the number of LODs on this component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetMinLOD

Set MinLodModel of the mesh component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewMinLOD | int32 | Set new MinLodModel that make sure the LOD does not go below of this value. Range from [0, Max Number of LOD - 1]. This will affect in the next tick update. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetForcedLOD

Set MinLodModel of the mesh component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InNewForcedLOD | int32 | Set new ForcedLODModel that forces to set the incoming LOD. Range from [1, Max Number of LOD]. This will affect in the next tick update. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCastCapsuleDirectShadow

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCastCapsuleIndirectShadow

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCapsuleIndirectShadowMinVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNumBones

Returns the number of bones in the skeleton.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetBoneIndex

Find the index of bone by name. Looks in the current SkeletalMesh being used by this SkeletalMeshComponent.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName | Name of bone to look up |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | Index of the named bone in the current SkeletalMesh. Will return INDEX_NONE if bone not found. |  |

### GetBoneName

Get Bone Name from index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneIndex | int32 | Index of the bone |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | the name of the bone at the specified index |  |

### GetSocketBoneName

Returns bone name linked to a given named socket on the skeletal mesh component.
	  If you're unsure to deal with sockets or bones names, you can use this function to filter through, and always return the bone name.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSocketName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | bone name |  |

### SetSkeletalMesh

Change the SkeletalMesh that is rendered for this Component. Will re-initialize the animation tree etc.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMesh | USkeletalMesh *  | New mesh to set for this component |  |
| bReinitPose | bool  | Whether we should keep current pose or reinitialize. |  |
| bCheckBoneMap | bool  |  |  |
| bTickAnimationNow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetSkeletalMesh

Return SkeletalMesh.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USkeletalMesh * |  |  |

### GetParentBone

Get Parent Bone of the input bone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName | Name of the bone |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | the name of the parent bone for the specified bone. Returns 'None' if the bone does not exist or it is the root bone |  |

### ClearBoneExtraOffset

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OffsetBoneExtraOffsprings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputBoneName | FName  |  |  |
| InputTranslation | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RotateBoneExtraOffsprings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputBoneName | FName  |  |  |
| InputRotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### ScaleBoneExtraOffsprings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputBoneName | FName  |  |  |
| InputScale | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### SetVertexColorOverride_LinearColor

Allow override of vertex colors on a per-component basis, taking array of Blueprint-friendly LinearColors.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32  |  |  |
| VertexColors | TArray < FLinearColor > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearVertexColorOverride

Clear any applied vertex color override

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSkinWeightOverride

Allow override of skin weights on a per-component basis.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32  |  |  |
| SkinWeights | TArray < FSkelMeshSkinWeightInfo > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearSkinWeightOverride

Clear any applied skin weight override

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSkinWeightProfile

Setup an override Skin Weight Profile for this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InProfileName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClearSkinWeightProfile

Clear the Skin Weight Profile from this component, in case it is set

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UpdateSkinWeightForRemapping

Update Skin weight for remapping skeleton

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WeightInfo | FSkinWeightInfoForFPP |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnloadSkinWeightProfile

Unload a Skin Weight Profile's skin weight buffer (if created)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InProfileName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HasSkinweightProfileByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InProfileName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetCurrentSkinWeightProfileName

Return the name of the Skin Weight Profile that is currently set otherwise returns 'None'

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName |  |  |

### IsUsingSkinWeightProfile

Check whether or not a Skin Weight Profile is currently set

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SwitchToOverrideSkinWeights

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InvalidateCachedBounds

Invalidate Cached Bounds, when Mesh Component has been updated.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RefreshUpdateRateParams

Recreates update rate params and internal tracker data

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RefreshUpdateRateParamsEnsureTrackerOrder

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMasterPoseComponent

Set MasterPoseComponent for this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMasterBoneComponent | USkinnedMeshComponent *  | New MasterPoseComponent |  |
| bForceUpdate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveMasterPoseComponent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### TryRemoveDirtySlaveComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DirtySlaveMeshComponent | USkinnedMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoneTransform

Get Bone Transform from index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneIndex | int32 | Index of the bone |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  | the transform of the bone at the specified index |  |

### GetBoneLocation

Get Bone Location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  | Name of the bone |  |
| Space | EBoneSpaces :: Type | 0 == World, 1 == Local (Component) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | Vector of the bone |  |

### BoneIsChildOf

Tests if BoneName is child of (or equal to) ParentBoneName.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  | Name of the bone |  |
| ParentBoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if child (strictly, not same). false otherwise |  |

### TransformToBoneSpace

Transform a locationrotation from world space to bone relative space.
	 	This is handy if you know the location in world space for a bone attachment, as AttachComponent takes locationrotation in bone-relative space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  | Name of bone |  |
| InPosition | FVector  | Input position |  |
| InRotation | FRotator  | Input rotation |  |
| OutPosition | FVector &  | (out) Transformed position |  |
| OutRotation | FRotator & | (out) Transformed rotation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### TransformFromBoneSpace

Transform a locationrotation in bone relative space to world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  | Name of bone |  |
| InPosition | FVector  | Input position |  |
| InRotation | FRotator  | Input rotation |  |
| OutPosition | FVector &  | (out) Transformed position |  |
| OutRotation | FRotator & | (out) Transformed rotation |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FindClosestBone_K2

finds the closest bone to the given location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TestLocation | FVector  | the location to test against |  |
| BoneLocation | FVector &  | (optional, out) if specified, set to the world space location of the bone that was found, or (0,0,0) if no bone was found |  |
| IgnoreScale | float  | (optional) if specified, only bones with scaling larger than the specified factor are considered |  |
| bRequirePhysicsAsset | bool | (optional) if true, only bones with physics will be considered |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  | the name of the bone that was found, or 'None' if no bone was found |  |

### HideBoneByName

Hides the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
	 	Compoared to HideBone By Index - This keeps track of list of bones and update when LOD changes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |      Name of bone to hide |  |
| PhysBodyOption | EPhysBodyOp | Option for physics bodies that attach to the bones to be hidden |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnHideBoneByName

UnHide the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
	 	Compoared to HideBone By Index - This keeps track of list of bones and update when LOD changes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |      Name of bone to unhide |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBoneHiddenByName

Determines if the specified bone is hidden.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |      Name of bone to check |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if hidden |  |

### PropagateBoneHidden

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneIndex | int32  |  |  |
| PhysBodyOption | EPhysBodyOp |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PropagateBoneUnHidden

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FollowBoneHidden

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InHiddenLeaderComp | USkinnedMeshComponent *  |  |  |
| BoneName | FName  |  |  |
| PhysBodyOption | EPhysBodyOp |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FollowBoneUnHidden

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InUnHiddenLeaderComp | USkinnedMeshComponent *  |  |  |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableMeshClipPlane

Engine modify End -----------

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

Num of ClipPlanes is 4
	  0: Top Plane
	  1: Down Plane
	  2: Left Plane
	  3: Right Plane

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

### SetRenderStatic

Set whether this skinned mesh should be rendered as static mesh in a reference pose

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsSectionBatched

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LODIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

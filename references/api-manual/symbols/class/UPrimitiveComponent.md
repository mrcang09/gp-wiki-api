# UPrimitiveComponent

- Symbol Type: class
- Symbol Path: Others / UPrimitiveComponent
- Source JSON Path: class/detail/Others/UPrimitiveComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPrimitiveComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

PrimitiveComponents are SceneComponents that contain or generate some sort of geometry, generally to be rendered or used as collision data.
  There are several subclasses for the various types of geometry, but the most common by far are the ShapeComponents (Capsule, Sphere, Box), StaticMeshComponent, and SkeletalMeshComponent.
  ShapeComponents generate geometry that is used for collision detection but are not rendered, while StaticMeshComponents and SkeletalMeshComponents contain pre-built geometry that is rendered, but can also be used for collision detection.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ExpectedQualityLimit | FExpectedQuality | If limit > actual, primitive won't be rendered. |  |
| bFixedLODDistanceFactorSwitch | uint8 | open this switch to use r.LOD.FixedDistanceFactor to control lod switch<br>	 for example r.LOD.FixedDistanceFactor=0.5 is half distance of origin to switch new lod |  |
| CullingScreenSize | float | If the screen percentage of the bounding box under this value, it will be culled.<br>	 Set "0" to avoid contribution culling |  |
| MinDrawDistance | float | The minimum distance at which the primitive should be rendered,<br>	  measured in world space units from the center of the primitive's bounding sphere to the camera position. |  |
| LDMaxDrawDistance | float | Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object. |  |
| CachedMaxDrawDistance | float | The distance to cull this primitive at.<br>	  A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance. |  |
| DepthPriorityGroup | TEnumAsByte < enum ESceneDepthPriorityGroup > | The scene depth priority group to draw the primitive in. |  |
| ViewOwnerDepthPriorityGroup | TEnumAsByte < enum ESceneDepthPriorityGroup > | The scene depth priority group to draw the primitive in, if it's being viewed by its owner. |  |
| LightmapType | ELightmapType | Controls the type of lightmap used for this component. |  |
| VLMOptimizeType | EVLMOptimizeType | To optimize performance, VLM can select optimization method. |  |
| bInstanceCulling | uint8 |  |  |
| OverrideQueryMobilityType | EOverrideQueryMobilityType |  |  |
| bUseAsPVSOC | uint8 |  |  |
| bUseDynamicPVS | uint8 |  |  |
| FramePredictionCacheState | EFPCacheState |  |  |
| StaticSceneCacheState | EFPCacheState |  |  |
| bRenderToTerrainVirtualTexture | uint8 | This primitive will be rendered to terrain VT if true |  |
| bForceInjectToHierarchicalSurfel | uint8 | ------------------------------------Surfel GI Begin------------------------------------<br>	 If true, the primitive intersecting with the surfel volume will be injected into the volume whenever the camera moves. |  |
| bForceUseStaticMovability | uint8 | If true, the movability of the primitive will be considered as static in Surfel GI pipeline. |  |
| bAffectSurfelGIWhenHidden | uint8 | If true, always affect global illumination even if hidden in game |  |
| bBulletCanBreakThrough | uint8 | 子弹碰撞穿透 |  |
| bAlwaysCreatePhysicsState | uint8 | Indicates if we'd like to create physics state all the time (for collision and simulation).<br>	  If you set this to false, it still will create physics state if collision or simulation activated.<br>	  This can help performance if you'd like to avoid overhead of creating physics state when triggers |  |
| bGenerateOverlapEvents | uint8 | If true, this component will generate overlap events when it is overlapping other components (eg Begin Overlap).<br>	  Both components (this and the other) must have this enabled for overlap events to occur.<br>	 <br>	  @see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap() |  |
| bUpdateOverlapEventsWhenMove | uint8 |  |  |
| bForceUpdateOverlapEventsWhenMove | uint8 |  |  |
| bUseSingleSweep | uint8 | Use Sweep or single trace |  |
| bMultiBodyOverlap | uint8 | If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will<br>	  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another componentbody. This flag has no<br>	  influence on single body components. |  |
| bCheckAsyncSceneOnMove | uint8 | If true, this component will look for collisions on both physic scenes during movement.<br>	  Only required if the asynchronous physics scene is enabled and has geometry in it, and you wish to test for collisions with objects in that scene.<br>	  @see MoveComponent() |  |
| bTraceComplexOnMove | uint8 | If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).<br>	  If false, collision will be resolved against simple collision bounds instead.<br>	  @see MoveComponent() |  |
| bReturnMaterialOnMove | uint8 | If true, component sweeps will return the material in their hit result.<br>	  @see MoveComponent(), FHitResult |  |
| bUseViewOwnerDepthPriorityGroup | uint8 | True if the primitive should be rendered using ViewOwnerDepthPriorityGroup if viewed by its owner. |  |
| bAllowCullDistanceVolume | uint8 | Whether to accept cull distance volumes to modify cached cull distance. |  |
| bHasMotionBlurVelocityMeshes | uint8 | true if the primitive has motion blur velocity meshes |  |
| bVisibleInReflectionCaptures | uint8 | If true, this component will be visible in reflection captures. |  |
| bRejectReflectionCapture | uint8 | If true, this component won't be affected by any reflection capture. |  |
| bRenderInMainPass | uint8 | If true, this component will be rendered in the main pass (z prepass, basepass, transparency) |  |
| bForceRenderInShadowPass | uint8 | If true, this component will force be rendered in the shadow depth pass when bRenderInMainPass is false |  |
| HiddenInMainPassLocks | TArray < FName > | If Num() == 0, this component will be rendered in the main pass (z prepass, basepass, transparency) |  |
| bRenderInMono | uint8 | If true, this component will be rendered in mono only if an HMD is connected and monoscopic far field rendering is activated. |  |
| bReceivesDecals | uint8 | Whether the primitive receives decals. |  |
| bOwnerNoSee | uint8 | If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly. |  |
| bOnlyOwnerSee | uint8 | If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly. |  |
| bTreatAsBackgroundForOcclusion | uint8 | Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc. |  |
| bDrawIdeaOutline | uint8 | Whether to render the primitive's outline |  |
| bIdeaOutlineUseNormalInVertexColor | uint8 | Whether to use normal vector stored in vertex color |  |
| bIdeaOutlineUseOutlineMesh | uint8 |  |  |
| bIdeaOutlineNew | uint8 | Should only be used in UGC and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it. <br>	 Whether to use new outline pass. |  |
| bIdeaOutlineOcclusionHighlight | uint8 | Whether to use occlusion highlight |  |
| bDisableWriteDepthForOcclusionHighlight | uint8 | Whether to occlude other primitive's highlight. if this is already occlude highlight, it won't write depth and this flag make no use. |  |
| bIdeaOutlineNewUseBackFace | uint8 | use backface for outline drawing in outline pass |  |
| bIdeaOverrideOutlineAndOcclusion | uint8 | Override outline settings to enable both outline and occlusion |  |
| bDrawIdeaOutlineInHighlightPass | uint8 | Move old draw outline to highlight pass, not work for outline for separate pass, maybe custom depth outline in the future |  |
| IdeaOutlineOcclusionColor | FLinearColor | Edit it when enable Use Both Outline And Occlusion, otherwise use IdeaOutlineColor |  |
| bOverrideIdeaOutlineColor | uint8 | Whether to override the primitive's outline color |  |
| bOverrideIdeaOutlineThickness | uint8 | Whether to override the primitive's outline color |  |
| IdeaOutlineThickness | float | the primitive's override outline color |  |
| IdeaOutlineColor | FLinearColor | the primitive's override outline color |  |
| bDrawHighlight | uint8 | Whether to draw highlight for this primitive |  |
| bHighlightCanBeOccluded | uint8 | Whether the highlight mesh of this primitive can be occluded |  |
| bOverrideHighlightColor | uint8 | Whether to use HighlightColor for highlight rendering, if false, use the default color in HighlightMaterial |  |
| HighlightColor | FLinearColor | If bOverrideHighlightColor is true, use this color for highlight rendering |  |
| DrawDyeingMode | EDrawDyeingMode | Draw dyeing mode of primitive |  |
| VisibleDyeingColor | FLinearColor | Primitive's visible color when dyeing |  |
| OccludedDyeingColor | FLinearColor | Primitive's occlued color when dyeing |  |
| bDrawDyeing | uint8 | Whether to dyeing the primitive |  |
| bUseAsEarlyZ | uint8 | Whether to render the primitive in the early z pass for mobile platform. |  |
| bRenderInTwoPass | uint8 | Whether to render the primitive in the early z pass for mobile platform.   <br>	 If the mesh is visibility grid's proxy  <br>	 Whether to render the primitive in two pass - only work on masked hair model |  |
| bTwoPassTranslucent | uint8 | Whether to render translucency in two pass. |  |
| bTranslucentDepthWrite | uint8 | Whether to write depth for translucency. |  |
| bTranslucentDepthWriteInTwoPass | uint8 | Write depth for translucency in two pass. Add a depth-only pass before rendering the translucent object. |  |
| bForceIBL | uint8 | (TAPD:ID869829499) for SceneProxyIBL |  |
| bForceDisableIBL | uint8 |  |  |
| bForceDynamic | uint8 |  |  |
| ActiveScopeStatus | int32 |  |  |
| ScopeLocalTranslation | FVector |  |  |
| ScopeLocalRotation | FRotator |  |  |
| ScopeRadius | float |  |  |
| bIsFppLayer | uint8 |  |  |
| bIsTppLayer | uint8 | When enabled, the component will NOT cast a shadow on components with bIsFppLayer enabled.<br>	  This requires bCastInsetShadow to be enabled. |  |
| bUseAsOccluder | uint8 | Whether to render the primitive in the depth only pass.<br>	  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.<br>	  @todo - if any rendering features rely on a complete depth only pass, this variable needs to go away. |  |
| bOnlyAsOccluder | uint8 |  |  |
| bSelectable | uint8 | If this is True, this component can be selected in the editor. |  |
| bForceMipStreaming | uint8 | If true, forces mips for textures used by this component to be resident when this component's level is loaded. |  |
| bHasPerInstanceHitProxies | uint8 | If true a hit-proxy will be generated for each instance of instanced static meshes |  |
| bRecieveShadow | uint8 | Controls whether the primitive component should recieve a shadow or not.(by jinglei) |  |
| CastShadow | uint8 | Controls whether the primitive component should cast a shadow or not.<br>	 <br>	  This flag is ignored (no shadows will be generated) if all materials on this component have an Unlit shading model. |  |
| bAffectDynamicIndirectLighting | uint8 | Controls whether the primitive should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true. |  |
| bAffectDistanceFieldLighting | uint8 | Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. |  |
| bCastDynamicShadow | uint8 | Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. |  |
| bCastStaticShadow | uint8 | Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true. |  |
| bCastVolumetricTranslucentShadow | uint8 | Whether the object should cast a volumetric translucent shadow.<br>	  Volumetric translucent shadows are useful for primitives `with smoothly changing opacity like particles representing a volume,<br>	  But have artifacts when used on highly opaque surfaces. |  |
| bSelfShadowOnly | uint8 | When enabled, the component will only cast a shadow on itself and not other components in the world.<br>	  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled. |  |
| bCastFarShadow | uint8 | When enabled, the component will be rendering into the far shadow cascades (only for directional lights). |  |
| bCastInDoorShadow | uint8 | When enabled, the component will be rendering shadow in door (only for directional lights). |  |
| bCastInsetShadow | uint8 | Whether this component should create a per-object shadow that gives higher effective shadow resolution.<br>	  Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled. |  |
| bCastTranslucentShadowAsMask | uint8 |  |  |
| bCastPhotonShadow | uint8 | #if WITH_PHOTON_SHADOW |  |
| bCastPhotonPerObjectShadow | uint8 | #if WITH_PHOTON_PER_OBEJCT_SHADOW |  |
| bNearCascade | uint8 |  |  |
| bCastCinematicShadow | uint8 | Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.<br>	  This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired. |  |
| bCastHiddenShadow | uint8 | If true, the primitive will cast shadows even if bHidden is true.<br>	 	Controls whether the primitive should cast shadows when hidden.<br>	 	This flag is only used if CastShadow is true. |  |
| bCastShadowAsTwoSided | uint8 | Whether this primitive should cast dynamic shadows as if it were a two sided material. |  |
| bLightAsIfStatic_DEPRECATED | uint8 |  |  |
| bLightAttachmentsAsGroup | uint8 | Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.<br>	  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.<br>	  This is useful for improving performance when multiple movable components are attached together. |  |
| bReceiveCombinedCSMAndStaticShadowsFromStationaryLights | uint8 | Mobile only:<br>	  If enabled this component can receive combined static and CSM shadows from a stationary light. (Enabling will increase shading cost.)<br>	  If disabled this component will only receive static shadows from stationary lights. |  |
| bReceiveLandscapeShadows | uint8 |  |  |
| bSingleSampleShadowFromStationaryLights | uint8 | Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.<br>	  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.<br>	  This is currently only used on stationary directional lights. |  |
| bIgnoreRadialImpulse | uint8 | Will ignore radial impulses applied to this component. |  |
| bIgnoreRadialForce | uint8 | Will ignore radial forces applied to this component. |  |
| bApplyImpulseOnDamage | uint8 | True for damage to this component to apply physics impulse, false to opt out of these impulses. |  |
| bReplicatePhysicsToAutonomousProxy | uint8 | True if physics should be replicated to autonomous proxies. This should be true for<br>		server-authoritative simulations, and false for client authoritative simulations. |  |
| bCorrectPXTrans | uint8 |  |  |
| bCorrectPXTransUsingRemovePhysTargetFunction | uint8 |  |  |
| AlwaysLoadOnClient | uint8 | If this is True, this component must always be loaded on clients, even if Hidden and CollisionEnabled is NoCollision. |  |
| AlwaysLoadOnServer | uint8 | If this is True, this component must always be loaded on servers, even if Hidden and CollisionEnabled is NoCollision |  |
| bUseEditorCompositing | uint8 | Composite the drawing of this component onto the scene after post processing (only applies to editor drawing) |  |
| bRenderCustomDepth | uint8 | If true, this component will be rendered in the CustomDepth pass (usually used for outlines) |  |
| bUpdateTransformUseTeleportPhysics | uint8 |  |  |
| bUseAsyncCompilePSO | uint8 | #if WITH_ANDROID_ASYNC_COMPILE_PSO<br>	 whether this mesh is using async compile pso , only used for android |  |
| bIgnoreOtherCanBeOverlap | uint8 |  |  |
| bMoveMultiPenetratingIgnoreFlag | uint8 | 是否在移动的时候，有多个渗透，就忽略开启本标志的物体 |  |
| bHasCustomNavigableGeometry | TEnumAsByte < EHasCustomNavigableGeometry :: Type > | If true then DoCustomNavigableGeometryExport will be called to collect navigable geometry of this component. |  |
| CanCharacterStepUpOn | TEnumAsByte < enum ECanBeCharacterBase > | Determine whether a Character can step up onto this component.<br>	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.<br>	  @see FWalkableSlopeOverride |  |
| JumpOffVelocityFactor | float | 不能站的时候，角色随机移动的最大速度的比率<br>	 如果>0，表示使用本值，移动组件上的值无效；否则使用移动组件上的值 |  |
| LightingChannels | FLightingChannels | Channels that this component should be in.  Lights with matching channels will affect the component.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |  |
| IndoorOutdoorMask | TEnumAsByte < EIndoorOutdoorMask > |  |  |
| CustomDepthStencilWriteMask | ERendererStencilMask | Mask used for stencil buffer writes. |  |
| CustomDepthStencilValue | int32 | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |  |
| TranslucencySortPriority | int32 | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br>	 <br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.<br>	  It is especially problematic on dynamic gameplay effects. |  |
| TerrainRVTRenderSortPriority | int32 | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |  |
| VisibilityId | int32 | Used for precomputed visibility |  |
| PVSHandlerID | int32 | Used for precomputed visibility |  |
| NumInstanceVisibilityVolumes | int32 | Used for precomputed visibility |  |
| SkyLightIntensityScale | float |  |  |
| MinSkyVisibility | float |  |  |
| bForceSyncPSO | uint32 | #if ALLOW_FORCE_SYNC_CREATE_PSO<br>	  Force this material to link PSO synchronously (on iOS).<br>	  It avoids popping when the material is not suitable for async linking but may introduce stutters.<br>	  remove for IG |  |
| OverrideCylinderMaxDrawHeight | float | Used if [r.CylinderMaxDrawHeight] is not zero, override [r.CylinderMaxDrawHeight] global setting |  |
| bCanSeparateParticleRendering | bool |  |  |
| bDisableDynamicInstancing | bool |  |  |
| BoundsScale | float | Scales the bounds of the object.<br>	  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.<br>	  Warning: Increasing the bounds of an object will reduce performance and shadow quality!<br>	  Currently only used by StaticMeshComponent and SkeletalMeshComponent. |  |
| OCBoundsScale | float |  |  |
| OCBoundsExtent | int32 | ROC Extent the bounds a few pixels during depth test. |  |
| LastSubmitTime | float | Last time the component was submitted for rendering (called FScene::AddPrimitive). |  |
| LastRenderTime | float | The value of WorldSettings->TimeSeconds for the frame when this component was last rendered.  This is written<br>	  from the render thread, which is up to a frame behind the game thread, so you should allow this time to<br>	  be at least a frame behind the game thread's world time before you consider the actor non-visible. |  |
| LastRenderTimeOnScreen | float |  |  |
| TouchAsBlockActors | TArray < AActor * > |  |  |
| MoveIgnoreComponents | TArray < UPrimitiveComponent * > | Set of components to ignore during component sweeps in MoveComponent().<br>	 These components will be ignored when this component moves or updates overlaps.<br>	 The other components may also need to be told to do the same when they move.<br>	 Does not affect movement of this component when simulating physics.<br>	 @see IgnoreComponentWhenMoving() |  |
| BodyInstance | FBodyInstance | Physics scene information for this component, holds a single rigid body with multiple shapes. |  |
| LODParentPrimitive | UPrimitiveComponent * | LOD parent primitive to draw instead of this one (multiple UPrim's will point to the same LODParent ) |  |
| PostPhysicsComponentTick | FPrimitiveComponentPostPhysicsTickFunction | Tick function for physics ticking |  |
| IndirectLightingCacheQuality | TEnumAsByte < EIndirectLightingCacheQuality > | Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time. |  |
| bGenerateSurfaceSample | uint8 |  |  |
| bOccludeLightingRay | uint8 |  |  |
| bEnableAutoLODGeneration | uint8 | If true, and if World setting has bEnableHierarchicalLOD equal to true, then this component will be included when generating a Proxy mesh for the parent Actor |  |
| bUseMaxLODAsImposter | uint8 | Use the Maximum LOD Mesh (imposter) instead of including Mesh data from this component in the Proxy Generation process |  |
| ExcludeForSpecificHLODLevels | TArray < int32 > | Which specific HLOD levels this component should be excluded from |  |
| bIsVisibilityGridProxy | uint8 | Whether to render the primitive in the early z pass for mobile platform.   <br>	 If the mesh is visibility grid's proxy |  |
| CanBeCharacterBase_DEPRECATED | TEnumAsByte < enum ECanBeCharacterBase > |  |  |
| LpvBiasMultiplier | float | Multiplier used to scale the Light Propagation Volume light injection bias, to reduce light bleeding.<br>	  Set to 0 for no bias, 1 for default or higher for increased biasing (e.g. for<br>	  thin geometry such as walls) |  |
| bCoastline | uint8 | if true, primitive will be collected as coastline |  |

## Functions

### SetLightingChannels

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bChannel0Open | bool  |  |  |
| bChannel1Open | bool  |  |  |
| bChannel2Open | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IgnoreActorWhenMoving

Tells this component whether to ignore collision with all components of a specific Actor when this component is moved.
	  Components on the other Actor may also need to be told to do the same when they move.
	  Does not affect movement of this component when simulating physics.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | AActor *  |  |  |
| bShouldIgnore | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyArrayOfMoveIgnoreActors

Returns the list of actors we currently ignore when moving.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < AActor * > |  |  |

### ClearMoveIgnoreActors

Clear the list of actors we ignore when moving.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IgnoreComponentWhenMoving

Tells this component whether to ignore collision with another component when this component is moved.
	 The other components may also need to be told to do the same when they move.
	 Does not affect movement of this component when simulating physics.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Component | UPrimitiveComponent *  |  |  |
| bShouldIgnore | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyArrayOfMoveIgnoreComponents

Returns the list of actors we currently ignore when moving.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UPrimitiveComponent * > |  |  |

### ClearMoveIgnoreComponents

Clear the list of components we ignore when moving.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsOverlappingComponent

Check whether this component is overlapping another component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherComp | UPrimitiveComponent * | Component to test this component against. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether this component is overlapping another component. |  |

### IsOverlappingActor

Check whether this component is overlapping any component of the given Actor.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Other | AActor * | Actor to test this component against. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether this component is overlapping any component of the given Actor. |  |

### GetOverlappingActors

Returns a list of actors that this component is overlapping.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OverlappingActors | TArray < AActor * > &  | [out] Returned list of overlapping actors |  |
| ClassFilter | TSubclassOf < AActor > |  [optional] If set, only returns actors of this class or subclasses |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOverlappingComponents

Returns list of components this component is overlapping.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOverlappingComponents | TArray < UPrimitiveComponent * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBoundsScale

Scale the bounds of this object, used for frustum culling. Useful for features like WorldPositionOffset.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewBoundsScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoundsScale

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetMaterial

Returns the material used by the element at the specified index

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32 | - The element to access the material of. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface *  | the material used by the indexed element of this mesh. |  |

### SetMaterial

Changes the material applied to an element of the mesh.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32  | - The element to access the material of. |  |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | the material used by the indexed element of this mesh. |  |

### SetMaterialByName

Changes the material applied to an element of the mesh.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialSlotName | FName  | - The slot name to access the material of. |  |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  | the material used by the indexed element of this mesh. |  |

### CreateAndSetMaterialInstanceDynamic

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32 | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic *  |  |  |

### CreateAndSetMaterialInstanceDynamicFromMaterial

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32  | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |  |
| Parent | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic *  |  |  |

### CreateDynamicMaterialInstance

Creates a Dynamic Material Instance for the specified element index, optionally from the supplied material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ElementIndex | int32  | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |  |
| SourceMaterial | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic *  |  |  |

### GetMaterialFromCollisionFaceIndex

Try and retrieve the material applied to a particular collision face of mesh. Used with face index returned from collision trace.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FaceIndex | int32  | Face index from hit result that was hit by a trace |  |
| SectionIndex | int32 & | Section of the mesh that the face belongs to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface *  | 				Material applied to section that the hit face belongs to |  |

### GetWalkableSlopeOverride

Returns the slope override struct for this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const struct FWalkableSlopeOverride & |  |  |

### SetWalkableSlopeOverride

Sets a new slope override for this component instance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewOverride | FWalkableSlopeOverride & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSimulatePhysics

Sets whether or not a single body should use physics simulation, or should be 'fixed' (kinematic).
	 	Note that if this component is currently attached to something, beginning simulation will detach it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bSimulate | bool | New simulation state for single body |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLockedAxis

Sets the constraint mode of the component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LockedAxis | EDOFMode :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetConstraintMode

Sets the constraint mode of the component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConstraintMode | EDOFMode :: Type | The type of constraint to use. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddImpulse

Add an impulse to a single rigid body. Good for one time instant burst.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  | Magnitude and direction of impulse to apply. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |  |
| bVelChange | bool | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddAngularImpulse

Add an angular impulse to a single rigid body. Good for one time instant burst.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  |  |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |  |
| bVelChange | bool | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddAngularImpulseInRadians

Add an angular impulse to a single rigid body. Good for one time instant burst.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  |  |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |  |
| bVelChange | bool | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddAngularImpulseInDegrees

Add an angular impulse to a single rigid body. Good for one time instant burst.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  |  |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |  |
| bVelChange | bool | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddImpulseAtLocation

Add an impulse to a single rigid body at a specific location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Impulse | FVector  | Magnitude and direction of impulse to apply. |  |
| Location | FVector  | Point in world space to apply impulse at. |  |
| BoneName | FName | If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddRadialImpulse

Add an impulse to all rigid bodies in this component, radiating out from the specified position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Origin | FVector  | Point of origin for the radial impulse blast, in world space |  |
| Radius | float  | Size of radial impulse. Beyond this distance from Origin, there will be no affect. |  |
| Strength | float  | Maximum strength of impulse applied to body. |  |
| Falloff | ERadialImpulseFalloff  | Allows you to control the strength of the impulse as a function of distance from Origin. |  |
| bVelChange | bool | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddForce

Add a force to a single rigid body.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  |  Force vector to apply. Magnitude indicates strength of force. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddForce_AssumesLocked

Add a force to a single rigid body.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.
 
 	Notice: AssumesLocked   yufeiili 未加锁版本

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  |  Force vector to apply. Magnitude indicates strength of force. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddForceAtLocation

Add a force to a single rigid body at a particular location in world space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  | Force vector to apply. Magnitude indicates strength of force. |  |
| Location | FVector  | Location to apply force, in world space. |  |
| BoneName | FName | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddForceAtLocation_AssumesLocked

Add a force to a single rigid body at a particular location in world space.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.
 
 	Notice: AssumesLocked   yufeiili 未加锁版本

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  | Force vector to apply. Magnitude indicates strength of force. |  |
| Location | FVector  | Location to apply force, in world space. |  |
| BoneName | FName | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddForceAtLocationLocal

Add a force to a single rigid body at a particular location. Both Force and Location should be in body space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Force | FVector  | Force vector to apply. Magnitude indicates strength of force. |  |
| Location | FVector  | Location to apply force, in component space. |  |
| BoneName | FName | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddRadialForce

Add a force to all bodies in this component, originating from the supplied world-space location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Origin | FVector  | Origin of force in world space. |  |
| Radius | float  | Radius within which to apply the force. |  |
| Strength | float  | Strength of force to apply. |  |
| Falloff | ERadialImpulseFalloff  | Allows you to control the strength of the force as a function of distance from Origin. |  |
| bAccelChange | bool | If true, Strength is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTorque

Add a torque to a single rigid body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Torque | FVector  | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTorqueInRadians

Add a torque to a single rigid body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Torque | FVector  | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTorqueInRadians_AssumesLocked

Add a torque to a single rigid body.
	 	assumesLocked yufeiii 未加锁版本

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Torque | FVector  | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTorqueInDegrees

Add a torque to a single rigid body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Torque | FVector  | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddTorqueInDegrees_AssumesLocked

Add a torque to a single rigid body.
	 	Notice: AssumesLocked   yufeiili 未加锁版本

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Torque | FVector  | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |  |
| BoneName | FName  | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |  |
| bAccelChange | bool | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsLinearVelocity

Set the linear velocity of a single body.
	 	This should be used cautiously - it may be better to use AddForce or AddImpulse.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewVel | FVector  |  New linear velocity to apply to physics. |  |
| bAddToCurrent | bool  | If true, NewVel is added to the existing velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPhysicsLinearVelocity

Get the linear velocity of a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsLinearVelocity_AssumesLocked

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsLinearVelocityAtPoint

Get the linear velocity of a point on a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point is specified in world space. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### SetAllPhysicsLinearVelocity

Set the linear velocity of all bodies in this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewVel | FVector  |  New linear velocity to apply to physics. |  |
| bAddToCurrent | bool | If true, NewVel is added to the existing velocity of the body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsAngularVelocity

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector  | New angular velocity to apply to body, in degrees per second. |  |
| bAddToCurrent | bool  | If true, NewAngVel is added to the existing angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsAngularVelocityInRadians

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector  | New angular velocity to apply to body, in radians per second. |  |
| bAddToCurrent | bool  | If true, NewAngVel is added to the existing angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsAngularVelocityInDegrees

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector  | New angular velocity to apply to body, in degrees per second. |  |
| bAddToCurrent | bool  | If true, NewAngVel is added to the existing angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsMaxAngularVelocity

Set the maximum angular velocity of a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMaxAngVel | float  | New maximum angular velocity to apply to body, in degrees per second. |  |
| bAddToCurrent | bool  | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsMaxAngularVelocityInDegrees

Set the maximum angular velocity of a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMaxAngVel | float  | New maximum angular velocity to apply to body, in degrees per second. |  |
| bAddToCurrent | bool  | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysicsMaxAngularVelocityInRadians

Set the maximum angular velocity of a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewMaxAngVel | float  | New maximum angular velocity to apply to body, in radians per second. |  |
| bAddToCurrent | bool  | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPhysicsAngularVelocity

Get the angular velocity of a single body, in degrees per second.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsAngularVelocity_AssumesLocked

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsAngularVelocityInDegrees

Get the angular velocity of a single body, in degrees per second.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsAngularVelocityInDegrees_AssumesLocked

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsAngularVelocityInRadians

Get the angular velocity of a single body, in radians per second.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetPhysicsAngularVelocityInRadians_AssumesLocked

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetCenterOfMass

Get the center of mass of a single body. In the case of a welded body this will return the center of mass of the entire welded body (including its parent and children)
	   Objects that are not simulated return (0,0,0) as they do not have COM

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to get center of mass of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### SetCenterOfMass

Set the center of mass of a single body. This will offset the physx-calculated center of mass.
		Note that in the case where multiple bodies are attached together, the center of mass will be set for the entire group.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CenterOfMassOffset | FVector  | User specified offset for the center of mass of this object, from the calculated location. |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### WakeRigidBody

'Wake' physics simulation for a single body.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName | If a SkeletalMeshComponent, name of body to wake. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PutRigidBodyToSleep

Force a single body back to sleep.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName | If a SkeletalMeshComponent, name of body to put to sleep. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNotifyRigidBodyCollision

Changes the value of bNotifyRigidBodyCollision

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewNotifyRigidBodyCollision | bool | - The value to assign to bNotifyRigidBodyCollision |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOwnerNoSee

Changes the value of bOwnerNoSee.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewOwnerNoSee | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOnlyOwnerSee

Changes the value of bOnlyOwnerSee.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewOnlyOwnerSee | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDrawIdeaOutline

Changes the value of DrawOutline.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewDrawOutline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineUseNormalInVertexColor

Changes whether use the new outline method which uses normal vectors in vertex colors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewUseNormalInVertexColor | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineNew

Should only be used in  and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it. 
	 Changes whether use the new outline pass.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNew | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineUseOutlineMesh

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseOutlineMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineOcclusionHighlight

Changes whether use the occlusion highlight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOcclusionHighlight | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDisableWriteDepthForOcclusionHighlight

Changes whether to occlude other primitives' highlight. if this is already occlude highlight, it won't write depth and this flag make no use.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bDisable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOverrideOutlineAndOcclusion

Override outline settings to enable both outline and occlusion

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOutlineAndOcclusion | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDrawIdeaOutlineInHighlightPass

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bHighlight | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineNewUseBackFace

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseBackFace | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OverrideIdeaOutlineColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverride | bool  |  |  |
| InOutlineColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OverrideIdeaOutlineThickness

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverride | bool  |  |  |
| InThickness | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineOcclusionColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOcclusionColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutline_UGC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bDrawOutline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIdeaOutlineOcclusionHighlight_UGC

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOcclusionHighlight | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOutlineMesh

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StaticMesh | UStaticMesh * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDrawHighlight

Turn onoff the highlight rendering for this primitive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewDrawHighlight | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHighlightCanBeOccluded

Changes whether the highlight mesh of this primitive can be occluded

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInCanBeOccluded | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OverrideHighlightColor

Override the highlight color for this primitive

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverride | bool  | - If true, override the highlight color using InHighlightColor. If false, use the default color in HighlightMaterial. |  |
| InHighlightColor | FLinearColor | - New color used for highlight rendering |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDrawDyeing

Changes the value of DrawDyeing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewDrawOutline | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDrawDyeingMode

Changes the value of DrawDyeingMode.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDrawDyeingMode | EDrawDyeingMode |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetVisibleDyeingColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOccludedDyeingColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReveiceShadow

Changes the value of bReveiceShadow.(by jinglei)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewReveiceShadow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCastShadow

Changes the value of CastShadow.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewCastShadow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCastInsetShadow

Changes the value of CastInsetShadow.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInCastInsetShadow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLightAttachmentsAsGroup

Changes the value of LightAttachmentsAsGroup.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInLightAttachmentsAsGroup | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCastPhotonShadow

WITH_PHOTON_SHADOW 
	 Set cast photon shadow.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewCastPhotonShadow | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetSingleSampleShadowFromStationaryLights

Changes the value of bSingleSampleShadowFromStationaryLights.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewSingleSampleShadowFromStationaryLights | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTranslucentSortPriority

Changes the value of TranslucentSortPriority.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTranslucentSortPriority | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetReceivesDecals

Changes the value of bReceivesDecals.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewReceivesDecals | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCollisionEnabled

Controls what kind of collision is enabled for this body

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewType | ECollisionEnabled :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCollisionProfileName

Set Collision Profile Name
	  This function is called by constructors when they set ProfileName
	  This will change current CollisionProfileName to be this, and overwrite Collision Setting

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCollisionProfileName | FName | : New Profile Name |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCollisionProfileName

Get the collision profile name

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName |  |  |

### SetCollisionObjectType

Changes the collision channel that this object uses when it moves

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Channel | ECollisionChannel |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### K2_LineTraceComponent

Perform a line trace against a single component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TraceStart | FVector  |  |  |
| TraceEnd | FVector  |  |  |
| bTraceComplex | bool  |  |  |
| bShowTrace | bool  |  |  |
| HitLocation | FVector &  |  |  |
| HitNormal | FVector &  |  |  |
| BoneName | FName &  |  |  |
| OutHit | FHitResult & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetRenderCustomDepth

Sets the bRenderCustomDepth property and marks the render state dirty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCustomDepthStencilValue

Sets the CustomDepth stencil value (0 - 255) and marks the render state dirty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCustomDepthStencilWriteMask

Sets the CustomDepth stencil write mask and marks the render state dirty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WriteMaskBit | ERendererStencilMask |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderInMainPass

Sets bRenderInMainPass property and marks the render state dirty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bValue | bool  |  |  |
| LockKey | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsRenderInMainPass

Sets bRenderInMainPass property and marks the render state dirty.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetRenderInMono

Sets bRenderInMono property and marks the render state dirty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bValue | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetForceIBL

set bForceIBL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForceIBL | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetForceDisableIBL

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForceDisableIBL | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsForceDynamic

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetForceDynamic

set bForceDynamic

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForceDynamic | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsActiveScope

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetActiveScope

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsActiveScope | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScopeInfoLocal

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLocalTranslation | FVector  |  |  |
| InLocalRotation | FRotator  |  |  |
| InScopeRadius | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFppLayer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsFppLayer | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTppLayer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsTppLayer | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTwoPassTranslucent

Changes the value of Two Pass Translucent.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewTwoPassTranslucent | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTranslucentDepthWrite

Changes the value of Translucent Depth Write.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewTranslucentDepthWrite | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetTranslucentDepthWriteInTwoPass

Changes the value of Translucent Depth Write In Two Pass.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bNewTranslucentDepthWriteInTwoPass | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetNumMaterials

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | number of material elements in this primitive |  |

### GetClosestPointOnCollision

Returns the distance and closest point to the collision surface.
	 Component must have simple collision to be queried for closest point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector &  |  World 3D vector |  |
| OutPointOnBody | FVector &  | Point on the surface of collision closest to Point |  |
| BoneName | FName |  If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 	Success if returns > 0.f, if returns 0.f, it is either not convex or inside of the point |  |

### GetCollisionEnabled

Returns the form of collision for this component

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECollisionEnabled :: Type |  |  |

### K2_IsCollisionEnabled

Utility to see if there is any form of collision (query or physics) enabled on this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### K2_IsQueryCollisionEnabled

Utility to see if there is any query collision enabled on this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### K2_IsPhysicsCollisionEnabled

Utility to see if there is any physics collision enabled on this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetCollisionResponseToChannel

Gets the response type given a specific channel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Channel | ECollisionChannel |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECollisionResponse  |  |  |

### GetCollisionObjectType

Gets the collision object type

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECollisionChannel |  |  |

### SetAllPhysicsAngularVelocity

Set the angular velocity of all bodies in this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector &  | New angular velocity to apply to physics, in degrees per second. |  |
| bAddToCurrent | bool | If true, NewAngVel is added to the existing angular velocity of all bodies. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllPhysicsAngularVelocityInDegrees

Set the angular velocity of all bodies in this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector &  | New angular velocity to apply to physics, in degrees per second. |  |
| bAddToCurrent | bool | If true, NewAngVel is added to the existing angular velocity of all bodies. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAllPhysicsAngularVelocityInRadians

Set the angular velocity of all bodies in this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAngVel | FVector &  | New angular velocity to apply to physics, in radians per second. |  |
| bAddToCurrent | bool | If true, NewAngVel is added to the existing angular velocity of all bodies. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### WakeAllRigidBodies

Ensure simulation is running for all bodies in this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetEnableGravity

Enablesdisables whether this component is affected by gravity. This applies only to components with bSimulatePhysics set to true.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bGravityEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsGravityEnabled

Returns whether this component is affected by gravity. Returns always false if the component is not simulated.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetLinearDamping

Sets the linear damping of this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDamping | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetLinearDamping

Returns the linear damping of this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetAngularDamping

Sets the angular damping of this component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDamping | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAngularDamping

Returns the angular damping of this component.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetMassScale

Change the mass scale used to calculate the mass of a single physics body

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| InMassScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetMassScale

Returns the mass scale used to calculate the mass of a single physics body

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SetAllMassScale

Change the mass scale used fo all bodies in this component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMassScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetMassOverrideInKg

Override the mass (in Kg) of a single physics body.
		Note that in the case where multiple bodies are attached together, the override mass will be set for the entire group.
		Set the Override Mass to false if you want to reset the body's mass to the auto-calculated physx mass.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| MassInKg | float  |  |  |
| bOverrideMass | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetMass

Returns the mass of this component in kg.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetInertiaTensor

Returns the inertia tensor of this component in kg cm^2. The inertia tensor is in local component space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### ScaleByMomentOfInertia

Scales the given vector by the world space moment of inertia. Useful for computing the torque needed to rotate an object.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InputVector | FVector  |  |  |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### IsAnyRigidBodyAwake

Returns if any body in this component is currently awake and simulating.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetCollisionResponseToChannel

Changes a member of the ResponseToChannels container for this PrimitiveComponent.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Channel | ECollisionChannel  |  |  |
| NewResponse | ECollisionResponse |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCollisionResponseToAllChannels

Changes all ResponseToChannels container for this PrimitiveComponent. to be NewResponse

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewResponse | ECollisionResponse |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPhysMaterialOverride

Changes the current PhysMaterialOverride for this component.
	 	Note that if physics is already running on this component, this will _not_ alter its massinertia etc,
	 	it will only change its surface properties like friction.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPhysMaterial | UPhysicalMaterial * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPhysMaterial

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Item | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPhysicalMaterial *  |  |  |

### SetCullDistance

Changes the value of CullDistance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewCullDistance | float  | - The value to assign to CullDistance. |  |
| EnableIncrease | bool | - Whether or not to increase the cull distance if it is greater than the current cull distance. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CanCharacterStepUp

Return true if the given Pawn can step up onto this component.
	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pawn | APawn * | the Pawn that wants to step onto this component. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsComponentRenderQualityEnough

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsComponentDeviceQualityEnough

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

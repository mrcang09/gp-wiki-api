# UMaterialInstance

- Symbol Type: class
- Symbol Path: Others / UMaterialInstance
- Source JSON Path: class/detail/Others/UMaterialInstance.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInstance.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshLogicType | int32 | 材质实例的功能分类：1:挂件 |  |
| PhysMaterial | UPhysicalMaterial * | Physical material to use for this graphics material. Used for sounds, effects etc. |  |
| Parent | UMaterialInterface * | Parent material. |  |
| bOverride_IncludeShaderCode | uint32 |  |  |
| bIncludeShaderCode | uint32 |  |  |
| bHasStaticPermutationResource | uint32 | Indicates whether the instance has static permutation resources (which are required when static parameters are present)<br>	  Read directly from the rendering thread, can only be modified with the use of a FMaterialUpdateContext.<br>	  When true, StaticPermutationMaterialResources will always be valid and non-null. |  |
| bOverrideSubsurfaceProfile | uint32 | Defines if SubsurfaceProfile from this instance is used or it uses the parent one. |  |
| FontParameterValues | TArray < FFontParameterValue > | Font parameters. |  |
| ScalarParameterValues | TArray < FScalarParameterValue > | Scalar parameters. |  |
| TextureParameterValues | TArray < FTextureParameterValue > | Texture parameters. |  |
| VectorParameterValues | TArray < FVectorParameterValue > | Vector parameters. |  |
| DynamicInstancingParameters | TMap < FString , FVector4 > | Dynamic instancing parameters. |  |
| bOverrideBaseProperties_DEPRECATED | bool |  |  |
| BasePropertyOverrides | FMaterialInstanceBasePropertyOverrides |  |  |
| PermutationTextureReferences | TArray < UTexture * > | Cached texture references from all expressions in the material (including nested functions).<br>	 This is used to link uniform texture expressions which were stored in the DDC with the UTextures that they reference. |  |
| bEnableTexture2DArrayShaderVariant | uint32 |  |  |
| ReferencedTextureGuids | TArray < FGuid > |  |  |

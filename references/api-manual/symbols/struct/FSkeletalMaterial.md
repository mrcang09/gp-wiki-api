# FSkeletalMaterial

- Symbol Type: struct
- Symbol Path: FSkeletalMaterial
- Source JSON Path: cppstruct/detail/FSkeletalMaterial.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSkeletalMaterial.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialInterface | UMaterialInterface * |  |  |
| bEnableShadowCasting_DEPRECATED | bool |  |  |
| bRecomputeTangent_DEPRECATED | bool |  |  |
| MaterialSlotName | FName | This name should be use by the gameplay to avoid error if the skeletal mesh Materials array topology change |  |
| UVChannelData | FMeshUVChannelInfo | Data used for texture streaming relative to each UV channels. |  |
| MaterialSoftRef | FSoftObjectPath | Soft Reference to MaterialInterface add by jingleechen |  |
| ImportedMaterialSlotName | FName | This name should be use when we re-import a skeletal mesh so we can order the Materials array like it should be |  |

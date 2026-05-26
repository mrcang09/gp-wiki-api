# FStaticMaterial

- Symbol Type: struct
- Symbol Path: FStaticMaterial
- Source JSON Path: cppstruct/detail/FStaticMaterial.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FStaticMaterial.json
- Mirrored At (UTC): 2026-05-19 08:24:48Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialInterface | UMaterialInterface * |  |  |
| MaterialSlotName | FName | This name should be use by the gameplay to avoid error if the skeletal mesh Materials array topology change |  |
| UVChannelData | FMeshUVChannelInfo | Data used for texture streaming relative to each UV channels. |  |
| MaterialSoftRef | FSoftObjectPath | Soft Reference to MaterialInterface |  |
| ImportedMaterialSlotName | FName | This name should be use when we re-import a skeletal mesh so we can order the Materials array like it should be |  |

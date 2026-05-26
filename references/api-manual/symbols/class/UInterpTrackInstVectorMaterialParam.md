# UInterpTrackInstVectorMaterialParam

- Symbol Type: class
- Symbol Path: Others / UInterpTrackInstVectorMaterialParam
- Source JSON Path: class/detail/Others/UInterpTrackInstVectorMaterialParam.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstVectorMaterialParam.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialInstances | TArray < UMaterialInstanceDynamic * > | MIDs we're using to set the desired parameter. |  |
| ResetVectors | TArray < FVector > | Saved values for restoring state when exiting Matinee. |  |
| PrimitiveMaterialRefs | TArray < struct FPrimitiveMaterialRef > | Primitive components on which materials have been overridden. |  |
| InstancedTrack | UInterpTrackVectorMaterialParam * | Track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately. |  |

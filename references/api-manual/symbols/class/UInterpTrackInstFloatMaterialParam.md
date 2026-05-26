# UInterpTrackInstFloatMaterialParam

- Symbol Type: class
- Symbol Path: Others / UInterpTrackInstFloatMaterialParam
- Source JSON Path: class/detail/Others/UInterpTrackInstFloatMaterialParam.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatMaterialParam.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaterialInstances | TArray < UMaterialInstanceDynamic * > | MIDs we're using to set the desired parameter. |  |
| ResetFloats | TArray < float > | Saved values for restoring state when exiting Matinee. |  |
| PrimitiveMaterialRefs | TArray < struct FPrimitiveMaterialRef > | Primitive components on which materials have been overridden. |  |
| InstancedTrack | UInterpTrackFloatMaterialParam * | track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately |  |

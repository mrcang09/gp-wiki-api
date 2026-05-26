# FClothParameterMask_PhysMesh

- Symbol Type: struct
- Symbol Path: FClothParameterMask_PhysMesh
- Source JSON Path: cppstruct/detail/FClothParameterMask_PhysMesh.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FClothParameterMask_PhysMesh.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

A mask is simply some storage for a physical mesh parameter painted onto clothing.
  Used in the editor for users to paint onto and then target to a parameter, which
  is then later applied to a phys mesh

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MaskName | FName | Name of the mask, mainly for users to differentiate |  |
| CurrentTarget | MaskTarget_PhysMesh | The currently targeted parameter for the mask |  |
| MaxValue | float | The maximum value currently in the mask value array |  |
| MinValue | float | The maximum value currently in the mask value array |  |
| Values | TArray < float > | The actual values stored in the mask |  |
| bEnabled | bool | Whether this mask is enabled and able to effect final mesh values |  |

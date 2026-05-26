# UParticleModuleBeamModifier

- Symbol Type: class
- Symbol Path: Others / UParticleModuleBeamModifier
- Source JSON Path: class/detail/Others/UParticleModuleBeamModifier.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleBeamModifier.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModifierType | TEnumAsByte < enum BeamModifierType > | Whether this module modifies the Source or the Target. |  |
| PositionOptions | FBeamModifierOptions | The options associated with the position. |  |
| Position | FRawDistributionVector | The value to use when modifying the position. |  |
| TangentOptions | FBeamModifierOptions | The options associated with the Tangent. |  |
| Tangent | FRawDistributionVector | The value to use when modifying the Tangent. |  |
| bAbsoluteTangent | uint32 | If true, don't transform the tangent modifier into the tangent basis. |  |
| StrengthOptions | FBeamModifierOptions | The options associated with the Strength. |  |
| Strength | FRawDistributionFloat | The value to use when modifying the Strength. |  |

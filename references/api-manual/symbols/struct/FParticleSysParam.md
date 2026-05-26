# FParticleSysParam

- Symbol Type: struct
- Symbol Path: FParticleSysParam
- Source JSON Path: cppstruct/detail/FParticleSysParam.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FParticleSysParam.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Struct used for a particular named instance parameter for this ParticleSystemComponent.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FName | The name of the parameter |  |
| ParamType | TEnumAsByte < enum EParticleSysParamType > | The type of parameters<br>	 	PSPT_None       - There is no data type<br>	 	PSPT_Scalar     - Use the scalar value<br>	 	PSPT_ScalarRand - Select a scalar value in the range [Scalar_Low..Scalar)<br>	 	PSPT_Vector     - Use the vector value<br>	 	PSPT_VectorRand - Select a vector value in the range [Vector_Low..Vector)<br>	 	PSPT_Color      - Use the color value<br>	 	PSPT_Actor      - Use the actor value<br>	 	PSPT_Material   - Use the material value |  |
| Scalar | float |  |  |
| Scalar_Low | float |  |  |
| Vector | FVector |  |  |
| Vector_Low | FVector |  |  |
| Color | FColor |  |  |
| Actor | AActor * |  |  |
| Material | UMaterialInterface * |  |  |

# FImportanceTexture

- Symbol Type: struct
- Symbol Path: FImportanceTexture
- Source JSON Path: cppstruct/detail/FImportanceTexture.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FImportanceTexture.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Texture processed for importance sampling
 Holds marginal PDF of the rows, as well as the PDF of each row

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Size | FIntPoint |  |  |
| NumMips | int |  |  |
| MarginalCDF | TArray < float > |  |  |
| ConditionalCDF | TArray < float > |  |  |
| TextureData | TArray < FColor > |  |  |
| Texture | TWeakObjectPtr < UTexture2D > |  |  |
| Weighting | TEnumAsByte < EImportanceWeight :: Type > |  |  |

# UOceanFFTComponent

- Symbol Type: class
- Symbol Path: Others / UOceanFFTComponent
- Source JSON Path: class/detail/Others/UOceanFFTComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UOceanFFTComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DisTexture | UTextureRenderTarget2D * |  |  |
| NormalMapTexture | UTextureRenderTarget2D * |  |  |
| FFTGridSize | int32 | Size of grid for FFT |  |
| WaveAmplitude | float |  |  |
| FetchLength | float |  |  |
| WaveSwell | float |  |  |
| WindSpeed | FVector2D |  |  |
| SamplePatch | FVector2D |  |  |
| WaveSpeed | float | Speed of time for FFT |  |
| XYDisplaceFactor | float |  |  |
| JacobianFactor | float |  |  |
| FoamDissipationSpeed | float |  |  |
| FoamFalloffSpeed | float |  |  |
| FoamGenerationAmount | float |  |  |
| FoamGenerationThreshold | float |  |  |
| DisplaceTextureArray | TArray < UTexture2D * > |  |  |
| NormalTextureArray | TArray < UTexture2D * > |  |  |
| Frameinterval | int |  |  |
| FrameNum | int32 |  |  |
| UpdateNeeded | bool |  |  |
| DisRTArray | TArray < UTextureRenderTarget2D * > |  |  |
| NormalRTArray | TArray < UTextureRenderTarget2D * > |  |  |

## Functions

### Update

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeltaTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

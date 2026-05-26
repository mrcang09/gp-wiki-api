# USceneCaptureComponentCube

- Symbol Type: class
- Symbol Path: Others / USceneCaptureComponentCube
- Source JSON Path: class/detail/Others/USceneCaptureComponentCube.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponentCube.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

Used to capture a 'snapshot' of the scene from a 6 planes and feed it to a render target.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TextureTarget | UTextureRenderTargetCube * | Temporary render target that can be used by the editor. |  |

## Functions

### CaptureScene

Render the scene to the texture target immediately.  
	  This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

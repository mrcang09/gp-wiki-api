# UDrawFrustumComponent

- Symbol Type: class
- Symbol Path: Others / UDrawFrustumComponent
- Source JSON Path: class/detail/Others/UDrawFrustumComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDrawFrustumComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

Utility component for drawing a view frustum. Origin is at the component location, frustum points down position X axis.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FrustumColor | FColor | Color to draw the wireframe frustum. |  |
| FrustumAngle | float | Angle of longest dimension of view shape. <br>	   If the angle is 0 then an orthographic projection is used |  |
| FrustumAspectRatio | float | Ratio of horizontal size over vertical size. |  |
| FrustumStartDist | float | Distance from origin to start drawing the frustum. |  |
| FrustumEndDist | float | Distance from origin to stop drawing the frustum. |  |
| Texture | UTexture * | optional texture to show on the near plane |  |

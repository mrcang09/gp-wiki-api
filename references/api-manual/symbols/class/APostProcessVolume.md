# APostProcessVolume

- Symbol Type: class
- Symbol Path: Others / APostProcessVolume
- Source JSON Path: class/detail/Others/APostProcessVolume.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/APostProcessVolume.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Settings | FPostProcessSettings | Post process settings to use for this volume. |  |
| Priority | float | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |  |
| BlendRadius | float | World space radius around the volume that is used for blending (only if not unbound). |  |
| BlendWeight | float | 0:no effect, 1:full effect |  |
| bEnabled | uint32 | Whether this volume is enabled or not. |  |
| bUnbound | uint32 | Whether this volume covers the whole world, or just the area inside its bounds. |  |

## Functions

### AddOrUpdateBlendable

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBlendableObject | TScriptInterface < IBlendableInterface >  |  |  |
| InWeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

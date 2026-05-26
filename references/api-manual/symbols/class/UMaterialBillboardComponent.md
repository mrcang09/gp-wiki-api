# UMaterialBillboardComponent

- Symbol Type: class
- Symbol Path: Others / UMaterialBillboardComponent
- Source JSON Path: class/detail/Others/UMaterialBillboardComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialBillboardComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

A 2d material that will be rendered always facing the camera.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Elements | TArray < FMaterialSpriteElement > | Current array of material billboard elements |  |

## Functions

### SetElements

Set all elements of this material billboard component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewElements | TArray < FMaterialSpriteElement > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddElement

Adds an element to the sprite.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface *  |  |  |
| DistanceToOpacityCurve | UCurveFloat *  |  |  |
| bSizeIsInScreenSpace | bool  |  |  |
| BaseSizeX | float  |  |  |
| BaseSizeY | float  |  |  |
| DistanceToSizeCurve | UCurveFloat * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

# ADecalActor

- Symbol Type: class
- Symbol Path: Others / ADecalActor
- Source JSON Path: class/detail/Others/ADecalActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ADecalActor.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

DecalActor contains a DecalComponent which can be used to render material modifications on top of existing geometry.

 @see UDecalComponent

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Decal | UDecalComponent * | The decal component for this decal actor |  |
| ArrowComponent | UArrowComponent * | Reference to the editor only arrow visualization component |  |
| SpriteComponent | UBillboardComponent * | Reference to the billboard component |  |
| BoxComponent_DEPRECATED | UBoxComponent * |  |  |

## Functions

### SetDecalMaterial

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDecalMaterial | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDecalMaterial

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface * |  |  |

### CreateDynamicMaterialInstance

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic * |  |  |

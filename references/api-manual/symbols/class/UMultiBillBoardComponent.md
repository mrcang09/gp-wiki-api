# UMultiBillBoardComponent

- Symbol Type: class
- Symbol Path: Others / UMultiBillBoardComponent
- Source JSON Path: class/detail/Others/UMultiBillBoardComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMultiBillBoardComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Elements | TArray < FBillBoardMaterialSpriteElement > | Current array of material billboard elements |  |
| BillboardDatas | TArray < FBillboardData > |  |  |

## Functions

### GetElements

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const TArray < FBillBoardMaterialSpriteElement > & |  |  |

### SetElements

Set all elements of this material billboard component

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewElements | TArray < FBillBoardMaterialSpriteElement > & |  |  |

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

### K2_AddBillBoard

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLocation | FVector  |  |  |
| UV0 | FVector2D  |  |  |
| UV1 | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RemoveBillboard

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ID | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearAllBillBoards

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetBillboardUV

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ID | int32  |  |  |
| UV0 | FVector2D  |  |  |
| UV1 | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CreateMultiBillboardComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| MultiBillboardClass | TSubclassOf < UMultiBillBoardComponent > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMultiBillBoardComponent *  |  |  |

# UNavigationPath

- Symbol Type: class
- Symbol Path: Others / UNavigationPath
- Source JSON Path: class/detail/Others/UNavigationPath.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UNavigationPath.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

UObject wrapper for FNavigationPath

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PathPoints | TArray < FVector > |  |  |
| RecalculateOnInvalidation | TEnumAsByte < ENavigationOptionFlag :: Type > |  |  |

## Functions

### GetDebugString

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### EnableDebugDrawing

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bShouldDrawDebugData | bool  |  |  |
| PathColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EnableRecalculationOnInvalidation

if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DoRecalculation | TEnumAsByte < ENavigationOptionFlag :: Type > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPathLength

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetPathCost

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### IsPartial

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsValid

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsStringPulled

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

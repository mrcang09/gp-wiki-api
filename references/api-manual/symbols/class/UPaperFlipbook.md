# UPaperFlipbook

- Symbol Type: class
- Symbol Path: Others / UPaperFlipbook
- Source JSON Path: class/detail/Others/UPaperFlipbook.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbook.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

Contains an animation sequence of sprite frames

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FramesPerSecond | float |  |  |
| KeyFrames | TArray < FPaperFlipbookKeyFrame > |  |  |
| DefaultMaterial | UMaterialInterface * |  |  |
| CollisionSource | TEnumAsByte < EFlipbookCollisionMode :: Type > |  |  |

## Functions

### GetNumFrames

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetTotalDuration

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetKeyFrameIndexAtTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bClampToEnds | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetSpriteAtTime

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Time | float  |  |  |
| bClampToEnds | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPaperSprite *  |  |  |

### GetSpriteAtFrame

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FrameIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPaperSprite *  |  |  |

### GetNumKeyFrames

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### IsValidKeyFrameIndex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Index | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

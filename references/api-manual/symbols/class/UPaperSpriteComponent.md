# UPaperSpriteComponent

- Symbol Type: class
- Symbol Path: Others / UPaperSpriteComponent
- Source JSON Path: class/detail/Others/UPaperSpriteComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

A component that handles rendering and collision for a single instance of a UPaperSprite asset.
 
  This component is created when you drag a sprite asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  @see UPrimitiveComponent, UPaperSprite

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceSprite | UPaperSprite * |  |  |
| MaterialOverride_DEPRECATED | UMaterialInterface * |  |  |
| SpriteColor | FLinearColor |  |  |

## Functions

### SetSprite

Change the PaperSprite used by this instance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewSprite | UPaperSprite * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetSprite

Gets the PaperSprite used by this instance.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPaperSprite * |  |  |

### SetSpriteColor

Set color of the sprite

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

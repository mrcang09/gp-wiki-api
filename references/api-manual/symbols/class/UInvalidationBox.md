# UInvalidationBox

- Symbol Type: class
- Symbol Path: Others / UInvalidationBox
- Source JSON Path: class/detail/Others/UInvalidationBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UInvalidationBox.json
- Mirrored At (UTC): 2026-05-19 08:23:30Z

---

## Description

Invalidate
   Single Child
   Caching  Performance

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bCanCache | bool | Should the invalidation panel cache the widgets?  Making this false makes it so the invalidation<br>	  panel stops acting like an invalidation panel, just becomes a simple container widget. |  |
| CacheRelativeTransforms | bool | Caches the locations for child draw elements relative to the invalidation box,<br>	  this adds extra overhead to drawing them every frame.  However, in cases where<br>	  the position of the invalidation boxes changes every frame this can be a big savings. |  |

## Functions

### InvalidateCache

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCanCache

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetCanCache

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CanCache | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

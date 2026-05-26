# UWidgetSkinProxy

- Symbol Type: class
- Symbol Path: Others / UWidgetSkinProxy
- Source JSON Path: class/detail/Others/UWidgetSkinProxy.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSkinProxy.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

The user widget proxy, using this proxy to activate widget skin for an user widget.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bHideBeforeLoadSkin | bool |  |  |
| ActiveSkins | TArray < UUserWidgetSkin * > |  |  |

## Functions

### ApplySkin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SkinPathPtr | TSoftClassPtr < UUserWidgetSkin >  |  |  |
| bAsyncLoad | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RevertSkin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SkinPathPtr | TSoftClassPtr < UUserWidgetSkin > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RevertRevertableSkin

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetActiveSkins

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | TArray < UUserWidgetSkin * > |  |  |

### GetRevertableSkin

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidgetSkin * |  |  |

### ContainsSkin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSkin | UUserWidgetSkin * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetOwnerUserWidget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidget * |  |  |

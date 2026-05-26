# UWidgetAnimation

- Symbol Type: class
- Symbol Path: Others / UWidgetAnimation
- Source JSON Path: class/detail/Others/UWidgetAnimation.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetAnimation.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MovieScene | UMovieScene * | Pointer to the movie scene that controls this animation. |  |
| AnimationBindings | TArray < FWidgetAnimationBinding > |  |  |

## Functions

### GetStartTime

Get the start time of this animation.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API float | Start time in seconds. |  |

### GetEndTime

Get the end time of this animation.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMG_API float | End time in seconds. |  |

### BindToAnimationStarted

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget *  |  |  |
| Delegate | FWidgetAnimationDynamicEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindFromAnimationStarted

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget *  |  |  |
| Delegate | FWidgetAnimationDynamicEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindAllFromAnimationStarted

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindToAnimationFinished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget *  |  |  |
| Delegate | FWidgetAnimationDynamicEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindFromAnimationFinished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget *  |  |  |
| Delegate | FWidgetAnimationDynamicEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindAllFromAnimationFinished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

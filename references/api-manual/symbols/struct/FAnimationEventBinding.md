# FAnimationEventBinding

- Symbol Type: struct
- Symbol Path: FAnimationEventBinding
- Source JSON Path: cppstruct/detail/FAnimationEventBinding.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimationEventBinding.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

Used to manage different animation event bindings that users want callbacks on.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation * | The animation to look for. |  |
| Delegate | FWidgetAnimationDynamicEvent | The callback. |  |
| AnimationEvent | EWidgetAnimationEvent | The type of animation event. |  |
| UserTag | FName | A user tag used to only get callbacks for specific runs of the animation. |  |

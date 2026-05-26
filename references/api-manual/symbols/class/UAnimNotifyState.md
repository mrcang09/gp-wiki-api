# UAnimNotifyState

- Symbol Type: class
- Symbol Path: Others / UAnimNotifyState
- Source JSON Path: class/detail/Others/UAnimNotifyState.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOldFPPAnimMode_ChangeToNewFPPMesh | bool |  |  |
| bEnableBoneRetargetAdaptFeature | bool |  |  |
| bCheckAnimIsolation | bool |  |  |
| bCheckAnimIsolation_OnlyNewFPP | bool |  |  |
| bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode | bool |  |  |
| bCheckAnimIsolation_OnlyTPP | bool | 仅在TPP（第三人称）下生效，开启后此NotifyState只会在TPP AnimInstance中触发 |  |

## Functions

### GetNotifyName

Implementable event to get a custom name for the notify

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### Received_NotifyBegin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshComp | USkeletalMeshComponent *  |  |  |
| Animation | UAnimSequenceBase *  |  |  |
| TotalDuration | float  |  |  |
| InvokeAnimInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Received_NotifyTick

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshComp | USkeletalMeshComponent *  |  |  |
| Animation | UAnimSequenceBase *  |  |  |
| FrameDeltaTime | float  |  |  |
| InvokeAnimInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Received_NotifyEnd

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MeshComp | USkeletalMeshComponent *  |  |  |
| Animation | UAnimSequenceBase *  |  |  |
| InvokeAnimInstance | UAnimInstance * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TryGetNewFPPAdaptSkelMeshComp

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| InIsInitCall | bool  |  |  |
| HasRetarget | bool  |  |  |
| ForceGetFPPMesh | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USkeletalMeshComponent *  |  |  |

### TryGetBoneRetargetAdaptSkelMeshComp

For Bone Retarget Feature Start

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| InIsInitCall | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USkeletalMeshComponent *  |  |  |

### ClearBoneRetargetAdaptState

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsBoneRetargetAdaptInitDone

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsEnableBoneRetargetAdaptFeature

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

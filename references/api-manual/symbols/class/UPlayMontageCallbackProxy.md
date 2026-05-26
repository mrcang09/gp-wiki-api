# UPlayMontageCallbackProxy

- Symbol Type: class
- Symbol Path: Others / UPlayMontageCallbackProxy
- Source JSON Path: class/detail/Others/UPlayMontageCallbackProxy.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPlayMontageCallbackProxy.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Functions

### CreateProxyObjectForPlayMontage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSkeletalMeshComponent | USkeletalMeshComponent *  |  |  |
| MontageToPlay | UAnimMontage *  |  |  |
| PlayRate | float  |  |  |
| StartingPosition | float  |  |  |
| StartingSection | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPlayMontageCallbackProxy *  |  |  |

### OnMontageBlendingOut

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| bInterrupted | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnMontageEnded

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Montage | UAnimMontage *  |  |  |
| bInterrupted | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnNotifyBeginReceived

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NotifyName | FName  |  |  |
| BranchingPointNotifyPayload | FBranchingPointNotifyPayload & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnNotifyEndReceived

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NotifyName | FName  |  |  |
| BranchingPointNotifyPayload | FBranchingPointNotifyPayload & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

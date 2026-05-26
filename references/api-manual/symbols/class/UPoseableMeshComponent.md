# UPoseableMeshComponent

- Symbol Type: class
- Symbol Path: Others / UPoseableMeshComponent
- Source JSON Path: class/detail/Others/UPoseableMeshComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPoseableMeshComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

UPoseableMeshComponent that allows bone transforms to be driven by blueprint.

## Functions

### SetBoneTransformByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| InTransform | FTransform &  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBoneLocationByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| InLocation | FVector  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBoneRotationByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| InRotation | FRotator  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBoneScaleByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| InScale3D | FVector  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBoneTransformByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### GetBoneLocationByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetBoneRotationByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetBoneScaleByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName  |  |  |
| BoneSpace | EBoneSpaces :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### ResetBoneTransformByName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BoneName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CopyPoseFromSkeletalComponent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InComponentToCopy | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

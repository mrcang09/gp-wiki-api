# USkeletalMeshSocket

- Symbol Type: class
- Symbol Path: Others / USkeletalMeshSocket
- Source JSON Path: class/detail/Others/USkeletalMeshSocket.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshSocket.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SocketName | FName | Defines a named attachment location on the USkeletalMesh. <br>	 	These are set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent.<br>	 	The Outer of a SkeletalMeshSocket should always be the USkeletalMesh. |  |
| BoneName | FName |  |  |
| RelativeLocation | FVector |  |  |
| RelativeRotation | FRotator |  |  |
| RelativeScale | FVector |  |  |
| BaseLocation | FVector |  |  |
| BaseRotation | FRotator |  |  |
| BaseScale | FVector |  |  |
| bDynamicCreate | bool |  |  |
| RelativeBoneName | FName |  |  |
| bForceAlwaysAnimated | bool | If true then the hierarchy of bones this socket is attached to will always be <br>	    evaluated, even if it had previously been removed due to the current lod setting |  |

## Functions

### GetSocketLocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SkelComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API FVector  |  |  |

### InitializeSocketFromLocation

Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SkelComp | USkeletalMeshComponent *  |  |  |
| WorldLocation | FVector  |  |  |
| WorldNormal | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ENGINE_API void  |  |  |

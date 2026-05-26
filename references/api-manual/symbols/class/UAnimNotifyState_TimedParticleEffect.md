# UAnimNotifyState_TimedParticleEffect

- Symbol Type: class
- Symbol Path: Others / UAnimNotifyState_TimedParticleEffect
- Source JSON Path: class/detail/Others/UAnimNotifyState_TimedParticleEffect.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState_TimedParticleEffect.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PSTemplate | UParticleSystem * |  |  |
| bIsPlayInWorld | bool |  |  |
| bIsRelativeToMeshSocketInWorld | bool |  |  |
| SocketName | FName |  |  |
| LocationOffset | FVector |  |  |
| RotationOffset | FRotator |  |  |
| RotationOffsetDisable | uint32 |  |  |
| ScaleDisable | uint32 |  |  |
| ScaleMultiplier | FVector |  |  |
| bDestroyAtEnd | bool |  |  |
| bEnableAttachMeshChangeIgnoreSocketCheck | bool |  |  |
| bAdaptToNewFPP | bool |  |  |
| CacheAttachAdaptMeshComp | TWeakObjectPtr < USkeletalMeshComponent > |  |  |
| SimulatedActivationOfQualityLevel | int32 |  |  |
| CurveParamList | TMap < FName , FCurveParams > |  |  |
| ParticleComp | UParticleSystemComponent * |  |  |
| bNotifyControlParticleVisible | bool |  |  |
| bEnableSpawnObjTrackFeature | bool |  |  |
| bAddAnotherBone_Z_Delta | bool |  |  |
| Z_Delta_BoneName | FName |  |  |
| ParticleTag | FName |  |  |
| SpawnedObjCacheMap | TMap < FName , TWeakObjectPtr < UObject > > |  |  |
| bSkipSocketNameCheck | bool |  |  |
| EnableDestoryByUniqueTagAtEnd | bool |  |  |
| PreviousPSTemplates | TArray < UParticleSystem * > |  |  |
| PreviousSocketNames | TArray < FName > |  |  |
| bInDebugMode | bool |  |  |
| CurrentLocationOffset | FVector |  |  |
| CurrentRotationOffset | FRotator |  |  |
| CurrentScaleMultiplier | FVector |  |  |
| CachedSpawnedParticleComponent | UParticleSystemComponent * |  |  |

## Functions

### IsEnableSpawnObjTrackFeature

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### TryMarkSpawnObjTracker

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| InSpawnedObj | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### TryClearSpawnObjTracker

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsTrackingObj

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetOverrideParticleTemplate

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| InPSTemplate | UParticleSystem * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UParticleSystem *  |  |  |

### GetOverrideParticleWorldTransform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent *  |  |  |
| TargetTransform | FTransform |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### InnerCheckParticleParentVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| skComp | USkeletalMeshComponent *  |  |  |
| InPSC | UParticleSystemComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### CheckParticleParentVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InComponent | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsEnableSearchAllDescendants

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTargetSkelMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SearchChildrenParticleAndDestroy

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Children | TArray < USceneComponent * >  |  |  |
| MeshComp | USkeletalMeshComponent *  |  |  |
| AttachAdaptMeshComp | USkeletalMeshComponent * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

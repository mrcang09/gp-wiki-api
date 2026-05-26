# APlayerCameraManager

- Symbol Type: class
- Symbol Path: Others / APlayerCameraManager
- Source JSON Path: class/detail/Others/APlayerCameraManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/APlayerCameraManager.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

A PlayerCameraManager is responsible for managing the camera for a particular
  player. It defines the final view properties used by other systems (e.g. the renderer),
  meaning you can think of it as your virtual eyeball in the world. It can compute the 
  final camera properties directly, or it can arbitrateblend between other objects or 
  actors that influence the camera (e.g. blending from one CameraActor to another).
  
  The PlayerCameraManagers primary external responsibility is to reliably respond to
  various Get() functions, such as GetCameraViewPoint. Most everything else is
  implementation detail and overrideable by user projects.
  
  By default, a PlayerCameraManager maintains a "view target", which is the primary actor
  the camera is associated with. It can also apply various "post" effects to the final 
  view state, such as camera animations, shakes, post-process effects or special 
  effects such as dirt on the lens.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PCOwner | APlayerController * | PlayerController that owns this Camera actor |  |
| TransformComponent | USceneComponent * | Dummy component we can use to attach things to the camera. |  |
| DefaultFOV | float | FOV to use by default. |  |
| DefaultOrthoWidth | float | The default desired width (in world units) of the orthographic view (ignored in Perspective mode) |  |
| DefaultAspectRatio | float | Default aspect ratio (used when a view target override the aspect ratio and bConstrainAspectRatio is set; most of the time the value from a camera component will be used instead) |  |
| CameraCache | FCameraCacheEntry | Cached camera properties. |  |
| LastFrameCameraCache | FCameraCacheEntry | Cached camera properties, one frame old. |  |
| ViewTarget | FTViewTarget | Current ViewTarget |  |
| PendingViewTarget | FTViewTarget | Pending view target for blending |  |
| CachedViewPOV | FMinimalViewInfo | If This POV is not null, Use this Value to Blend Target |  |
| ModifierList | TArray < UCameraModifier * > | List of active camera modifier instances that have a chance to update the final camera POV |  |
| DefaultModifiers | TArray < TSubclassOf < UCameraModifier > > | List of modifiers to create by default for this camera |  |
| FreeCamDistance | float | Distance to place free camera from view target (used in certain CameraStyles) |  |
| FreeCamOffset | FVector | Offset to Z free camera position (used in certain CameraStyles) |  |
| ViewTargetOffset | FVector | Offset to view target (used in certain CameraStyles) |  |
| CameraLensEffects | TArray < AEmitterCameraLensEffectBase * > | CameraBlood emitter attached to this camera |  |
| CachedCameraShakeMod | UCameraModifier_CameraShake * | Cached ref to modifier for code-driven screen shakes |  |
| AnimInstPool | UCameraAnimInst * | Internal pool of camera anim instance objects available for playing camera animations. Defines the max number of camera anims that can play simultaneously. |  |
| PostProcessBlendCache | TArray < struct FPostProcessSettings > | Internal pool of camera anim instance objects available for playing camera animations. Defines the max number of camera anims that can play simultaneously. <br>	class UCameraAnimInst AnimInstPool[8];    MAX_ACTIVE_CAMERA_ANIMS @fixme constant <br>	 Internal list of active post process effects. Parallel array to PostProcessBlendCacheWeights. |  |
| ActiveAnims | TArray < UCameraAnimInst * > | Array of camera anim instances that are currently playing and in-use |  |
| FreeAnims | TArray < UCameraAnimInst * > | Array of camera anim instances that are not playing and available to be used. |  |
| AnimCameraActor | ACameraActor * | Internal. Receives the output of individual camera animations. |  |
| bIsOrthographic | uint32 | True when this camera should use an orthographic perspective instead of FOV |  |
| bDefaultConstrainAspectRatio | uint32 | True if black bars should be added if the destination view has a different aspect ratio (only used when a view target doesn't specify whether or not to constrain the aspect ratio; most of the time the value from a camera component is used instead) |  |
| bUseClientSideCameraUpdates | uint32 | True if server will use camera positions replicated from the client instead of calculating them locally. |  |
| bGameCameraCutThisFrame | uint32 | True if we did a camera cut this frame. Automatically reset to false every frame.<br>	  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur). |  |
| SendServerUpdateCameraInterval | float |  |  |
| ViewPitchMin | float | Minimum view pitch, in degrees. |  |
| ViewPitchMax | float | Maximum view pitch, in degrees. |  |
| ViewYawMin | float | Minimum view yaw, in degrees. |  |
| ViewYawMax | float | Maximum view yaw, in degrees. |  |
| ViewRollMin | float | Minimum view roll, in degrees. |  |
| ViewRollMax | float | Maximum view roll, in degrees. |  |
| BaseCamAnimTrans | FTransform |  |  |
| NotifyCameraActor | ACameraActor * |  |  |

## Functions

### SetViewPitchMin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InViewPitchMin | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetViewPitchMin

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetViewPitchMax

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InViewPitchMax | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetViewPitchMax

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### PhotographyCameraModify

Implementable blueprint hook to allow a PlayerCameraManager subclass to
	 constrain or otherwise modify the camera during free-camera photography.
	 For example, a blueprint may wish to limit the distance from the camera's
	 original point, or forbid the camera from passing through walls.
	 NewCameraLocation contains the proposed new camera location.
	 PreviousCameraLocation contains the camera location in the previous frame.
	 OriginalCameraLocation contains the camera location before the game was put
	 into photography mode.
	 Return ResultCameraLocation as modified according to your constraints.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewCameraLocation | FVector  |  |  |
| PreviousCameraLocation | FVector  |  |  |
| OriginalCameraLocation | FVector  |  |  |
| ResultCameraLocation | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnPhotographySessionStart

Event triggered upon entering Photography mode (before pausing, if
	 r.Photography.AutoPause is 1).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnPhotographySessionEnd

Event triggered upon leaving Photography mode (after unpausing, if
	 r.Photography.AutoPause is 1).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnPhotographyMultiPartCaptureStart

Event triggered upon the start of a multi-part photograph capture (i.e. a
	 stereoscopic or 360-degree shot).  This is an ideal time to turn off
	 rendering effects that tile badly (UI, subtitles, vignette, very aggressive
	 bloom, etc; most of these are automatically disabled when
	 r.Photography.AutoPostprocess is 1).

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### OnPhotographyMultiPartCaptureEnd

Event triggered upon the end of a multi-part photograph capture, when manual
	 free-roaming photographic camera control is about to be returned to the user.
	 Here you may re-enable whatever was turned off within
	 OnPhotographyMultiPartCaptureStart.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### BlueprintUpdateCamera

Blueprint hook to allow blueprints to override existing camera behavior or implement custom cameras.
	  If this function returns true, we will use the given returned values and skip further calculations to determine
	  final camera POV.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CameraTarget | AActor *  |  |  |
| NewCameraLocation | FVector &  |  |  |
| NewCameraRotation | FRotator &  |  |  |
| NewCameraFOV | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetOwningPlayerController

Returns the PlayerController that owns this camera.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController * |  |  |

### SetCachedViewPOV

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Setup | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetViewTarget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor * | the current ViewTarget. |  |

### AddNewCameraModifier

Creates and initializes a new camera modifier of the specified class.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModifierClass | TSubclassOf < UCameraModifier > | - The class of camera modifier to create. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCameraModifier *  | Returns the newly created camera modifier. |  |

### FindCameraModifierByClass

Returns camera modifier for this camera of the given class, if it exists. 
	  Exact class match only. If there are multiple modifiers of the same class, the first one is returned.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModifierClass | TSubclassOf < UCameraModifier >  |  |  |
| bIncludeSuper | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCameraModifier *  |  |  |

### RemoveCameraModifier

Removes the given camera modifier from this camera (if it's on the camera in the first place) and discards it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ModifierToRemove | UCameraModifier * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if successfully removed, false otherwise. |  |

### GetFOVAngle

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | Returns the camera's current full FOV angle, in degrees. |  |

### SetFOV

Locks the FOV to the given value.  Unlock with UnlockFOV.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewFOV | float | - New full FOV angle to use, in degrees. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnlockFOV

Unlocks the FOV.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCameraRotation

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator | Returns camera's current rotation. |  |

### GetCameraLocation

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector | Returns camera's current location. |  |

### AddCameraLensEffect

Creates a camera lens effect of the given class on this camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LensEffectEmitterClass | TSubclassOf < AEmitterCameraLensEffectBase > | - Class of lens effect emitter to create. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AEmitterCameraLensEffectBase *  | Returns the new emitter actor. |  |

### RemoveCameraLensEffect

Removes the given lens effect from the camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Emitter | AEmitterCameraLensEffectBase * | - the emitter actor to remove from the camera |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearCameraLensEffects

Removes all camera lens effects.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### PlayCameraShake

Plays a camera shake on this camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShakeClass | TSubclassOf < UCameraShake >  |  |  |
| Scale | float  | - Scalar defining how "intense" to play the shake. 1.0 is normal (as authored). |  |
| PlaySpace | ECameraAnimPlaySpace :: Type  | - Which coordinate system to play the shake in (affects oscillations and camera anims) |  |
| UserPlaySpaceRot | FRotator | - Coordinate system to play shake when PlaySpace == CAPS_UserDefined. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCameraShake *  |  |  |

### PlayCameraShakeWithWorldLocation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShakeClass | TSubclassOf < UCameraShake >  |  |  |
| WorldLocation | FVector  |  |  |
| Scale | float  |  |  |
| PlaySpace | ECameraAnimPlaySpace :: Type  |  |  |
| UserPlaySpaceRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCameraShake *  |  |  |

### StopCameraShake

Immediately stops the given shake instance and invalidates it.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ShakeInstance | UCameraShake *  |  |  |
| bImmediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopAllInstancesOfCameraShake

Stops playing CameraShake of the given class.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Shake | TSubclassOf < UCameraShake >  |  |  |
| bImmediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopAllCameraShakes

Stops all active camera shakes on this camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bImmediately | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StartCameraFade

Does a camera fade tofrom a solid color.  Animates automatically.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FromAlpha | float  | - Alpha at which to begin the fade. Range [0..1], where 0 is fully transparent and 1 is fully opaque solid color. |  |
| ToAlpha | float  | - Alpha at which to finish the fade. |  |
| Duration | float  | - How long the fade should take, in seconds. |  |
| Color | FLinearColor  | - Color to fade tofrom. |  |
| bShouldFadeAudio | bool  | - True to fade audio volume along with the alpha of the solid color. |  |
| bHoldWhenFinished | bool | - True for fade to hold at the ToAlpha until explicitly stopped (e.g. with StopCameraFade) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopCameraFade

Stops camera fading.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetManualCameraFade

Turns on camera fading at the given opacity. Does not auto-animate, allowing user to animate themselves.
	  Call StopCameraFade to turn fading back off.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFadeAmount | float  |  |  |
| Color | FLinearColor  |  |  |
| bInFadeAudio | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayCameraAnim

Play the indicated CameraAnim on this camera.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Anim | UCameraAnim *  | The animation that should play on this instance. |  |
| Rate | float  |  How fast to play the animation. 1.0 is normal. |  |
| Scale | float  |  How "intense" to play the animation. 1.0 is normal. |  |
| BlendInTime | float  | Time to linearly ramp in. |  |
| BlendOutTime | float  | Time to linearly ramp out. |  |
| bLoop | bool  |  True to loop the animation if it hits the end. |  |
| bRandomStartTime | bool  | Whether or not to choose a random time to start playing. Useful with bLoop=true and a duration to randomize things like shakes. |  |
| Duration | float  |  Optional total playtime for this animation, including blends. 0 means to use animations natural duration, or infinite if looping. |  |
| PlaySpace | ECameraAnimPlaySpace :: Type  |  Which space to play the animation in. |  |
| UserPlaySpaceRot | FRotator | Custom play space, used when PlaySpace is UserDefined. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCameraAnimInst *  | The CameraAnim instance, which can be stored to manipulatestop the anim after the fact. |  |

### StopAllInstancesOfCameraAnim

Stop playing all instances of the indicated CameraAnim.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Anim | UCameraAnim *  |  |  |
| bImmediate | bool | True to stop it right now and ignore blend out, false to let it blend out as indicated. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopCameraAnimInst

Stops the given CameraAnimInst from playing.  The given pointer should be considered invalid after this.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AnimInst | UCameraAnimInst *  |  |  |
| bImmediate | bool | True to stop it right now and ignore blend out, false to let it blend out as indicated. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopAllCameraAnims

Stop playing all CameraAnims on this CameraManager.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bImmediate | bool | True to stop it right now and ignore blend out, false to let it blend out as indicated. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

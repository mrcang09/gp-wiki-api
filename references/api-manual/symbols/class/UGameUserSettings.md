# UGameUserSettings

- Symbol Type: class
- Symbol Path: Others / UGameUserSettings
- Source JSON Path: class/detail/Others/UGameUserSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameUserSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Description

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bUseVSync | bool | Whether to use VSync or not. (public to allow UI to connect to it) |  |
| ResolutionSizeX | uint32 | Game screen resolution width, in pixels. |  |
| ResolutionSizeY | uint32 | Game screen resolution height, in pixels. |  |
| LastUserConfirmedResolutionSizeX | uint32 | Game screen resolution width, in pixels. |  |
| LastUserConfirmedResolutionSizeY | uint32 | Game screen resolution height, in pixels. |  |
| IsBorderless | bool | Is game window borderless added by windzjliu |  |
| BorderlessMode | int32 |  |  |
| WindowPosX | int32 | Window PosX |  |
| WindowPosY | int32 | Window PosY |  |
| FullscreenMode | int32 | Game window fullscreen mode<br>	 	0 = Fullscreen<br>	 	1 = Windowed fullscreen<br>	 	2 = Windowed |  |
| LastConfirmedFullscreenMode | int32 | Last user confirmed fullscreen mode setting. |  |
| PreferredFullscreenMode | int32 | Fullscreen mode to use when toggling between windowed and fullscreen. Same values as r.FullScreenMode. |  |
| Version | uint32 | All settings will be wiped and set to default if the serialized version differs from UE_GAMEUSERSETTINGS_VERSION. |  |
| AudioQualityLevel | int32 |  |  |
| FrameRateLimit | float | Frame rate cap |  |
| DesiredScreenWidth | int32 | Desired screen width used to calculate the resolution scale when user changes display mode |  |
| bUseDesiredScreenHeight | bool | If true, the desired screen height will be used to scale the render resolution automatically. |  |
| DesiredScreenHeight | int32 | Desired screen height used to calculate the resolution scale when user changes display mode |  |
| LastRecommendedScreenWidth | float | Result of the last benchmark; calculated resolution to use. |  |
| LastRecommendedScreenHeight | float | Result of the last benchmark; calculated resolution to use. |  |
| LastCPUBenchmarkResult | float | Result of the last benchmark (CPU); -1 if there has not been a benchmark run |  |
| LastGPUBenchmarkResult | float | Result of the last benchmark (GPU); -1 if there has not been a benchmark run |  |
| LastCPUBenchmarkSteps | TArray < float > | Result of each individual sub-section of the last CPU benchmark; empty if there has not been a benchmark run |  |
| LastGPUBenchmarkSteps | TArray < float > | Result of each individual sub-section of the last GPU benchmark; empty if there has not been a benchmark run |  |
| LastGPUBenchmarkMultiplier | float | Multiplier used against the last GPU benchmark |  |
| bUseHDRDisplayOutput | bool | HDR |  |
| HDRDisplayOutputNits | int32 | HDR |  |

## Functions

### ApplySettings

Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bCheckForCommandLineOverrides | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ApplyNonResolutionSettings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ApplyResolutionSettings

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bCheckForCommandLineOverrides | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetScreenResolution

Returns the user setting for game screen resolution, in pixels.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntPoint |  |  |

### GetLastConfirmedScreenResolution

Returns the last confirmed user setting for game screen resolution, in pixels.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntPoint |  |  |

### GetDesktopResolution

Returns user's desktop resolution, in pixels.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntPoint |  |  |

### SetScreenResolution

Sets the user setting for game screen resolution, in pixels.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Resolution | FIntPoint |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetIsBorderless

IsBorderless getter and setter added by windzjliu

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetIsBorderless

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIsBorderless | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetBorderlessMode

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetBorderlessMode

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBorderlessMode | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFullscreenMode

Returns the user setting for game window fullscreen mode.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EWindowMode :: Type |  |  |

### GetLastConfirmedFullscreenMode

Returns the last confirmed user setting for game window fullscreen mode.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EWindowMode :: Type |  |  |

### SetFullscreenMode

Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFullscreenMode | EWindowMode :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPreferredFullscreenMode

Returns the user setting for game window fullscreen mode.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EWindowMode :: Type |  |  |

### SetVSyncEnabled

Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsVSyncEnabled

Returns the user setting for vsync.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsScreenResolutionDirty

Checks if the Screen Resolution user setting is different from current

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsFullscreenModeDirty

Checks if the FullscreenMode user setting is different from current

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsVSyncDirty

Checks if the vsync user setting is different from current system setting

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ConfirmVideoMode

Mark current video mode settings (fullscreenmoderesolution) as being confirmed by the user

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RevertVideoMode

Revert video mode (fullscreenmoderesolution) back to the last user confirmed values

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetBenchmarkFallbackValues

Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetAudioQualityLevel

Sets the user's audio quality level setting

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QualityLevel | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAudioQualityLevel

Returns the user's audio quality level setting

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetFrameRateLimit

Sets the user's frame rate limit (0 will disable frame rate limiting)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewLimit | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFrameRateLimit

Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetOverallScalabilityLevel

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOverallScalabilityLevel

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### GetResolutionScaleInformation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurrentScaleNormalized | float &  |  |  |
| CurrentScaleValue | int32 &  |  |  |
| MinScaleValue | int32 &  |  |  |
| MaxScaleValue | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetResolutionScaleInformationEx

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurrentScaleNormalized | float &  |  |  |
| CurrentScaleValue | float &  |  |  |
| MinScaleValue | float &  |  |  |
| MaxScaleValue | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetResolutionScaleValue

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScaleValue | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetResolutionScaleValueEx

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScaleValue | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetResolutionScaleNormalized

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewScaleNormalized | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetViewDistanceQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetViewDistanceQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetShadowQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetShadowQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetAntiAliasingQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAntiAliasingQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetTextureQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTextureQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetVisualEffectQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetVisualEffectQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetPostProcessingQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPostProcessingQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### SetFoliageQuality

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetFoliageQuality

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### IsDirty

Checks if any user settings is different from current

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### ValidateSettings

Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### LoadSettings

Loads the user settings from persistent storage

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bForceReload | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SaveSettings

Save the user settings to persistent storage (automatically happens as part of ApplySettings)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ResetToCurrentSettings

This function resets all settings to the current system settings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetToDefaults

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetDefaultResolutionScale

Gets the desired resolution quality based on DesiredScreenWidthHeight and the current screen resolution

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetRecommendedResolutionScale

Gets the recommended resolution quality based on LastRecommendedScreenWidthHeight and the current screen resolution

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetDefaultResolution

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntPoint | The default resolution when no resolution is set |  |

### GetDefaultWindowPosition

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntPoint | The default window position when no position is set |  |

### GetDefaultWindowMode

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EWindowMode :: Type | The default window mode when no mode is set |  |

### GetGameUserSettings

Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGameUserSettings * |  |  |

### RunHardwareBenchmark

Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorkScale | int32  |  |  |
| CPUMultiplier | float  |  |  |
| GPUMultiplier | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ApplyHardwareBenchmarkResults

Applies the settings stored in ScalabilityQuality and saves settings

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SupportsHDRDisplayOutput

Whether the curently running system supports HDR display output

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### EnableHDRDisplayOutput

Enables or disables HDR display output. Can be called again to change the desired nit level

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnable | bool  |  |  |
| DisplayNits | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentHDRDisplayNits

Returns 0 if HDR isn't supported or is turned off

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### IsHDREnabled

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

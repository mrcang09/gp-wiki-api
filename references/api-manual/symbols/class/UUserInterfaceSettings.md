# UUserInterfaceSettings

- Symbol Type: class
- Symbol Path: Others / UUserInterfaceSettings
- Source JSON Path: class/detail/Others/UUserInterfaceSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UUserInterfaceSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

User Interface settings that control Slate and UMG.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RenderFocusRule | ERenderFocusRule | Rule to determine if we should render the Focus Brush for widgets that have user focus. |  |
| HardwareCursors | TMap < TEnumAsByte < EMouseCursor :: Type > , FHardwareCursorReference > |  |  |
| SoftwareCursors | TMap < TEnumAsByte < EMouseCursor :: Type > , FSoftClassPath > |  |  |
| DefaultCursor_DEPRECATED | FSoftClassPath |  |  |
| TextEditBeamCursor_DEPRECATED | FSoftClassPath |  |  |
| CrosshairsCursor_DEPRECATED | FSoftClassPath |  |  |
| HandCursor_DEPRECATED | FSoftClassPath |  |  |
| GrabHandCursor_DEPRECATED | FSoftClassPath |  |  |
| GrabHandClosedCursor_DEPRECATED | FSoftClassPath |  |  |
| SlashedCircleCursor_DEPRECATED | FSoftClassPath |  |  |
| ApplicationScale | float | An optional application scale to apply on top of the custom scaling rules.  So if you want to expose a <br>	  property in your game title, you can modify this underlying value to scale the entire UI. |  |
| UIScaleRule | EUIScalingRule | The rule used when trying to decide what scale to apply. |  |
| CustomScalingRuleClass | FSoftClassPath | Set DPI Scale Rule to Custom, and this class will be used instead of any of the built-in rules. |  |
| UIScaleCurve | FRuntimeFloatCurve | Controls how the UI is scaled at different resolutions based on the DPI Scale Rule |  |
| ExtendUIScaleCurves | TArray < FRuntimeFloatCurve > |  |  |
| ExtendUIScaleCurveIndex | int32 |  |  |
| DefaultUIScaleCurveIndex | int32 |  |  |
| bScreenAdaption | bool |  |  |
| bUseFixedDPIMapping | bool |  |  |
| FixedDPIScaleConfig | TArray < FFixedDPIValueEntry > |  |  |
| bUseAndroidHarmonyFixedDPIScaleConfig | bool |  |  |
| AndroidHarmonyFixedDPIScaleConfig | TMap < FString , FFixedDPIValueEntry > |  |  |
| bLoadWidgetsOnDedicatedServer | bool | If false, widget references will be stripped during cook for server builds and not loaded at runtime. |  |
| FixDPIScaleCurveIndex | int32 |  |  |
| CursorClasses | TArray < UObject * > |  |  |
| CustomScalingRuleClassInstance | UClass * |  |  |
| CustomScalingRule | UDPICustomScalingRule * |  |  |

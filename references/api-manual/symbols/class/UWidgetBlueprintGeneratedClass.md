# UWidgetBlueprintGeneratedClass

- Symbol Type: class
- Symbol Path: Others / UWidgetBlueprintGeneratedClass
- Source JSON Path: class/detail/Others/UWidgetBlueprintGeneratedClass.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetBlueprintGeneratedClass.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

The widget blueprint generated class allows us to create blueprint-able widgets for UMG at runtime.
  All WBPGC's are of UUserWidget classes, and they perform special post initialization using this class
  to give themselves many of the same capabilities as AActor blueprints, like dynamic delegate binding for
  widgets.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetTree | UWidgetTree * | A tree of the widget templates to be created |  |
| WidgetTreePath | FSoftObjectPath |  |  |
| bAutoReleaseWidgetTree | uint8 |  |  |
| bAllowTemplate | uint8 |  |  |
| bValidTemplate | uint8 |  |  |
| bTemplateInitialized | uint8 |  |  |
| bCookedTemplate | uint8 |  |  |
| Bindings | TArray < FDelegateRuntimeBinding > |  |  |
| Animations | TArray < UWidgetAnimation * > |  |  |
| NamedSlots | TArray < FName > |  |  |
| TemplateAsset | TSoftObjectPtr < UUserWidget > |  |  |
| Template | UUserWidget * |  |  |

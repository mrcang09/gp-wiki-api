# FDebugDisplayProperty

- Symbol Type: struct
- Symbol Path: FDebugDisplayProperty
- Source JSON Path: cppstruct/detail/FDebugDisplayProperty.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FDebugDisplayProperty.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Debug property display functionality to interact with this, use "display", "displayall", "displayclear"
 
  @see UGameViewportClient
  @see FDebugDisplayProperty
  @see DrawStatsHUD

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Obj | UObject * | the object whose property to display. If this is a class, all objects of that class are drawn. |  |
| WithinClass | TSubclassOf < UObject > | if Obj is a class and WithinClass is not nullptr, further limit the display to objects that have an Outer of WithinClass |  |

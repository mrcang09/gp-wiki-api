# FShapedTextOptions

- Symbol Type: struct
- Symbol Path: FShapedTextOptions
- Source JSON Path: cppstruct/detail/FShapedTextOptions.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FShapedTextOptions.json
- Mirrored At (UTC): 2026-05-19 08:24:47Z

---

## Description

Common data for all widgets that use shaped text.
  Contains the common options that should be exposed for the underlying Slate widget.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverride_TextShapingMethod | uint32 |  |  |
| bOverride_TextFlowDirection | uint32 |  |  |
| TextShapingMethod | ETextShapingMethod | Which text shaping method should the text within this widget use? (unset to use the default returned by GetDefaultTextShapingMethod) |  |
| TextFlowDirection | ETextFlowDirection | Which text flow direction should the text within this widget use? (unset to use the default returned by GetDefaultTextFlowDirection) |  |

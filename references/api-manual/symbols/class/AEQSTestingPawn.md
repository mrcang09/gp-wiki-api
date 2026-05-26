# AEQSTestingPawn

- Symbol Type: class
- Symbol Path: Others / AEQSTestingPawn
- Source JSON Path: class/detail/Others/AEQSTestingPawn.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AEQSTestingPawn.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Description

this class is abstract even though it's perfectly functional on its own.
 	The reason is to stop it from showing as valid player pawn type when configuring 
 	project's game mode.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| QueryTemplate | UEnvQuery * |  |  |
| QueryParams | TArray < FEnvNamedValue > | optional parameters for query |  |
| QueryConfig | TArray < FAIDynamicParam > |  |  |
| TimeLimitPerStep | float |  |  |
| StepToDebugDraw | int32 |  |  |
| HighlightMode | EEnvQueryHightlightMode |  |  |
| bDrawLabels | uint32 |  |  |
| bDrawFailedItems | uint32 |  |  |
| bReRunQueryOnlyOnFinishedMove | uint32 |  |  |
| bShouldBeVisibleInGame | uint32 |  |  |
| bTickDuringGame | uint32 |  |  |
| QueryingMode | TEnumAsByte < EEnvQueryRunMode :: Type > |  |  |
| EdRenderComp | UEQSRenderingComponent * | Editor Preview |  |

# FAnimNode_CurveSource

- Symbol Type: struct
- Symbol Path: FAnimNode_CurveSource
- Source JSON Path: cppstruct/detail/FAnimNode_CurveSource.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CurveSource.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

Supply curves from some external source (e.g. audio)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourcePose | FPoseLink |  |  |
| SourceBinding | FName | The binding of the curve source we want to bind to.<br>	  We will bind to an object that implements ICurveSourceInterface. First we check <br>	  the actor that owns this (if any), then we check each of its components to see if we should<br>	  bind to the source that matches this name. |  |
| Alpha | float | How much we wan to blend the curve in by |  |
| CurveSource | TScriptInterface < ICurveSourceInterface > | Our bound source |  |

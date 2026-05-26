# FAnimNode_Base

- Symbol Type: struct
- Symbol Path: FAnimNode_Base
- Source JSON Path: cppstruct/detail/FAnimNode_Base.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Base.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Description

This is the base of all runtime animation nodes
 
  To create a new animation node:
    Create a struct derived from FAnimNode_Base - this is your runtime node
    Create a class derived from UAnimGraphNode_Base, containing an instance of your runtime node as a member - this is your visualeditor-only node

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NodeUID | int32 |  |  |
| EvaluateGraphExposedInputs | FExposedValueHandler |  |  |
| bEnableAsyncInitNode | bool |  |  |
| NodeTag | FName |  |  |

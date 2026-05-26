# FNode

- Symbol Type: struct
- Symbol Path: FNode
- Source JSON Path: cppstruct/detail/FNode.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FNode.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Rig Controller for bone transform

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FName | Name of the original node. We don't allow to change this. This is used for identity. |  |
| ParentName | FName | We save Parent Node but if the parent node is removed, it will reset to root |  |
| Transform | FTransform | Absolute transform of the node. Hoping to use this data in the future to render |  |
| DisplayName | FString | This is Display Name where it will be used to display in Retarget Manager. This name has to be unique. |  |
| bAdvanced | bool |  |  |

# FRepAttachment

- Symbol Type: struct
- Symbol Path: FRepAttachment
- Source JSON Path: cppstruct/detail/FRepAttachment.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRepAttachment.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

Handles attachment replication to clients. Movement replication will not happen while AttachParent is non-nullptr

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RelativeScale3D | FVector_NetQuantize100 |  |  |
| AttachParent | AActor * |  |  |
| LocationOffset | FVector_NetQuantize100 |  |  |
| RotationOffset | FRotator |  |  |
| AttachSocket | FName |  |  |
| AttachComponent | USceneComponent * |  |  |
| AttachParent_Direct | AActor * |  |  |
| bHasValidParent | bool |  |  |

# FToolMenuProfile

- Symbol Type: struct
- Symbol Path: FToolMenuProfile
- Source JSON Path: cppstruct/detail/FToolMenuProfile.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FToolMenuProfile.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

A menu profile is a way for systems to modify instances of a menu by showinghiding specific items. You can have multiple profiles active on
  a single menu at the same time.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FName |  |  |
| Entries | TMap < FName , FCustomizedToolMenuEntry > |  |  |
| Sections | TMap < FName , FCustomizedToolMenuSection > |  |  |
| SuppressExtenders | TArray < FName > |  |  |

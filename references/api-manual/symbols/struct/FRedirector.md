# FRedirector

- Symbol Type: struct
- Symbol Path: FRedirector
- Source JSON Path: cppstruct/detail/FRedirector.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FRedirector.json
- Mirrored At (UTC): 2026-05-19 08:24:46Z

---

## Description

This is used for redirecting old name to new name
 We use manually parsing array, but that makes harder to modify from property setting
 So adding this USTRUCT to support it properly

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewName | FName | Types of objects that this physics objects will collide with. |  |
| OldName | FName |  |  |

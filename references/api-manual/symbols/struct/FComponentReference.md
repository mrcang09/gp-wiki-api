# FComponentReference

- Symbol Type: struct
- Symbol Path: FComponentReference
- Source JSON Path: cppstruct/detail/FComponentReference.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FComponentReference.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Struct that allows for different ways to reference a component.
 	If just an Actor is specified, will return RootComponent of that Actor.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OtherActor | AActor * | Pointer to a different Actor that owns the Component. |  |
| ComponentProperty | FName | Name of component property to use |  |

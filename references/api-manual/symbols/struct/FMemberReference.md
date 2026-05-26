# FMemberReference

- Symbol Type: struct
- Symbol Path: FMemberReference
- Source JSON Path: cppstruct/detail/FMemberReference.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMemberReference.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MemberParent | UObject * | Most often the Class that this member is defined in. Could be a UPackage <br>	  if it is a native delegate signature function (declared globally). Should <br>	  be NULL if bSelfContext is true. |  |
| MemberScope | FString |  |  |
| MemberName | FName | Name of variable |  |
| MemberGuid | FGuid | The Guid of the variable |  |
| bSelfContext | bool | Whether or not this should be a "self" context |  |
| bWasDeprecated | bool | Whether or not this property has been deprecated |  |

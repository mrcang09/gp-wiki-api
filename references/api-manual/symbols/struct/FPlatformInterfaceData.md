# FPlatformInterfaceData

- Symbol Type: struct
- Symbol Path: FPlatformInterfaceData
- Source JSON Path: cppstruct/detail/FPlatformInterfaceData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FPlatformInterfaceData.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Struct that encompasses the most common types of data. This is the data payload
  of PlatformInterfaceDelegateResult.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DataName | FName | An optional tag for this data |  |
| Type | TEnumAsByte < enum EPlatformInterfaceDataType > | Specifies which value is valid for this structure |  |
| IntValue | int32 | Various typed result values |  |
| FloatValue | float |  |  |
| StringValue | FString |  |  |
| ObjectValue | UObject * |  |  |

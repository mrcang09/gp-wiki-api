# FEdGraphPinType

- Symbol Type: struct
- Symbol Path: FEdGraphPinType
- Source JSON Path: cppstruct/detail/FEdGraphPinType.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphPinType.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

Struct used to define the type of information carried on this pin

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PinCategory | FString | Category of pin type |  |
| PinSubCategory | FString | Sub-category of pin type |  |
| PinSubCategoryObject | TWeakObjectPtr < UObject > | Sub-category object |  |
| PinSubCategoryMemberReference | FSimpleMemberReference | Sub-category member reference |  |
| PinValueType | FEdGraphTerminalType | Data used to determine value types when bIsMap is true |  |
| ContainerType | EPinContainerType |  |  |
| bIsArray_DEPRECATED | uint8 | DEPRECATED(4.17) Whether or not this pin represents an array of values |  |
| bIsReference | uint8 | Whether or not this pin is a value passed by reference or not |  |
| bIsConst | uint8 | Whether or not this pin is a immutable const value |  |
| bIsWeakPointer | uint8 | Whether or not this is a weak reference |  |

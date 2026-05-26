# FAIDataProviderValue

- Symbol Type: struct
- Symbol Path: FAIDataProviderValue
- Source JSON Path: cppstruct/detail/FAIDataProviderValue.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderValue.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Description

AIDataProvider is an object that can provide collection of properties
  associated with bound pawn owner or request Id.
 
  Editable properties are used to set up provider instance,
  creating additional filters or ways of accessing data (e.g. gameplay tag of ability)
 
  Non editable properties are holding data

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CachedProperty | UProperty * | cached uproperty of provider |  |
| DataBinding | UAIDataProvider * | (optional) provider for dynamic data binding |  |
| DataField | FName | name of provider's value property |  |

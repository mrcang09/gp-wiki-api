# FAssetData

- Symbol Type: struct
- Symbol Path: FAssetData
- Source JSON Path: cppstruct/detail/FAssetData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAssetData.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

A struct to hold important information about an assets found by the Asset Registry
  This struct is transient and should never be serialized

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ObjectPath | FName | The object path for the asset in the form PackageName.AssetName. Only top level objects in a package can have AssetData |  |
| PackageName | FName | The name of the package in which the asset is found, this is the full long package name such as GamePathPackage |  |
| PackagePath | FName | The path to the package in which the asset is found, this is GamePath with the Package stripped off |  |
| AssetName | FName | The name of the asset without the package |  |
| AssetClass | FName | The name of the asset's class |  |
| AssetTags | TArray < FName > | Custom Asset Type Tag |  |

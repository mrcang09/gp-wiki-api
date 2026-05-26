# FFullyLoadedPackagesInfo

- Symbol Type: struct
- Symbol Path: FFullyLoadedPackagesInfo
- Source JSON Path: cppstruct/detail/FFullyLoadedPackagesInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FFullyLoadedPackagesInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Struct to help hold information about packages needing to be fully-loaded for DLC, etc.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FullyLoadType | TEnumAsByte < enum EFullyLoadPackageType > | When to load these packages |  |
| Tag | FString | When this map or gametype is loaded, the packages in the following array will be loaded and added to root, then removed from root when map is unloaded |  |
| PackagesToLoad | TArray < FName > | The list of packages that will be fully loaded when the above Map is loaded |  |
| LoadedObjects | TArray < UObject * > | List of objects that were loaded, for faster cleanup |  |

# FAssetBundleEntry

- Symbol Type: struct
- Symbol Path: FAssetBundleEntry
- Source JSON Path: cppstruct/detail/FAssetBundleEntry.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAssetBundleEntry.json
- Mirrored At (UTC): 2026-05-19 08:24:35Z

---

## Description

A struct representing a single AssetBundle

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BundleScope | FPrimaryAssetId | Asset this bundle is saved within. This is empty for global bundles, or in the saved bundle info |  |
| BundleName | FName | Specific name of this bundle, should be unique for a given scope |  |
| BundleAssets | TArray < FSoftObjectPath > | List of string assets contained in this bundle |  |

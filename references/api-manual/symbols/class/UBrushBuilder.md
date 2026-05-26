# UBrushBuilder

- Symbol Type: class
- Symbol Path: Others / UBrushBuilder
- Source JSON Path: class/detail/Others/UBrushBuilder.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBrushBuilder.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

Base class of UnrealEd brush builders.
 
 
  Tips for writing brush builders:
 
  - Always validate the user-specified and call BadParameters function
    if anything is wrong, instead of actually building geometry.
    If you build an invalid brush due to bad user parameters, you'll
    cause an extraordinary amount of pain for the poor user.
 
  - When generating polygons with more than 3 vertices, BE SURE all the
    polygon's vertices are coplanar!  Out-of-plane polygons will cause
    geometry to be corrupted.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BitmapFilename | FString |  |  |
| ToolTip | FString | localized FString that will be displayed as the name of this brush builder in the editor |  |
| NotifyBadParams | uint32 | If false, disabled the bad param notifications |  |
| Vertices | TArray < FVector > |  |  |
| Polys | TArray < struct FBuilderPoly > |  |  |
| Layer | FName |  |  |
| MergeCoplanars | uint32 |  |  |

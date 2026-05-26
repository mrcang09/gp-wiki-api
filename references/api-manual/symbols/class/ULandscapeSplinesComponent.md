# ULandscapeSplinesComponent

- Symbol Type: class
- Symbol Path: Others / ULandscapeSplinesComponent
- Source JSON Path: class/detail/Others/ULandscapeSplinesComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeSplinesComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ControlPoints | TArray < ULandscapeSplineControlPoint * > |  |  |
| Segments | TArray < ULandscapeSplineSegment * > |  |  |
| CookedForeignMeshComponents | TArray < UMeshComponent * > |  |  |
| SplineResolution | float | Resolution of the spline, in distance per point |  |
| SplineColor | FColor | Color to use to draw the splines |  |
| ControlPointSprite | UTexture2D * | Sprite used to draw control points |  |
| SplineEditorMesh | UStaticMesh * | Mesh used to draw splines that have no mesh |  |
| bShowSplineEditorMesh | uint32 | Whether we are in-editor and showing spline editor meshes |  |
| ForeignWorldSplineDataMap | TMap < TSoftObjectPtr < UWorld > , FForeignWorldSplineData > |  |  |

# ABrush

- Symbol Type: class
- Symbol Path: Others / ABrush
- Source JSON Path: class/detail/Others/ABrush.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ABrush.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BrushType | TEnumAsByte < enum EBrushType > | Type of brush |  |
| BrushColor | FColor |  |  |
| PolyFlags | int32 |  |  |
| bColored | uint32 |  |  |
| bSolidWhenSelected | uint32 |  |  |
| bPlaceableFromClassBrowser | uint32 | If true, this brush class can be placed using the class browser like other simple class types |  |
| bNotForClientOrServer | uint32 | If true, this brush is a builder or otherwise does not need to be loaded into the game |  |
| Brush | UModel * |  |  |
| BrushComponent | UBrushComponent * |  |  |
| bInManipulation | uint32 | Flag set when we are in a manipulation (scaling, translation, brush builder param change etc.) |  |
| SavedSelections | TArray < struct FGeomSelection > | Stores selection information from geometry mode.  This is the only information that we can't<br>	  regenerate by looking at the source brushes following an undo operation. |  |

# UMaterialFunction

- Symbol Type: class
- Symbol Path: Others / UMaterialFunction
- Source JSON Path: class/detail/Others/UMaterialFunction.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMaterialFunction.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

A Material Function is a collection of material expressions that can be reused in different materials

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| StateId | FGuid | Used by materials using this function to know when to recompile. |  |
| Description | FString | Description of the function which will be displayed as a tooltip wherever the function is used. |  |
| bExposeToLibrary | uint32 | Whether to list this function in the material function library, which is a window in the material editor that lists categorized functions. |  |
| bUseFullPrecision | uint32 | Whether forces the function to use full (highp) precision in the pixel shader. |  |
| FunctionExpressions | TArray < UMaterialExpression * > | Array of material expressions, excluding Comments.  Used by the material editor. |  |
| bReentrantFlag | uint32 | Transient flag used to track re-entrance in recursive functions like IsDependent. |  |
| ParentFunction | UMaterialFunction * | Used in the material editor, points to the function asset being edited, which this function is just a preview for. |  |
| LibraryCategories_DEPRECATED | TArray < FString > | Categories that this function belongs to in the material function library.  <br>	  Ideally categories should be chosen carefully so that there are not too many. |  |
| LibraryCategoriesText | TArray < FText > | Categories that this function belongs to in the material function library.  <br>	  Ideally categories should be chosen carefully so that there are not too many. |  |
| FunctionEditorComments | TArray < UMaterialExpressionComment * > | Array of comments associated with this material; viewed in the material editor. |  |
| PreviewMaterial | UMaterial * |  |  |
| CombinedInputTypes | uint32 |  |  |
| CombinedOutputTypes | uint32 |  |  |
| ThumbnailInfo | UThumbnailInfo * | Information for thumbnail rendering |  |

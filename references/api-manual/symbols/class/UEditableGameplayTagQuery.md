# UEditableGameplayTagQuery

- Symbol Type: class
- Symbol Path: Others / UEditableGameplayTagQuery
- Source JSON Path: class/detail/Others/UEditableGameplayTagQuery.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQuery.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

This is an editor-only representation of a query, designed to be editable with a typical property window.
  To edit a query in the editor, an FGameplayTagQuery is converted to a set of UObjects and edited,  When finished,
  the query struct is rewritten and these UObjects are discarded.
  This query representation is not intended for runtime use.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UserDescription | FString | User-supplied description, shown in property details. Auto-generated description is shown if not supplied. |  |
| RootExpression | UEditableGameplayTagQueryExpression * | The base expression of this query. |  |
| TagQueryExportText_Helper | FGameplayTagQuery | Property to hold a gameplay tag query so we can use the exporttext path to get a string representation. |  |

# UListView

- Symbol Type: class
- Symbol Path: Others / UListView
- Source JSON Path: class/detail/Others/UListView.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UListView.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Description

Allows thousands of items to be displayed in a list.  Generates widgets dynamically for each item.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ItemHeight | float | The height of each widget |  |
| Items | TArray < UObject * > | The list of items to generate widgets for |  |
| SelectionMode | TEnumAsByte < ESelectionMode :: Type > | The selection method for the list |  |
| OnGenerateRowEvent | FOnGenerateRowUObject | Called when a widget needs to be generated |  |

# UGCCommonDragDropItem

- Symbol Type: class
- Symbol Path: Others / UGCCommonDragDropItem
- Source JSON Path: class/detail/Others/UGCCommonDragDropItem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGCCommonDragDropItem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

拖拽控件

## Functions

### SetDragWidget

设置拖拽时的控件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget|Class | 拖拽时的控件实例 或 类 |  |
| bCreate | boolean | 是否创建控件，传入Class则创建控件实例 |  |

### SetDragDirectionMode

设置拖拽方向模式

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DirectionMode | EDragDirectionMode | 拖拽方向模式 |  |

### SetDragDropMode

设置拖拽模式

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DragDropMode | EDragDropMode | 拖拽模式 |  |

### RegisterDragDropData

注册拖拽(入口)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DragDropData | table | 拖拽数据 |  |
| DragDropMode | EDragDropMode | 拖拽模式 |  |

### SetData

设置拖拽数据

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Data | table | 拖拽数据 |  |

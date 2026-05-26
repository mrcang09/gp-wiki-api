# UGCWidgetManagerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / UI 界面 / UGCWidgetManagerSystem
- Source JSON Path: class/detail/和平全局接口/UI 界面/UGCWidgetManagerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/UI%20%E7%95%8C%E9%9D%A2/UGCWidgetManagerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

UI控件管理器系统接口库

## Functions

### CreateWidgetAsync

异步创建一个控件，返回控件实例

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClassPath | string|FSoftObjectPath | 控件类路径 |  |
| OnCreatedCallback | fun(Widget:UUserWidget) | 创建完成回调 |  |

### CreateWidget

创建一个控件，返回控件实例

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClass | UClass | 控件蓝图类 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidget | 控件实例 |  |

### DestroyWidget

销毁一个控件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

### AddToSlot

添加一个控件到指定 UI 挂点槽位

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |
| SlotName | string | 控件槽位名称，默认为 UI.UISlot.MainUISlot_Low |  |
| ZOrder | number | 控件层级，默认为 0 |  |
| AnchorData | FAnchorData | 控件锚点，默认为 { Anchors = { Minimum = Vector2D.New(0, 0), Maximum = Vector2D.New(1, 1) } } | cppstruct/detail/FAnchorData.json |

### RemoveFromSlot

从 UI 挂点槽位移除控件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

### SetWidgetLayout

异步加载并设置当前的 WidgetLayout，同时只能设置一个，旧的 WidgetLayout 会被卸载。传入 “Default” 可卸载 WidgetLayout 回到默认状态。（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LayoutPath | string | WidgetLayout 引用路径 |  |

### ShowWidget

显示一个控件，需要控件已经挂载到挂点槽上

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

### HideWidget

隐藏一个控件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

### IsWidgetAddedToSlot

判断一个控件是否已经挂载在 UI 挂点上

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否已经挂载 |  |

### IsWidgetVisible

判断一个控件是否可见

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 是否可见 |  |

### GetSubWidget

获取子控件，可用于获取 UMG 蓝图里的子控件

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |
| SubWidgetName | string | 子控件名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget | 子控件实例 |  |

### GetAllWidgetsOfClass

获取指定类别的所有控件，可筛选只获取已被添加到挂点的控件
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClass | UClass | 控件类（UUserWidget） |  |
| bAddedToSlotOnly | boolean | 是否只获取已添加到挂点的控件 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidget[] | 控件实例列表 |  |

### GetMainUI

获取主 UI 面板实例（MainControlPanelTochButton）
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### GetMainControlUI

获取主控制 UI 面板实例（MainControlBaseUI）
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### GetShootingUIPanel

获取射击相关UI面板实例（ShootingUIPanel）
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### GetSkillRootPanel

获取技能相关UI面板实例（SkillRootPanel_BP）
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### GetUserWidgetByWidgetLayout

获取通过WidgetLayout加载的自定义UserWidget
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetLayoutPath | string | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |  |
| UserWidgetName | string | 控件 Name |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### SubWidgetHiddenLayer

【废弃】请使用 UGCWidgetManagerSystem.ShowWidget
SubWidgetHiddenLayer为控件减少隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UserWidget |  |  |

### SetVirtualJoystickVisibility

设置摇杆是否可见
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsVisibility | boolean | 是否可见（true 为显示，false 为隐藏） |  |

### SetCrosshairVisibility

设置准星是否可见
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsVisibility | boolean | 是否可见（true 为显示，false 为隐藏，在没有被隐藏的情况下禁止将其显示） |  |

### Share

弹出分享界面
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CloseCallBack | function | 关闭分享界面回调函数 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 分享调用是否成功 |  |

### AddChildToTochButton

把自定义 UI 挂到和平 UI 上并应用自定义布局
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UserWidget |  |  |

### LoadLobbyChatFrameUI

加载大厅聊天框 UI
生效范围：客户端

### AddObjectPositionUI

添加对象位置 UI,头顶 UI（类似血条，玩家名）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | Actor | 需要添加位置 UI 的 Actor 对象 |  |
| WidgetClassPath | string | 控件 ClassPath 控件需继承自 UObjectPositionWidget |  |
| Offset | FVector | 偏移量 | cppstruct/detail/FVector.json |
| SizeAutoContent | boolean | 大小适配 |  |
| OutViewHide | boolean | 控件离开镜头后是否隐藏（比如在背后） |  |
| BeOcclusionHide | boolean | 被遮挡后是否隐藏 |  |
| ShowSelf | boolean | 是否显示自己的 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 实例 Index |  |

### AddObjectPositionUI_Custom

添加对象位置 UI,头顶 UI（类似血条，玩家名），自定义版本，提供更多参数配置。（ObjectPosUIInfo 可在蓝图中添加参数使用带有默认值的版本）
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | Actor | 需要添加位置 UI 的 Actor 对象 |  |
| WidgetClassPath | string | 控件 ClassPath 控件需继承自 UObjectPositionWidget |  |
| ObjectPosUIInfo | FObjectPosUIInfo | 配置属性结构体，可以在蓝图中定义该变量传入 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 实例 Index |  |

### RemoveObjectPositionUI

移除对象位置 UI
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContent | UObject | 世界中对象 |  |
| InstanceIndex | number | 实例 Index |  |

### GetObjectPositionUI

根据 InstanceIndex 获取 Widget 实例（Add 之后不能立刻获取到，Widget 有可能还在加载）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContent | UObject | 世界中对象 |  |
| InstanceIndex | number | 实例 Index |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UObjectPositionWidget | @Widget | 实例 |  |

### SetPlayerStateUIVisibility

设置玩家状态 UI 可见性
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bVisible | boolean | 是否显示（true 为显示，false 为隐藏） |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 实际修改的控件数量 |  |

### ShowTipsUI

在屏幕中间上方显示 Tips 内容
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TipsContent | string | Tips 文字内容 |  |

### ShowTipsUIByServer

在屏幕中间上方显示 Tips 内容，从DS发起，在传入的PC所属的客户端显示
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TipsContent | string | Tips 文字内容 |  |
| PlayerController | PlayerController | 玩家控制器 |  |

### GetGlobalOBUI

获取全局观战 UI，仅全局观战模式下生效
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### ChangeMap

修改右上角地图
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MapPath | string | 地图文件路径 |  |
| MapCentre | FVector | 地图中心点坐标 | cppstruct/detail/FVector.json |
| MapSize | number | 地图实际大小 |  |
| MapScale | number | 地图缩放比 |  |

### ChangeMapByMapID

根据地图ID修改右上角地图
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MapID | number | 地图ID |  |

### ProjectWorldLocationToWidgetPosition

将世界坐标转换为控件坐标
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldLocation | FVector | 世界坐标 | cppstruct/detail/FVector.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 控件坐标 | cppstruct/detail/FVector2D.json |

### SlotAsCanvasSlot

获取 Canvas 插槽
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UCanvasPanelSlot |  Canvas 插槽实例 |  |

### SlotAsOverlaySlot

获取 Overlay 插槽
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UOverlaySlot | @Overlay | 插槽实例 |  |

### SlotAsVerticalBoxSlot

获取 HorizontalBox 插槽
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UUserWidget | 控件实例 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UVerticalBoxSlot | @HorizontalBox | 插槽实例 |  |

### GetViewportScale

获取视口缩放比例
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 缩放比例 |  |

### GetViewportSize

获取视口尺寸
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 视口尺寸 | cppstruct/detail/FVector2D.json |

### GetViewportWidgetGeometry

获取视口 Widget 几何信息
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGeometry | 几何信息 |  |

### AbsoluteToLocal

绝对坐标转本地坐标
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry | 控件几何信息 |  |
| AbsoluteCoordinate | FVector2D | 绝对坐标 | cppstruct/detail/FVector2D.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 本地坐标 | cppstruct/detail/FVector2D.json |

### LocalToAbsolute

本地坐标转绝对坐标
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry | 控件几何信息 |  |
| LocalCoordinate | FVector2D | 本地坐标 | cppstruct/detail/FVector2D.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 绝对坐标 | cppstruct/detail/FVector2D.json |

### GetLocalSize

获取控件的本地尺寸
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry | 控件几何信息 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 本地尺寸 | cppstruct/detail/FVector2D.json |

### GetAbsoluteSize

获取控件的绝对尺寸
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry | 控件几何信息 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 绝对尺寸 | cppstruct/detail/FVector2D.json |

### GetAbsolutePosition

获取控件的绝对位置
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Geometry | FGeometry | 控件几何信息 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | 绝对位置 | cppstruct/detail/FVector2D.json |

### GetWidgetFromName

【废弃】请使用 UGCWidgetManagerSystem.GetSubWidget
通过控件名获取某一控件的子控件
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UserWidget |  |  |
| UserWidgetName | string | 控件 Name |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### LoadMainUIWidgetLayoutByPath

【废弃】请使用 UGCWidgetManagerSystem.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetLayoutPath | string | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |  |

### UnloadMainUIWidgetLayoutByPath

【废弃】请使用 UGCWidgetManagerSystem.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetLayoutPath | string | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |  |

### AddChildToUISlotByPath

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync() + UGCWidgetManagerSystem.AddToSlot()
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetPath | string | 控件 ClassPath |  |
| UISlotName | string | 挂点标识 |  |
| ZOrder | number | 层级 |  |
| AnchorData | FAnchorData | 控件布局信息 | cppstruct/detail/FAnchorData.json |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | PromiseFuture对象 |  |

### AddChildToUISlotByWidget

【废弃】请使用 UGCWidgetManagerSystem.AddToSlot
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UserWidget | UI |  |
| UISlotName | string | 挂点标识 |  |
| ZOrder | number | 层级 |  |
| AnchorData | FAnchorData | 控件布局信息 | cppstruct/detail/FAnchorData.json |

### AddWidgetHiddenLayer

【废弃】请使用 UGCWidgetManagerSystem.HideWidget
为控件添加隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UserWidget |  |  |

### AddNewUI

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync() + UGCWidgetManagerSystem.AddToSlot()
添加新 UI，将会自动完成 AddViewport 显示
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClassPath | string | Widget 路径 |  |
| IsAdaptation | boolean | 是否屏幕适配 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### CreateNewWidget

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync
创建新控件
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClassPath | string | Widget 路径 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UserWidget |  |  |

### CreateNewWidgetAsync

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync
异步创建新控件，并绑定回调
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetClassPath | string | Widget 路径 |  |
| InCreatedDelegate | ULuaSingleDelegate | 回调 |  |

# UPESkillWidget

- Symbol Type: class
- Symbol Path: Others / UPESkillWidget
- Source JSON Path: class/detail/Others/UPESkillWidget.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPESkillWidget.json
- Mirrored At (UTC): 2026-05-19 08:23:36Z

---

## Description

技能UI基类

## Functions

### BindToSlot

将技能绑定到指定PE组件的指定Slot上
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Comp | UPersistBaseComponent *  | 绑定的组件 |  |
| SlotName | FGameplayTag | 绑定的槽位 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetCurrentSkill

获取当前绑定的技能
	  生效范围C

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPersistEffectSkill * | 当前绑定的技能 |  |

### BindImageAndTextForSkillNameAndIcon

绑定用于显示技能图标、名字、描述的控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IconImage | UImage *  | 图标控件 |  |
| NameText | UTextBlock *  | 名字控件 |  |
| DescribeText | UTextBlock * | 描述控件 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RefreshSkillUI

刷新当前UI绑定的控件的内容
	  生效范围C

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetSkillName

获取技能名字
	  生效范围C

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName | 技能名字 |  |

### GetSkillDetail

获取技能描述
	  生效范围C

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString | 技能描述 |  |

### GetSkillIcon

获取技能图标
	  生效范围C

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSoftObjectPath | 技能图标 |  |

### InitButton

绑定技能按钮控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IconImage | UImage *  | 图标控件 |  |
| NameText | UTextBlock *  | 名字控件 |  |
| ClickButton | UButton * | 按钮控件 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitLayer

绑定技能使用层数控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LayerText | UTextBlock *  | 技能层数 |  |
| LayerPanel | UPanelWidget * | 技能层数的Panel控件，控制层数的显隐 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitCDProgress

绑定技能CD控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CDText | UTextBlock *  | 技能CD时间 |  |
| CDProgressImage | UImage *  | @技能CD进度条 |  |
| CDProgressPanel | UPanelWidget * | 整个CD的Panel控件，控制CD的显隐 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitEnergyProgress

绑定技能能量控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EnergyProgressImage | UImage *  | 技能能量进度条 |  |
| EnergyCanvasPanel | UPanelWidget * | 技能能量Panel控件，控制能量进度条的显隐 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitTagDisableState

绑定技能显示TagDisable状态的控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagDisableCanvasPanel | UPanelWidget * | 技能TagDisable状态的Panel控件，控制TagDisable状态的显隐 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitEnableState

绑定技能显示Enable状态的控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EnableCanvasPanel | UPanelWidget * | 技能Enable状态的Panel控件，控制Enable状态的显隐 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### InitVirtualJoystick

绑定技能摇杆输入控件
	  生效范围C

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| VirtualJoystickPanel | UPanelWidget *  |  |  |
| VirtualJoystick | UPESkillVirtualJoystick * | 技能技能摇杆控件，控制摇杆的生效和失效 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

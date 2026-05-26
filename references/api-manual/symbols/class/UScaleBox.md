# UScaleBox

- Symbol Type: class
- Symbol Path: Others / UScaleBox
- Source JSON Path: class/detail/Others/UScaleBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UScaleBox.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
  you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
  to auto fit some text to an area, this is the control for you.
 
   Single Child
   Aspect Ratio

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stretch | TEnumAsByte < EStretch :: Type > | The stretching rule to apply when content is stretched |  |
| StretchDirection | TEnumAsByte < EStretchDirection :: Type > | Controls in what direction content can be scaled |  |
| UserSpecifiedScale | float | Optional scale that can be specified by the User. Used only for UserSpecified stretching. |  |
| UserSpecifiedScaleBias | float | Scale bias that can fit to the content, especially for the text exceeded the bounds. <br>	 #if UMG_SCALE_BIAS |  |
| IgnoreInheritedScale | bool | Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation. |  |
| UsePcParams | bool |  |  |
| StretchPc | TEnumAsByte < EStretch :: Type > |  |  |
| StretchDirectionPc | TEnumAsByte < EStretchDirection :: Type > |  |  |
| UserSpecifiedScalePc | float |  |  |
| UserSpecifiedScaleBiasPc | float |  |  |
| IgnoreInheritedScalePc | bool |  |  |
| bSingleLayoutPass | bool | Only perform a single layout pass, if you do this, it can save a considerable<br>	  amount of time, however, some things like text may not look correct.  You may also<br>	  see the UI judder between frames.  This generally is caused by not explicitly<br>	  sizing the widget, and instead allowing it to layout based on desired size along<br>	  which won't work in Single Layout Pass mode. |  |
| bFroceSlateLayoutCachingCalcSize | bool |  |  |
| bForceUseLastUnPrepassChildSize | bool |  |  |

## Functions

### SetStretch

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InStretch | EStretch :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetStretchDirection

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InStretchDirection | EStretchDirection :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUserSpecifiedScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InUserSpecifiedScale | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIgnoreInheritedScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInIgnoreInheritedScale | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetUserSpecifiedScaleBias

#if UMG_SCALEBOX_BIAS

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InUserSpecifiedScaleBias | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPcParamController

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InValue | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnUIRectOffsetChange

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

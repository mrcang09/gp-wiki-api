# UProgressBar

- Symbol Type: class
- Symbol Path: Others / UProgressBar
- Source JSON Path: class/detail/Others/UProgressBar.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UProgressBar.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

The progress bar widget is a simple bar that fills up that can be restyled to fit any number of uses.
 
   No Children

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WidgetStyle | FProgressBarStyle | The progress bar style |  |
| Style_DEPRECATED | USlateWidgetStyleAsset * | Style used for the progress bar |  |
| BackgroundImage_DEPRECATED | USlateBrushAsset * | The brush to use as the background of the progress bar |  |
| FillImage_DEPRECATED | USlateBrushAsset * | The brush to use as the fill image |  |
| MarqueeImage_DEPRECATED | USlateBrushAsset * | The brush to use as the marquee image |  |
| Percent | float | Used to determine the fill position of the progress bar ranging 0..1 |  |
| BarFillType | TEnumAsByte < EProgressBarFillType :: Type > | Defines if this progress bar fills Left to right or right to left |  |
| bIsMarquee | bool |  |  |
| BorderPadding | FVector2D |  |  |
| PercentDelegate | FGetFloat | A bindable delegate to allow logic to drive the text of the widget |  |
| FillColorAndOpacity | FLinearColor | Fill Color and Opacity |  |
| FillColorAndOpacityDelegate | FGetLinearColor |  |  |

## Functions

### SetPercent

Sets the current value of the ProgressBar.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPercent | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOppositePercent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPercent | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFillColorAndOpacity

Sets the fill color of the progress bar.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetIsMarquee

Sets the progress bar to show as a marquee.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InbIsMarquee | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPercent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetOppositePercent

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

# USizeBox

- Symbol Type: class
- Symbol Path: Others / USizeBox
- Source JSON Path: class/detail/Others/USizeBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USizeBox.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

A widget that allows you to specify the size it reports to have and desire.  Not all widgets report a desired size
  that you actually desire.  Wrapping them in a SizeBox lets you have the Size Box force them to be a particular size.
 
   Single Child
   Fixed Size

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bOverride_WidthOverride | uint32 |  |  |
| bOverride_HeightOverride | uint32 |  |  |
| bOverride_MinDesiredWidth | uint32 |  |  |
| bOverride_MinDesiredHeight | uint32 |  |  |
| bOverride_MaxDesiredWidth | uint32 |  |  |
| bOverride_MaxDesiredHeight | uint32 |  |  |
| bOverride_MaxAspectRatio | uint32 |  |  |
| WidthOverride | float | When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width. |  |
| HeightOverride | float | When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height. |  |
| MinDesiredWidth | float | When specified, will report the MinDesiredWidth if larger than the content's desired width. |  |
| MinDesiredHeight | float | When specified, will report the MinDesiredHeight if larger than the content's desired height. |  |
| MaxDesiredWidth | float | When specified, will report the MaxDesiredWidth if smaller than the content's desired width. |  |
| MaxDesiredHeight | float | When specified, will report the MaxDesiredHeight if smaller than the content's desired height. |  |
| MaxAspectRatio | float |  |  |

## Functions

### SetWidthOverride

When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InWidthOverride | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearWidthOverride

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetHeightOverride

When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InHeightOverride | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearHeightOverride

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMinDesiredWidth

When specified, will report the MinDesiredWidth if larger than the content's desired width.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMinDesiredWidth | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMinDesiredWidth

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMinDesiredHeight

When specified, will report the MinDesiredHeight if larger than the content's desired height.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMinDesiredHeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMinDesiredHeight

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMaxDesiredWidth

When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaxDesiredWidth | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMaxDesiredWidth

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMaxDesiredHeight

When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaxDesiredHeight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMaxDesiredHeight

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### SetMaxAspectRatio

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMaxAspectRatio | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ClearMaxAspectRatio

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

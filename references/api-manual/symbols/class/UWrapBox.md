# UWrapBox

- Symbol Type: class
- Symbol Path: Others / UWrapBox
- Source JSON Path: class/detail/Others/UWrapBox.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWrapBox.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

Arranges widgets left-to-right.  When the widgets exceed the Width it will place widgets on the next line.
  
   Many Children
   Flows
   Wraps

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InnerSlotPadding | FVector2D | The inner slot padding goes between slots sharing borders |  |
| WrapWidth | float | When this width is exceeded, elements will start appearing on the next line. |  |
| bExplicitWrapWidth | bool | Use explicit wrap width whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI" |  |

## Functions

### SetInnerSlotPadding

Sets the inner slot padding goes between slots sharing borders

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPadding | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddChildWrapBox

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Content | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWrapBoxSlot *  |  |  |

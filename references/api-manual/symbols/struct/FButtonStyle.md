# FButtonStyle

- Symbol Type: struct
- Symbol Path: FButtonStyle
- Source JSON Path: cppstruct/detail/FButtonStyle.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FButtonStyle.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Represents the appearance of an SButton

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Normal | FSlateBrush | Button appearance when the button is not hovered or pressed |  |
| Hovered | FSlateBrush | Button appearance when hovered |  |
| Pressed | FSlateBrush | Button appearance when pressed |  |
| Disabled | FSlateBrush | Button appearance when disabled, by default this is set to an invalid resource when that is the case default disabled drawing is used. |  |
| NormalPadding | FMargin | Padding that accounts for the border in the button's background image.<br>	  When this is applied, the content of the button should appear flush<br>	  with the button's border. Use this padding when the button is not pressed. |  |
| PressedPadding | FMargin | Same as NormalPadding but used when the button is pressed. Allows for moving the content to match<br>	  any "movement" in the button's border image. |  |
| PressedSlateSound | FSlateSound | The sound the button should play when pressed |  |
| HoveredSlateSound | FSlateSound | The sound the button should play when initially hovered over |  |
| PressedSound_DEPRECATED | FName |  |  |
| HoveredSound_DEPRECATED | FName |  |  |

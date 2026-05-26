# UMenuAnchor

- Symbol Type: class
- Symbol Path: Others / UMenuAnchor
- Source JSON Path: class/detail/Others/UMenuAnchor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMenuAnchor.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

The Menu Anchor allows you to specify an location that a popup menu should be anchored to, 
  and should be summoned from.
   Single Child
   Popup

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MenuClass | TSubclassOf < UUserWidget > | The widget class to spawn when the menu is required.  Creates the widget freshly each time.  <br>	  If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent <br>	  instead. |  |
| OnGetMenuContentEvent | FGetWidget | Called when the menu content is requested to allow a more customized handling over what to display |  |
| Placement | TEnumAsByte < EMenuPlacement > | The placement location of the summoned widget. |  |
| ShouldDeferPaintingAfterWindowContent | bool |  |  |
| UseApplicationMenuStack | bool | Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself. |  |

## Functions

### ToggleOpen

Toggles the menus open state.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bFocusOnOpen | bool | Should we focus the popup as soon as it opens? |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Open

Opens the menu if it is not already open

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bFocusMenu | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Close

Closes the menu if it is currently open.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsOpen

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the popup is open; false otherwise. |  |

### ShouldOpenDueToClick

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if we should open the menu due to a click. Sometimes we should not, if |  |

### GetMenuPosition

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | The current menu position |  |

### HasOpenSubMenus

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | Whether this menu has open submenus |  |

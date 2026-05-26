# UPlatformEventsComponent

- Symbol Type: class
- Symbol Path: Others / UPlatformEventsComponent
- Source JSON Path: class/detail/Others/UPlatformEventsComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPlatformEventsComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Description

Component to handle receiving notifications from the OS about platform events.

## Functions

### IsInLaptopMode

Check whether a convertible laptop is laptop mode.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if in laptop mode, false otherwise or if not a convertible laptop. |  |

### IsInTabletMode

Check whether a convertible laptop is laptop mode.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if in tablet mode, false otherwise or if not a convertible laptop. |  |

### SupportsConvertibleLaptops

Check whether the platform supports convertible laptops.
	 
	  Note: This does not necessarily mean that the platform is a convertible laptop.
	  For example, convertible laptops running Windows 7 or older will return false,
	  and regular laptops running Windows 8 or newer will return true.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true for convertible laptop platforms, false otherwise. |  |

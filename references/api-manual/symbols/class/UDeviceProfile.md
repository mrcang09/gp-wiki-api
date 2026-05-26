# UDeviceProfile

- Symbol Type: class
- Symbol Path: Others / UDeviceProfile
- Source JSON Path: class/detail/Others/UDeviceProfile.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDeviceProfile.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DeviceType | FString | The type of this profile, I.e. IOS, Windows, PS4 etc |  |
| BaseProfileName | FString | The name of the parent profile of this object |  |
| Parent | UObject * | The parent object of this profile, it is the object matching this DeviceType with the BaseProfileName |  |
| CVars | TArray < FString > | The collection of CVars which is set from this profile |  |

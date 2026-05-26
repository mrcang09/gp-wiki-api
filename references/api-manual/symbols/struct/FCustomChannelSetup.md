# FCustomChannelSetup

- Symbol Type: struct
- Symbol Path: FCustomChannelSetup
- Source JSON Path: cppstruct/detail/FCustomChannelSetup.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCustomChannelSetup.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Structure for custom channel setup information.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Channel | TEnumAsByte < enum ECollisionChannel > | Which channel you'd like to customize |  |
| Name | FName | Name of channel you'd like to show up |  |
| DefaultResponse | TEnumAsByte < enum ECollisionResponse > | Default Response for the channel |  |
| bTraceType | bool | Sets meta data TraceType="1" for the enum entry if true. Otherwise, this channel will be treated as object query channel, so you can query object types |  |
| bStaticObject | bool | Specifies if this is static object. Otherwise it will be dynamic object. This is used for query all objects vs all static objects vs all dynamic objects |  |

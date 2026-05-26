# FNetDriverDefinition

- Symbol Type: struct
- Symbol Path: FNetDriverDefinition
- Source JSON Path: cppstruct/detail/FNetDriverDefinition.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FNetDriverDefinition.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Container for describing various types of netdrivers available to the engine
  The engine will try to construct a netdriver of a given type and, failing that,
  the fallback version.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefName | FName | Unique name of this net driver definition |  |
| DriverClassName | FName | Class name of primary net driver |  |
| DriverClassNameFallback | FName | Class name of the fallback net driver if the main net driver class fails to initialize |  |

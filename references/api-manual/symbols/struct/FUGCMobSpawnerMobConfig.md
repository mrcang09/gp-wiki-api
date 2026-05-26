# FUGCMobSpawnerMobConfig

- Symbol Type: struct
- Symbol Path: FUGCMobSpawnerMobConfig
- Source JSON Path: cppstruct/detail/FUGCMobSpawnerMobConfig.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FUGCMobSpawnerMobConfig.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

刷怪系统：怪物刷新配置

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConfigMode | EUGCMobSpawnerConfigMode | 刷出怪物类型的配置方式 |  |
| MobClass | TSubclassOf < AGenericCharacter > | 使用蓝图配置时，刷出的怪物类 |  |
| MobGroupID | int32 | 使用怪物组表时，怪物组表的ID |  |
| CustomParam | TMap < FString , FString > | 使用自定义模式时，自定义参数列表 |  |

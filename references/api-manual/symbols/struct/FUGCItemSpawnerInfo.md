# FUGCItemSpawnerInfo

- Symbol Type: struct
- Symbol Path: FUGCItemSpawnerInfo
- Source JSON Path: cppstruct/detail/FUGCItemSpawnerInfo.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FUGCItemSpawnerInfo.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

物资生成管理器上每个刷新点的配置

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Spawner | AUGCItemSpawner * | 使用的刷新点 |  |
| bOverrideItemConfig | bool | 是否覆盖该刷新点上的物资配置，开启则刷新点上的配置无效，使用这里的配置 |  |
| ItemConfig | FUGCItemSpawnerItemConfig | 配置刷新点上的物资配置 |  |

# UUGCGamePartConfig

- Symbol Type: class
- Symbol Path: Others / UUGCGamePartConfig
- Source JSON Path: class/detail/Others/UUGCGamePartConfig.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UUGCGamePartConfig.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

GamePart配置基类

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GamePartName | FName | GamePart名称 |  |
| DependentGameParts | TArray < FName > | 依赖的的GamePart列表 |  |
| GlobalActorClass | TSubclassOf < AActor > | GlobalActor类配置 |  |
| PlayerComponentConfigs | TArray < FUGCGamePartPlayerComponentConfig > | GamePart PlayerComponent配置列表 |  |

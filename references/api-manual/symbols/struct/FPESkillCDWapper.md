# FPESkillCDWapper

- Symbol Type: struct
- Symbol Path: FPESkillCDWapper
- Source JSON Path: cppstruct/detail/FPESkillCDWapper.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FPESkillCDWapper.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

技能CD信息

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CDType | EPESkillCDType | 技能CD类型 |  |
| CDRecoveryTime | float | CD能量充能时间 |  |
| AllowRecoveryDuringActivation | bool | 技能激活期间恢复CD能量 |  |
| MaxLayer | int | 最大充能次数 |  |
| CDEnergyConsume | float | 持续消耗型每秒扣除速率，如果不选energy，就是直接扣完一层的所有能量 |  |
| AllowConsumeMinEnergy | float | 能开始消耗能量的最小百分比 |  |

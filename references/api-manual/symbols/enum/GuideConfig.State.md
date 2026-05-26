# GuideConfig.State

- Symbol Type: enum
- Symbol Path: GuideConfig.State
- Source JSON Path: cppenum/detail/GuideConfig.State.json
- Source JSON URL: https://developer.gp.qq.com/api/cppenum/detail/GuideConfig.State.json
- Mirrored At (UTC): 2026-05-19 08:24:32Z

---

## Variables

| Name | Value | Description |
| --- | --- | --- |
| Idle | 1 |   |
| Active | 2 | -- 空闲：等待触发 |
| Completed | 3 | -- 空闲：等待触发 -- 激活：正在显示 |
| Disabled | 4 | -- 空闲：等待触发 -- 激活：正在显示 -- 已完成（本次） |
| Queued | 5 | -- 空闲：等待触发 -- 激活：正在显示 -- 已完成（本次） -- 已禁用（达到完成上限） |

# FUGCRankingListData

- Symbol Type: struct
- Symbol Path: FUGCRankingListData
- Source JSON Path: cppstruct/detail/FUGCRankingListData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FUGCRankingListData.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

排行榜表格结构体

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ID | int32 | 排行榜索引ID |  |
| PeopleNum | int32 | 排行榜最大上榜人数 |  |
| PeriodType | ERankListPeriodType | 排行榜周期类型 |  |
| BeginDate | FDateTime | 排行榜开始时间 |  |
| SettleDate | FDateTime | 非周期榜结算时间 |  |
| EndDate | FDateTime | 排行榜结束时间 |  |
| SortPropertyName | FString | 排序属性名称 |  |
| SortType | ERankListSortType | 排序类型 |  |
| RankAward | TArray < FRankListAward > | 排行榜奖励列表 |  |
| TabName | FString | 排行榜页签名称 |  |
| EnableType | ERankListEnableType | 是否启用排行榜 |  |
| ShowInGame | ERankListDisplayType | 是否在玩法内展示 |  |
| ShowInDetails | ERankListDisplayType | 是否在玩法详情页展示 |  |
| Desc | FString | 排行榜说明 |  |
| ScoreFormatType | ERankListScoreFormatType | 分数显示格式 |  |

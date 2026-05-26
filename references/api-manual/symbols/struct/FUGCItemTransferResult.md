# FUGCItemTransferResult

- Symbol Type: struct
- Symbol Path: FUGCItemTransferResult
- Source JSON Path: cppstruct/detail/FUGCItemTransferResult.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FUGCItemTransferResult.json
- Mirrored At (UTC): 2026-05-19 08:24:49Z

---

## Description

物品转移结果

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CanTransfer | bool | 转移是否成功 |  |
| TransferErrorReason | TArray < FName > | 如果转移失败，失败原因来自于转移者 |  |
| ItemErrorReason | TMap < FItemDefineID , FName > | 如果转移失败，失败原因来自于物品 |  |

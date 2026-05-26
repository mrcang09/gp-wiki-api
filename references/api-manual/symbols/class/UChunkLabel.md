# UChunkLabel

- Symbol Type: class
- Symbol Path: Others / UChunkLabel
- Source JSON Path: class/detail/Others/UChunkLabel.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UChunkLabel.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Rules | FPrimaryAssetRules | Management rules for this specific asset, if set it will override the type rules |  |
| LogicChunkName | FString | True to Label everything in this directory and sub directories |  |
| FinalChunkName | FString |  |  |
| ChunkOutputPath | FString |  |  |
| bIsRuntimeLabel | uint32 | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |  |
| Key | FString |  |  |
| IV | FString |  |  |
| ManagerRuleNames | TArray < FString > |  |  |
| bUpdateManagerRulesWhenSaved | bool |  |  |
| bForceReloadManagerRule | bool |  |  |

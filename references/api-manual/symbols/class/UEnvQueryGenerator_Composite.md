# UEnvQueryGenerator_Composite

- Symbol Type: class
- Symbol Path: Others / UEnvQueryGenerator_Composite
- Source JSON Path: class/detail/Others/UEnvQueryGenerator_Composite.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Composite.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

Composite generator allows using multiple generators in single query option
  All child generators must produce exactly the same item type!

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Generators | TArray < UEnvQueryGenerator * > |  |  |
| bAllowDifferentItemTypes | uint32 | allow generators with different item types, use at own risk!<br>	 <br>	   WARNING: <br>	   generator will use ForcedItemType for raw data, you MUST ensure proper memory layout<br>	   child generators will be writing to memory block through their own item types:<br>	   - data must fit info block allocated by ForcedItemType<br>	   - tests will read item locationproperties through ForcedItemType |  |
| bHasMatchingItemType | uint32 |  |  |
| ForcedItemType | TSubclassOf < UEnvQueryItemType > |  |  |

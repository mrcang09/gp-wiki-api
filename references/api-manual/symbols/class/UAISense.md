# UAISense

- Symbol Type: class
- Symbol Path: Others / UAISense
- Source JSON Path: class/detail/Others/UAISense.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAISense.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DefaultExpirationAge | float | age past which stimulus of this sense are "forgotten" |  |
| NotifyType | EAISenseNotifyType |  |  |
| bWantsNewPawnNotification | uint32 | whether this sense is interested in getting notified about new Pawns being spawned <br>	 	this can be used for example for automated sense sources registration |  |
| bAutoRegisterAllPawnsAsSources | uint32 | If true all newly spawned pawns will get auto registered as source for this sense. |  |
| PerceptionSystemInstance | UAIPerceptionSystem * |  |  |

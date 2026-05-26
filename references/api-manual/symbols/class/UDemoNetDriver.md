# UDemoNetDriver

- Symbol Type: class
- Symbol Path: Others / UDemoNetDriver
- Source JSON Path: class/detail/Others/UDemoNetDriver.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDemoNetDriver.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Description

Simulated network driver for recording and playing back game sessions.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RollbackNetStartupActors | TMap < FString , FRollbackNetStartupActorInfo > | Net startup actors that need to be rolled back during scrubbing by being destroyed and re-spawned <br>	  NOTE - DeletedNetStartupActors will take precedence here, and destroy the actor instead |  |
| CheckpointSaveMaxMSPerFrame | float | Maximum time allowed each frame to spend on saving a checkpoint. If 0, it will save the checkpoint in a single frame, regardless of how long it takes.<br>	  See also demo.CheckpointSaveMaxMSPerFrameOverride. |  |
| bIsLocalReplay | bool |  |  |
| GameInstance | UGameInstance * |  |  |

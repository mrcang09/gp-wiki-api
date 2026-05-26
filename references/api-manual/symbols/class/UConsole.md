# UConsole

- Symbol Type: class
- Symbol Path: Others / UConsole
- Source JSON Path: class/detail/Others/UConsole.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UConsole.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Description

A basic command line console that accepts most commands.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConsoleTargetPlayer | ULocalPlayer * | The player which the next console command should be executed in the context of.  If nullptr, execute in the viewport. |  |
| DefaultTexture_Black | UTexture2D * |  |  |
| DefaultTexture_White | UTexture2D * |  |  |
| HistoryBuffer | TArray < FString > | Holds the history buffer, order is old to new |  |

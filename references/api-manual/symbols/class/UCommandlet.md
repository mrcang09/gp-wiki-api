# UCommandlet

- Symbol Type: class
- Symbol Path: Others / UCommandlet
- Source JSON Path: class/detail/Others/UCommandlet.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCommandlet.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HelpDescription | FString | Description of the commandlet's purpose |  |
| HelpUsage | FString | Usage template to show for "ucc help" |  |
| HelpWebLink | FString | Hyperlink for more info |  |
| HelpParamNames | TArray < FString > | The name of the parameter the commandlet takes |  |
| HelpParamDescriptions | TArray < FString > | The description of the parameter |  |
| IsServer | uint32 | Whether to load objects required in server, client, and editor context.  If IsEditor is set to false, then a<br>	  UGameEngine (or whatever the value of ScriptEngine.Engine.GameEngine is) will be created for the commandlet instead<br>	  of a UEditorEngine (or ScriptEngine.Engine.EditorEngine), unless the commandlet overrides the CreateCustomEngine method. |  |
| IsClient | uint32 |  |  |
| IsEditor | uint32 |  |  |
| LogToConsole | uint32 | Whether to redirect standard log to the console |  |
| ShowErrorCount | uint32 | Whether to show standard error and warning count on exit |  |

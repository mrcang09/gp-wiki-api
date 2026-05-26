# FExternalToolDefinition

- Symbol Type: struct
- Symbol Path: FExternalToolDefinition
- Source JSON Path: cppstruct/detail/FExternalToolDefinition.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FExternalToolDefinition.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

Structure for defining an external tool

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ToolName | FString | The name of the tool  test. |  |
| ExecutablePath | FFilePath | The executable to run. <br>	UPROPERTY(config, EditAnywhere, Category=ExternalTools, meta=(FilePathFilter = "")) |  |
| CommandLineOptions | FString | The command line options to pass to the executable. |  |
| WorkingDirectory | FDirectoryPath | The working directory for the new process. |  |
| ScriptExtension | FString | If set, look for scripts with this extension. |  |
| ScriptDirectory | FDirectoryPath | If the ScriptExtension is set, look here for the script files. |  |

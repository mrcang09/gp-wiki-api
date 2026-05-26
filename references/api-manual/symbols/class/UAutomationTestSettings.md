# UAutomationTestSettings

- Symbol Type: class
- Symbol Path: Others / UAutomationTestSettings
- Source JSON Path: class/detail/Others/UAutomationTestSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAutomationTestSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Implements the Editor's user settings.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EngineTestModules | TArray < FString > | Modules to load that have engine tests |  |
| EditorTestModules | TArray < FString > | Modules to load that have editor tests |  |
| AutomationTestmap | FSoftObjectPath | The automation test map to be used for several of the automation tests. |  |
| EditorPerformanceTestMaps | TArray < FEditorMapPerformanceTestDefinition > | The map to be used for the editor performance capture tool. |  |
| AssetsToOpen | TArray < FSoftObjectPath > | Asset to test for open in automation process |  |
| BuildPromotionTest | FBuildPromotionTestSettings | Editor build promotion test settings |  |
| MaterialEditorPromotionTest | FMaterialEditorPromotionSettings | Material editor promotion test settings |  |
| ParticleEditorPromotionTest | FParticleEditorPromotionSettings | Particle editor promotion test settings |  |
| BlueprintEditorPromotionTest | FBlueprintEditorPromotionSettings | Blueprint editor promotion test settings |  |
| TestLevelFolders | TArray < FString > | Folders containing levels to exclude from automated tests |  |
| ExternalTools | TArray < FExternalToolDefinition > | External executables and scripts to run as part of automation. |  |
| ImportExportTestDefinitions | TArray < FEditorImportExportTestDefinition > | Asset import  Export test settings |  |
| LaunchOnSettings | TArray < FLaunchOnTestSettings > | The map and device type to be used for the editor Launch On With Map Iterations test. |  |
| DefaultScreenshotResolution | FIntPoint | The default resolution to take all automation screenshots at. |  |

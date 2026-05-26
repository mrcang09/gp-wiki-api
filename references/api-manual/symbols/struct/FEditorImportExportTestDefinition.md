# FEditorImportExportTestDefinition

- Symbol Type: struct
- Symbol Path: FEditorImportExportTestDefinition
- Source JSON Path: cppstruct/detail/FEditorImportExportTestDefinition.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FEditorImportExportTestDefinition.json
- Mirrored At (UTC): 2026-05-19 08:24:39Z

---

## Description

Holds settings for the asset import  export automation test

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ImportFilePath | FFilePath | The file to import <br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |  |
| ExportFileExtension | FString | The file extension to use when exporting |  |
| bSkipExport | bool | If true, the export step will be skipped |  |
| FactorySettings | TArray < FImportFactorySettingValues > | Settings for the import factory |  |

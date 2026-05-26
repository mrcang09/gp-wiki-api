# UExporter

- Symbol Type: class
- Symbol Path: Others / UExporter
- Source JSON Path: class/detail/Others/UExporter.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UExporter.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SupportedClass | TSubclassOf < UObject > | Supported class of this exporter |  |
| ExportRootScope | UObject * | The root scope of objects to be exported, only used if PPF_ExportsNotFullyQualfied is set<br>	  Objects being exported that are contained within ExportRootScope will use just their name instead of a full path |  |
| FormatExtension | TArray < FString > | The root scope of objects to be exported, only used if PPF_ExportsNotFullyQualfied is set<br>	  Objects being exported that are contained within ExportRootScope will use just their name instead of a full path<br>	 <br>	 File extension to use for this exporter |  |
| FormatDescription | TArray < FString > | Descriptiong of the export format |  |
| PreferredFormatIndex | int32 | Index into FormatExtensionFormatDescription of the preferred export format. |  |
| TextIndent | int32 | Current indentation of spaces of the exported text |  |
| bText | uint32 | If true, this will export the data as text |  |
| bSelectedOnly | uint32 | If true, this will export only the selected objects |  |
| bForceFileOperations | uint32 | If true, this will force the exporter code to create a file-based Ar (this can keep large output files from taking too much memory) |  |

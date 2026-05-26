# UDataTableFunctionLibrary

- Symbol Type: class
- Symbol Path: Others / UDataTableFunctionLibrary
- Source JSON Path: class/detail/Others/UDataTableFunctionLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UDataTableFunctionLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:26Z

---

## Functions

### EvaluateCurveTableRow

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CurveTable | UCurveTable *  |  |  |
| RowName | FName  |  |  |
| InXY | float  |  |  |
| OutResult | TEnumAsByte < EEvaluateCurveTableResult :: Type > &  |  |  |
| OutXY | float &  |  |  |
| ContextString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDataTableRowNames

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Table | UDataTable *  |  |  |
| OutRowNames | TArray < FName > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetDataTableRowFromName

Get a Row from a DataTable given a RowName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Table | UDataTable *  |  |  |
| RowName | FName  |  |  |
| OutRow | FTableRowBase & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FillDataTableFromCSVString

Empty and fill a Data Table from CSV string.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DataTable | UDataTable *  |  |  |
| CSVString | FString & | The Data that representing the contents of a CSV file. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the operation succeeds, check the log for errors if it didn't succeed. |  |

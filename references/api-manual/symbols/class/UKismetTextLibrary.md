# UKismetTextLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetTextLibrary
- Source JSON Path: class/detail/Others/UKismetTextLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetTextLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Functions

### Conv_VectorToText

Converts a vector value to localized formatted text, in the form 'X= Y= Z='

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_Vector2dToText

Converts a vector2d value to localized formatted text, in the form 'X= Y='

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_RotatorToText

Converts a rotator value to localized formatted text, in the form 'P= Y= R='

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_TransformToText

Converts a transform value to localized formatted text, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTrans | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_ObjectToText

Converts a UObject value to culture invariant text by calling the object's GetName method

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InObj | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_ColorToText

Converts a linear color value to localized formatted text, in the form '(R=,G=,B=,A=)'

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_TextToString

Converts localizable text to the string

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### Conv_StringToText

Converts string to culture invariant text. Use Format or Make Literal Text to create localizable text

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_NameToText

Converts Name to culture invariant text

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextIsEmpty

Returns true if text is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TextIsTransient

Returns true if text is transient.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TextIsCultureInvariant

Returns true if text is culture invariant.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TextToLower

Transforms the text to lowercase in a culture correct way.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextToUpper

Transforms the text to uppercase in a culture correct way.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextTrimPreceding

Removes whitespace characters from the front of the text.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextTrimTrailing

Removes trailing whitespace characters.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextTrimPrecedingAndTrailing

Removes whitespace characters from the front and end of the text.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### GetEmptyText

Returns an empty piece of text.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText |  |  |

### FindTextInLocalizationTable

Attempts to find existing Text using the representation found in the loc tables for the specified namespace and key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Namespace | FString &  |  |  |
| Key | FString &  |  |  |
| OutText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_TextText

Returns true if A and B are linguistically equal (A == B).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FText &  |  |  |
| B | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_IgnoreCase_TextText

Returns true if A and B are linguistically equal (A == B), ignoring case.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FText &  |  |  |
| B | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_TextText

Returns true if A and B are linguistically not equal (A != B).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FText &  |  |  |
| B | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_IgnoreCase_TextText

Returns true if A and B are linguistically not equal (A != B), ignoring case.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FText &  |  |  |
| B | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_BoolToText

Converts a boolean value to formatted text, either 'true' or 'false'

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBool | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_ByteToText

Converts a byte value to formatted text

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_IntToText

Converts a passed in integer to text based on formatting options

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32  |  |  |
| bUseGrouping | bool  |  |  |
| MinimumIntegralDigits | int32  |  |  |
| MaximumIntegralDigits | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Conv_FloatToText

Converts a passed in float to text based on formatting options

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| RoundingMode | TEnumAsByte < ERoundingMode >  |  |  |
| bUseGrouping | bool  |  |  |
| MinimumIntegralDigits | int32  |  |  |
| MaximumIntegralDigits | int32  |  |  |
| MinimumFractionalDigits | int32  |  |  |
| MaximumFractionalDigits | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsCurrencyBase

Generate an FText that represents the passed number as currency in the current culture.
	  BaseVal is specified in the smallest fractional value of the currency and will be converted for formatting according to the selected culture.
	  Keep in mind the CurrencyCode is completely independent of the culture it's displayed in (and they do not imply one another).
	  For example: FText::AsCurrencyBase(650, TEXT("EUR")); would return an FText of "<EUR>6.50" in most English cultures (en_USen_UK) and "6,50<EUR>" in Spanish (es_ES) (where <EUR> is U+20AC)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BaseValue | int32  |  |  |
| CurrencyCode | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsCurrency_Integer

Converts a passed in integer to a text formatted as a currency

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32  |  |  |
| RoundingMode | TEnumAsByte < ERoundingMode >  |  |  |
| bUseGrouping | bool  |  |  |
| MinimumIntegralDigits | int32  |  |  |
| MaximumIntegralDigits | int32  |  |  |
| MinimumFractionalDigits | int32  |  |  |
| MaximumFractionalDigits | int32  |  |  |
| CurrencyCode | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsCurrency_Float

Converts a passed in float to a text formatted as a currency

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| RoundingMode | TEnumAsByte < ERoundingMode >  |  |  |
| bUseGrouping | bool  |  |  |
| MinimumIntegralDigits | int32  |  |  |
| MaximumIntegralDigits | int32  |  |  |
| MinimumFractionalDigits | int32  |  |  |
| MaximumFractionalDigits | int32  |  |  |
| CurrencyCode | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsPercent_Float

Converts a passed in float to a text, formatted as a percent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| RoundingMode | TEnumAsByte < ERoundingMode >  |  |  |
| bUseGrouping | bool  |  |  |
| MinimumIntegralDigits | int32  |  |  |
| MaximumIntegralDigits | int32  |  |  |
| MinimumFractionalDigits | int32  |  |  |
| MaximumFractionalDigits | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsDate_DateTime

Converts a passed in date & time to a text, formatted as a date using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDateTime | FDateTime & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsTimeZoneDate_DateTime

Converts a passed in date & time to a text, formatted as a date using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDateTime | FDateTime &  |  |  |
| InTimeZone | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsDateTime_DateTime

Converts a passed in date & time to a text, formatted as a date & time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| In | FDateTime & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsTimeZoneDateTime_DateTime

Converts a passed in date & time to a text, formatted as a date & time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDateTime | FDateTime &  |  |  |
| InTimeZone | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsTime_DateTime

Converts a passed in date & time to a text, formatted as a time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| In | FDateTime & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsTimeZoneTime_DateTime

Converts a passed in date & time to a text, formatted as a time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDateTime | FDateTime &  |  |  |
| InTimeZone | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### AsTimespan_Timespan

Converts a passed in time span to a text, formatted as a time span

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTimespan | FTimespan & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### Format

Used for formatting text using the FText::Format function and utilized by the UK2Node_FormatText

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPattern | FText  |  |  |
| InArgs | TArray < FFormatArgumentData > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  |  |  |

### TextIsFromStringTable

Returns true if the given text is referencing a string table.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Text | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TextFromStringTable

Attempts to create a text instance from a string table ID and key.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TableId | FName  |  |  |
| Key | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FText  | The found text, or a dummy text if the entry could not be found. |  |

### StringTableIdAndKeyFromText

Attempts to find the String Table ID and key used by the given text.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Text | FText  |  |  |
| OutTableId | FName &  |  |  |
| OutKey | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the String Table ID and key were found, false otherwise. |  |

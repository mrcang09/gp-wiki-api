# FCompositeSection

- Symbol Type: struct
- Symbol Path: FCompositeSection
- Source JSON Path: cppstruct/detail/FCompositeSection.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCompositeSection.json
- Mirrored At (UTC): 2026-05-19 08:24:38Z

---

## Description

Section data for each track. Reference of data will be stored in the child class for the way they want
  AnimComposite vs AnimMontage have different requirement for the actual data reference
  This only contains composite section information. (vertical sequences)

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SectionName | FName | Section Name |  |
| StartTime_DEPRECATED | float | Start Time |  |
| NextSectionName | FName | Should this animation loop. |  |
| MetaData | TArray < UAnimMetaData * > | Meta data that can be saved with the asset<br>	 <br>	  You can query by GetMetaData function |  |

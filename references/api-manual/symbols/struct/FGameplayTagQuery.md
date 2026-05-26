# FGameplayTagQuery

- Symbol Type: struct
- Symbol Path: FGameplayTagQuery
- Source JSON Path: cppstruct/detail/FGameplayTagQuery.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagQuery.json
- Mirrored At (UTC): 2026-05-19 08:24:40Z

---

## Description

Queries are internally represented as a byte stream that is memory-efficient and can be evaluated quickly at runtime.
  Note: these have an extensive details and graph pin customization for editing, so there is no need to expose the internals to Blueprints.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TokenStreamVersion | int32 | Versioning for future token stream protocol changes. See EGameplayTagQueryStreamVersion. |  |
| TagDictionary | TArray < FGameplayTag > | List of tags referenced by this entire query. Token stream stored indices into this list. |  |
| QueryTokenStream | TArray < uint8 > | Stream representation of the actual hierarchical query |  |
| UserDescription | FString | User-provided string describing the query |  |
| AutoDescription | FString | Auto-generated string describing the query |  |

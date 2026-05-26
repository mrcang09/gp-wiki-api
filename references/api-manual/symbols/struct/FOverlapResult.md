# FOverlapResult

- Symbol Type: struct
- Symbol Path: FOverlapResult
- Source JSON Path: cppstruct/detail/FOverlapResult.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FOverlapResult.json
- Mirrored At (UTC): 2026-05-19 08:24:45Z

---

## Description

Structure containing information about one hit of an overlap test

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Actor | TWeakObjectPtr < AActor > | Actor that the check hit. |  |
| Component | TWeakObjectPtr < UPrimitiveComponent > | PrimitiveComponent that the check hit. |  |
| bBlockingHit | uint32 | Indicates if this hit was requesting a block - if false, was requesting a touch instead |  |

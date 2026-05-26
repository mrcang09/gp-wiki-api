# FMovieSceneSequenceHierarchy

- Symbol Type: struct
- Symbol Path: FMovieSceneSequenceHierarchy
- Source JSON Path: cppstruct/detail/FMovieSceneSequenceHierarchy.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceHierarchy.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Description

Structure that stores hierarchical information pertaining to all sequences contained within a master sequence

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SubSequences | TMap < uint32 , FMovieSceneSubSequenceData > | Map of all (recursive) sub sequences found in this template, keyed on sequence ID |  |
| Hierarchy | TMap < uint32 , FMovieSceneSequenceHierarchyNode > | Structural information describing the structure of the sequence |  |

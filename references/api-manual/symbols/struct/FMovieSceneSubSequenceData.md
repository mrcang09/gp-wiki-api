# FMovieSceneSubSequenceData

- Symbol Type: struct
- Symbol Path: FMovieSceneSubSequenceData
- Source JSON Path: cppstruct/detail/FMovieSceneSubSequenceData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSubSequenceData.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Sub sequence data that is stored within an evaluation template as a backreference to the originating sequence, and section

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Sequence | UMovieSceneSequence * | The sequence that the sub section references |  |
| SequenceKeyObject | UObject * | The key object that the sub section uses. Usually either the sequence or the section. |  |
| RootToSequenceTransform | FMovieSceneSequenceTransform | Transform that transforms a given time from the sequences outer space, to its authored space. |  |
| SourceSequenceSignature | FGuid | Cached signature of the evaluation template |  |
| DeterministicSequenceID | FMovieSceneSequenceID | This sequence's deterministic sequence ID. Used in editor to reduce the risk of collisions on recompilation |  |
| PreRollRange | FFloatRange | The sequence preroll range considering the start offset |  |
| PostRollRange | FFloatRange | The sequence postroll range considering the start offset |  |
| HierarchicalBias | int32 | The accumulated hierarchical bias of this sequence. Higher bias will take precedence |  |

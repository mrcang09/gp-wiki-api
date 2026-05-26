# FAnimNode_RandomPlayer

- Symbol Type: struct
- Symbol Path: FAnimNode_RandomPlayer
- Source JSON Path: cppstruct/detail/FAnimNode_RandomPlayer.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RandomPlayer.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bShuffleMode | bool | When shuffle mode is active we will never loop a sequence beyond MaxLoopCount<br>	   without visiting each sequence in turn (no repeats). Enabling this will ignore<br>	   ChanceToPlay for each entry |  |
| Entries | TArray < FRandomPlayerSequenceEntry > | List of sequences to randomly step through |  |

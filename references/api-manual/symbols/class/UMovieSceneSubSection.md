# UMovieSceneSubSection

- Symbol Type: class
- Symbol Path: Others / UMovieSceneSubSection
- Source JSON Path: class/detail/Others/UMovieSceneSubSection.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubSection.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Implements a section in sub-sequence tracks.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Parameters | FMovieSceneSectionParameters |  |  |
| StartOffset_DEPRECATED | float |  |  |
| TimeScale_DEPRECATED | float |  |  |
| PrerollTime_DEPRECATED | float |  |  |
| SubSequence | UMovieSceneSequence * | Movie scene being played by this section.<br>	 <br>	  @todo Sequencer: Should this be lazy loaded? |  |
| ActorToRecord | TLazyObjectPtr < AActor > | Target actor to record |  |
| TargetSequenceName | FString | Target name of sequence to try to record to (will record automatically to another if this already exists) |  |
| TargetPathToRecordTo | FDirectoryPath | Target path of sequence to record to |  |

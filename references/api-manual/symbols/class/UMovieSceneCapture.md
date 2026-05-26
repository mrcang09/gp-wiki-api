# UMovieSceneCapture

- Symbol Type: class
- Symbol Path: Others / UMovieSceneCapture
- Source JSON Path: class/detail/Others/UMovieSceneCapture.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCapture.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

Class responsible for capturing scene data

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CaptureType | FCaptureProtocolID | The type of capture protocol to use |  |
| ProtocolSettings | UMovieSceneCaptureProtocolSettings * | Settings specific to the capture protocol |  |
| Settings | FMovieSceneCaptureSettings | Settings that define how to capture |  |
| bUseSeparateProcess | bool | Whether to capture the movie in a separate process or not |  |
| bCloseEditorWhenCaptureStarts | bool | When enabled, the editor will shutdown when the capture starts |  |
| AdditionalCommandLineArguments | FString | Additional command line arguments to pass to the external process when capturing |  |
| InheritedCommandLineArguments | FString | Command line arguments inherited from this process |  |

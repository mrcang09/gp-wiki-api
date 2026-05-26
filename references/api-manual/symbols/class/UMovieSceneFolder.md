# UMovieSceneFolder

- Symbol Type: class
- Symbol Path: Others / UMovieSceneFolder
- Source JSON Path: class/detail/Others/UMovieSceneFolder.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneFolder.json
- Mirrored At (UTC): 2026-05-19 08:23:35Z

---

## Description

Reprents a folder used for organizing objects in tracks in a movie scene.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FolderName | FName | The name of this folder. |  |
| ChildFolders | TArray < UMovieSceneFolder * > | The folders contained by this folder. |  |
| ChildMasterTracks | TArray < UMovieSceneTrack * > | The master tracks contained by this folder. |  |
| ChildObjectBindingStrings | TArray < FString > | The guid strings used to serialize the guids for the object bindings contained by this folder. |  |

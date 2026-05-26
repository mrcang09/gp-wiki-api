# UMovieSceneBindingOverrides

- Symbol Type: class
- Symbol Path: Others / UMovieSceneBindingOverrides
- Source JSON Path: class/detail/Others/UMovieSceneBindingOverrides.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneBindingOverrides.json
- Mirrored At (UTC): 2026-05-19 08:23:34Z

---

## Description

A one-to-many definition of movie scene object binding IDs to overridden objects that should be bound to that binding.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BindingData | TArray < FMovieSceneBindingOverrideData > | The actual binding data |  |

## Functions

### GetBindingData

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const TArray < FMovieSceneBindingOverrideData > & |  |  |

### MakeBindingID

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBindingID | FGuid &  |  |  |
| InSequenceID | FMovieSceneSequenceID  |  |  |
| InSpace | EMovieSceneObjectBindingSpace |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FMovieSceneObjectBindingID  |  |  |

### GetGuidStr

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BindingID | FMovieSceneObjectBindingID & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

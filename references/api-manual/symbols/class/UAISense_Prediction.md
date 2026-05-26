# UAISense_Prediction

- Symbol Type: class
- Symbol Path: Others / UAISense_Prediction
- Source JSON Path: class/detail/Others/UAISense_Prediction.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Prediction.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RegisteredEvents | TArray < FAIPredictionEvent > |  |  |

## Functions

### RequestControllerPredictionEvent

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Requestor | AAIController *  |  |  |
| PredictedActor | AActor *  |  |  |
| PredictionTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RequestPawnPredictionEvent

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Requestor | APawn *  |  |  |
| PredictedActor | AActor *  |  |  |
| PredictionTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

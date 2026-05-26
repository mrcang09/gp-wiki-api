# FAIStimulus

- Symbol Type: struct
- Symbol Path: FAIStimulus
- Source JSON Path: cppstruct/detail/FAIStimulus.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAIStimulus.json
- Mirrored At (UTC): 2026-05-19 08:24:33Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Age | float |  |  |
| ExpirationAge | float |  |  |
| Strength | float |  |  |
| StimulusLocation | FVector |  |  |
| ReceiverLocation | FVector |  |  |
| Tag | FName |  |  |
| bSuccessfullySensed | uint32 |  |  |
| bExpired | uint32 | this means the stimulus was originally created with a "time limit" and this time has passed. <br>	 	Expiration also results in calling MarkNoLongerSensed |  |

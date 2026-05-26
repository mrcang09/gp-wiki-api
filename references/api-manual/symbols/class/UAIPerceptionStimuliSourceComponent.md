# UAIPerceptionStimuliSourceComponent

- Symbol Type: class
- Symbol Path: Others / UAIPerceptionStimuliSourceComponent
- Source JSON Path: class/detail/Others/UAIPerceptionStimuliSourceComponent.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionStimuliSourceComponent.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

Gives owning actor a way to auto-register as perception system's sense stimuli source

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bAutoRegisterAsSource | uint32 |  |  |
| RegisterAsSourceForSenses | TArray < TSubclassOf < UAISense > > |  |  |

## Functions

### RegisterWithPerceptionSystem

Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses. 
	 	Note that you don't have to do it if bAutoRegisterAsSource == true

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RegisterForSense

Registers owning actor as source for specified sense class

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseClass | TSubclassOf < UAISense > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnregisterFromPerceptionSystem

Unregister owning actor from being a source of sense stimuli

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UnregisterFromSense

Unregisters owning actor from sources list of a specified sense class

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SenseClass | TSubclassOf < UAISense > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

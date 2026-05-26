# UBTDecorator_IsAtLocation

- Symbol Type: class
- Symbol Path: Others / UBTDecorator_IsAtLocation
- Source JSON Path: class/detail/Others/UBTDecorator_IsAtLocation.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_IsAtLocation.json
- Mirrored At (UTC): 2026-05-19 08:23:23Z

---

## Description

Is At Location decorator node.
  A decorator node that checks if AI controlled pawn is at given location.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AcceptableRadius | float | distance threshold to accept as being at location |  |
| ParametrizedAcceptableRadius | FAIDataProviderFloatValue |  |  |
| GeometricDistanceType | FAIDistanceType |  |  |
| bUseParametrizedRadius | uint32 |  |  |
| bUseNavAgentGoalLocation | uint32 | if moving to an actor and this actor is a nav agent, then we will move to their nav agent location |  |
| bPathFindingBasedTest | uint32 | If true the result will be consistent with tests done while following paths.<br>	 	Set to false to use geometric distance as configured with DistanceType |  |

# FNavAgentProperties

- Symbol Type: struct
- Symbol Path: FNavAgentProperties
- Source JSON Path: cppstruct/detail/FNavAgentProperties.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FNavAgentProperties.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

Properties of representation of an 'agent' (or Pawn) used by AI navigationpathfinding.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AgentRadius | float | Radius of the capsule used for navigationpathfinding. |  |
| AgentHeight | float | Total height of the capsule used for navigationpathfinding. |  |
| AgentStepHeight | float | Step height to use, or -1 for default value from navdata's config. |  |
| NavWalkingSearchHeightScale | float | Scale factor to apply to height of bounds when searching for navmesh to project to when nav walking |  |
| PreferredNavData | TSubclassOf < ANavigationData > | Type of navigation data used by agent, null means "any" |  |
| AgentType | int32 |  |  |

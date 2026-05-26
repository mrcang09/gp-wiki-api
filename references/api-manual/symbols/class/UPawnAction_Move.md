# UPawnAction_Move

- Symbol Type: class
- Symbol Path: Others / UPawnAction_Move
- Source JSON Path: class/detail/Others/UPawnAction_Move.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_Move.json
- Mirrored At (UTC): 2026-05-19 08:23:38Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GoalActor | AActor * |  |  |
| GoalLocation | FVector |  |  |
| AcceptableRadius | float |  |  |
| FilterClass | TSubclassOf < UNavigationQueryFilter > | "None" will result in default filter being used |  |
| bAllowStrafe | uint32 |  |  |
| bFinishOnOverlap | uint32 | if set to true (default) will make action succeed when the pawn's collision component overlaps with goal's collision component |  |
| bUsePathfinding | uint32 | if set, movement will use path finding |  |
| bAllowPartialPath | uint32 | if set, use incomplete path when goal can't be reached |  |
| bProjectGoalToNavigation | uint32 | if set, GoalLocation will be projected on navigation before using |  |
| bUpdatePathToGoal | uint32 | if set, path to GoalActor will be updated with goal's movement |  |
| bAbortChildActionOnPathChange | uint32 | if set, other actions with the same priority will be aborted when path is changed |  |

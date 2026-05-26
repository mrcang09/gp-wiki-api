# UGCCampSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 社交系统 / UGCCampSystem
- Source JSON Path: class/detail/和平全局接口/社交系统/UGCCampSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCCampSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

阵营接口库

## Functions

### AddCamp

增加阵营
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampName | string | 阵营名称 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 通过CampName创建的阵营ID，CampName与CampID都是阵营唯一标识符 |  |

### SetCampForActor

设置非玩家Actor所属阵营，例如设置怪物的阵营
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | AActor |  |
| InCampID | number | 阵营ID |  |

### SetCampForTeam

设置队伍所属阵营
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTeamID | number | 队伍ID |  |
| InCampID | number | 阵营ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 设置队伍所属阵营是否成功 |  |

### GetCampIDByActor

通过非玩家Actor获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | AActor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 阵营ID |  |

### GetCampNameByActor

通过非玩家Actor获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | AActor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 阵营名称 |  |

### GetCampIDByTeamID

通过队伍ID获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTeamID | number | 队伍ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number | 阵营ID |  |

### GetCampNameByTeamID

通过队伍ID获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTeamID | number | 队伍ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | 阵营名称 |  |

### SetDefaultCampRelation

设置默认阵营关系
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampRelation | ECampRelation | 阵营关系,1:友好,2:中立,3:敌对 |  |

### SetCampRelation

设置两个阵营之间的阵营关系
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampA_ID | number | 阵营A ID |  |
| InCampB_ID | number | 阵营B ID |  |
| InCampRelation | ECampRelation | 阵营关系,0:友好,1:中立,2:敌对 |  |

### GetCampRelation

获取两个阵营之间的阵营关系，获取失败默认返回中立
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampA_ID | number | 阵营A ID |  |
| InCampB_ID | number | 阵营B ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECampRelation | 阵营关系,1:友好,2:中立,3:敌对 |  |

### GetCampRelationWithActor

获取两个Actor之间的阵营关系，获取失败默认返回中立
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActorA | AActor | AActor |  |
| InActorB | AActor | AActor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ECampRelation | 阵营关系,1:友好,2:中立,3:敌对 |  |

### SetCampDefaultSpawnMethod

设置阵营出生方式
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCampID | number | 阵营ID |  |
| SpawnPointSelectionMethod | EUGCCampSpawnPointSelectionMethod | 阵营出生方式 |  |
| SpawnMethodInfo | FVector|uint8 | 指定PlayerStartID或者世界坐标 |  |
| PlayerStartInfo | boolean | 是否随机出生点ID |  |

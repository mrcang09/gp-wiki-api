# AUGCMobCharacter

- Symbol Type: class
- Symbol Path: Others / AUGCMobCharacter
- Source JSON Path: class/detail/Others/AUGCMobCharacter.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/AUGCMobCharacter.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

怪物角色类

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Health | float | 当前生命值 |  |
| HealthAddScale | float | 加血速率 |  |
| HealthMax | float | 最大生命值 |  |
| bInvincible | int | 是否无敌 |  |
| SkillCDRecoverRate | FGameAttributeProperty | 技能急速，值越大技能冷却越快结束 |  |
| IsShowDamageNum | bool | 是否显示伤害数字 |  |
| HealthBarWidget | UUGCCharacterPositionWidget * | 血条的蓝图类 |  |
| bIsShowHealthBar | bool | 是否显示血条 |  |
| ShowName | FName | 血条上显示的名字 |  |
| PlayBeHitedAnimTimeInterval | float | 受击动画播放最小间隔，小于受击动画长度时无效 |  |
| bNeedDestroyOnDeath | bool | 是否启用尸体消失后延迟销毁 |  |
| DisappearOnDeathLifeSpan | float | 尸体消失后延迟多久销毁 |  |
| DelayRemoveDeadBody | float | 死亡后尸体存在时间 |  |
| BornTime | float | 出生状态持续时间 |  |
| StunDuration | float | 硬直状态持续时间 |  |
| UGCGeneralMoveSpeedScale | float | 移动速度倍率 |  |
| AttackMeActorRemainTime | float | 活动范围，处于活动范围外时索敌无效，仇恨随时间消失<br>	 <br>	 UGC<br>	  处于活动范围外时仇恨持续时间 |  |
| SpawnLoc | FVector | 出生地点 |  |
| bOutOfActivityRange | bool | 是否在活动范围外 |  |

## Functions

### IsAlive

是否存活

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsInvincible

是否无敌

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FORCEINLINE int |  |  |

### ForceDie

生效范围 服务器
	  强制杀死怪物

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCurrentSpeed

生效范围 服务器&客户端
	  获取当前速度值

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float | float 当前速度值 |  |

### GetVelocity

生效范围 服务器&客户端
	  获取当前速度向量

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector | FVector 当前速度向量 |  |

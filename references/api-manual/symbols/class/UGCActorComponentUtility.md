# UGCActorComponentUtility

- Symbol Type: class
- Symbol Path: 和平全局接口 / 基础功能 / UGCActorComponentUtility
- Source JSON Path: class/detail/和平全局接口/基础功能/UGCActorComponentUtility.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCActorComponentUtility.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

Actor接口库

## Functions

### SpawnActor

在游戏世界中生成指定类型的 Actor
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject | 世界上下文对象 |  |
| ActorClass | UClass | 要生成的 Actor 类型，需通过 UGCObjectUtility.LoadClass 加载类引用 |  |
| Location | Vector | 生成位置坐标，推荐使用 {X=1,Y=1,Z=1} 构造 |  |
| Rotation | Rotator | 生成旋转角度，推荐使用 {X=0,Y=0,Z=0} 构造 |  |
| Scale3D | Vector | 可生成缩放比例，推荐使用 {X=1,Y=1,Z=1} 构造，默认值: Vector(0,0,0)，建议使用Vector(1,1,1)保持原始比例 |  |
| Owner | Actor | 新生成 Actor 的所属对象 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | Actor | 新生成的 Actor 实例 |  |

### DestroyActor

销毁Actor
生效范围：服务器&客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

### ToString

获取Actor的ToString
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | string | ToString |  |

### GetOwner

获取Actor的Owner
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor | Owner |  |

### SetOwner

设置Actor的Owner
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InOwner | AActor | Owner |  |

### GetUltimateOwnerActor

获取技能，武器，Buff等持有者acotr
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor | Owner |  |

### GetUltimateController

获取技能，武器，Buff等持有者的Controller
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor | Owner |  |

### AttachToActor

附着到Actor上
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InAttachTo | AActor | 需要附着到的Actor |  |
| LocationRule | EAttachmentRule | 附着位置规则 |  |
| RotationRule | EAttachmentRule | 附着旋转规则 |  |
| ScaleRule | EAttachmentRule | 附着缩放规则 |  |
| InSocketName | string | 需要附着到的SocketName |  |

### AttachToComponent

附着到Component上
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InAttachTo | USceneComponent | 需要附着到的Actor |  |
| LocationRule | EAttachmentRule | 附着位置规则 |  |
| RotationRule | EAttachmentRule | 附着旋转规则 |  |
| ScaleRule | EAttachmentRule | 附着缩放规则 |  |
| InSocketName | string | 需要附着到的SocketName |  |
| bWeldSimulatedBodies | boolean | 是否保持相对位置不变/是否焊接为模拟刚体 |  |

### DetachFromParent

将Component从父Actor上拆离
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InComponent | USceneComponent | Actor |  |
| bMaintainWorldPosition | boolean | 是否保持位置不变 |  |
| bCallModify | boolean | 是否调用Modify |  |

### GetRootComponent

获取根组件
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | USceneComponent | 根组件 |  |

### GetComponentsByOwner

获取Actor上的所有Component
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent[] | Actor上的所有Component |  |

### GetComponentsByClass

获取Actor上指定类的Component
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InComonentClass | UClass | 指定Component的Class |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent[] | Actor上特定类型的Components |  |

### GetComponentsByTag

获取Actor上指定Tag的Component
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InComonentClass | UClass | ComponentClass |  |
| Tag | string | Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UActorComponent[] | Components |  |

### GetAllActorsOfClass

获取指定Class在场景里的所有Actor
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject | WorldContextObject |  |
| ActorClass | UClass | ActorClass |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor[] | Actor列表 |  |

### GetAllActorsWithTag

获取指定Tag在场景里的所有Actor
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject | WorldContextObject |  |
| Tag | string | Tag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor[] | Actor列表 |  |

### GetActorTransform

获取Actor的Transform
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform | Transform | cppstruct/detail/FTransform.json |

### GetSceneComponentWorldTransform

获取场景组件的世界Transform
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InSceneComponent | USceneComponent | 场景组件 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform | Transform | cppstruct/detail/FTransform.json |

### SetActorTransform

设置Actor的Transform
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InTransform | FTransform | Transform | cppstruct/detail/FTransform.json |

### HasAuthority

判断是否为权威端
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean | 当前端是否为权威端 |  |

### CreateAndRegisterComponent

创建并注册组件
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InComponentClass | UClass | 要创建组件对应的Class |  |
| InOuter | UObject | Outer |  |
| InComponentName | string | 要创建组件对应的Class对应的ObjectName |  |

### DestroyComponent

销毁组件
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InActor | AActor | Actor |  |
| InComponent | UActorComponent | 要销毁的组件 |  |

### GetOverlappingActorsWithPrimitiveComponent

获取与PrimitiveComponent重叠的Actor
生效范围：客户端&服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPrimitiveComponent | UPrimitiveComponent | 组件 |  |
| Transform | FTransform | 组件的Transform | cppstruct/detail/FTransform.json |
| ObjectTypes | ESceneQueryType[] | 对象类型列表 |  |
| ActorClassFilter | UClass | 要检测的Actor类型（默认值：nil为全部类型的Actor） |  |
| ActorsToIgnore | AActor[] | 需要忽略的Actor列表 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor[] | 与目标Actor重叠的Actor列表 |  |

### GetActorByActorInstancePath

在运行时通过Actor实例路径获取Actor，对关卡编辑器实例列表里任意Actor右键，选择GetActorInstancePath即可获取路径
生效范围：客户端&服务器
路径格式：PackageName.ObjectPath，例如：UGCmap.test_8

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstancePath | string | 实例路径 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | AActor | Actor实例 |  |

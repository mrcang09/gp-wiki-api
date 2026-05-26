# UGCEMPZoneSystem

- Symbol Type: class
- Symbol Path: Others / UGCEMPZoneSystem
- Source JSON Path: class/detail/Others/UGCEMPZoneSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:28Z

---

## Description

电磁干扰区接口库

## Functions

### GenerateElectromagneticArea

生成电磁干扰区
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConfigID | number | 电磁干扰区配置 ID |  |
| Location | FVector | 电磁干扰区中心坐标 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bool, | number | 是否成功生成电磁干扰区, 实例ID |  |

### DestroyElectromagneticArea

取消电磁干扰区
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number | 电磁干扰区实例 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否成功取消电磁干扰区 |  |

### ModifyConfigElectromagneticArea

修改电磁干扰区参数
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConfigID | number | 电磁干扰区配置 ID |  |
| ParameterType | string | 参数类型 |  |
| NewValue | number | 新的参数值 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | 是否成功修改电磁干扰区配置 |  |

### GetAllConfigElectromagneticArea

查看当前全部电磁干扰区
生效范围：服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| table<number, | UGCEMPZoneConfig> | 所有电磁干扰区实例ID和对应的电磁干扰区参数 |  |

### GetSpecifyElectromagneticAreaList

查看指定电磁干扰区参数
生效范围：服务器

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InstanceID | number | 电磁干扰区实例 ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCEMPZoneConfig | 指定实例的电磁干扰区参数 |  |

### GetEMPZoneManager

获取电磁干扰区管理器
获取电磁干扰区全局管理器实例，用于绑定电磁干扰区相关事件
生效范围：服务器&客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UGCEMPZoneManager | 电磁干扰区管理器实例，失败时返回nil |  |

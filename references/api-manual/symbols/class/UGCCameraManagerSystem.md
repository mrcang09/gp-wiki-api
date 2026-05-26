# UGCCameraManagerSystem

- Symbol Type: class
- Symbol Path: 和平全局接口 / 角色系统 / UGCCameraManagerSystem
- Source JSON Path: class/detail/和平全局接口/角色系统/UGCCameraManagerSystem.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCCameraManagerSystem.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

相机管理器系统接口库

## Functions

### GetInVehicleFPPViewPitchLimitMin

获得第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| number | @Pitch | 视角限制（最小值） |  |

### SetInVehicleFPPViewPitchLimitMin

设置第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PitchLimit | number | Pitch 视角限制（最小值） |  |

### GetInVehicleFPPViewYawLimit

获得第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| number | @Yaw | 视角限制 |  |

### SetInVehicleFPPViewYawLimit

设置第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| YawLimit | number | Yaw 视角限制 |  |

### GetInVehicleNarrowSeatGrenadesYawLimit

获得在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| number | @Yaw | 视角限制 |  |

### SetInVehicleNarrowSeatGrenadesYawLimit

设置在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| YawLimit | number | Yaw 视角限制 |  |

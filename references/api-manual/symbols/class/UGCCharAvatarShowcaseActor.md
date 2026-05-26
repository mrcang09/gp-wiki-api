# UGCCharAvatarShowcaseActor

- Symbol Type: class
- Symbol Path: Others / UGCCharAvatarShowcaseActor
- Source JSON Path: class/detail/Others/UGCCharAvatarShowcaseActor.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGCCharAvatarShowcaseActor.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

复制玩家角色Avatar的Actor

## Functions

### ClientShowAvatar

显示PlayerUID的Avatar
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerUID | number | 玩家的 PlayerUID |  |

### ServerShowAvatar

显示PlayerUID的Avatar
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerUID | number | 玩家的 PlayerUID |  |

### PlayAnim

播放动画
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewAnimToPlay | UAnimationAsset | 动画资源 |  |
| bLooping | boolean | 是否循环播放 |  |

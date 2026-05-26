# ASTExtraBaseCharacter

- Symbol Type: class
- Symbol Path: 和平类事件 / 主角类（PlayerPawn） / ASTExtraBaseCharacter
- Source JSON Path: class/detail/和平类事件/主角类（PlayerPawn）/ASTExtraBaseCharacter.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E4%B8%BB%E8%A7%92%E7%B1%BB%EF%BC%88PlayerPawn%EF%BC%89/ASTExtraBaseCharacter.json
- Mirrored At (UTC): 2026-05-19 08:23:21Z

---

## Description

主角类（PlayerPawn）

## Functions

### DSTeleportToLocationOrRotation

生效范围：服务器
	  传送主角，只有服务器上调用生效，客户端调用无效

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| location | FVector  | 位置 | cppstruct/detail/FVector.json |
| rotation | FRotator  | 旋转 | cppstruct/detail/FRotator.json |
| setLoc | bool  | 是否修改位置 |  |
| setRot | bool  | 是否修改旋转 |  |
| ResetVelocity | bool  | 是否重置速度 |  |
| bRecordTeleportInfo | bool | 是否记录传送时间用于射击校验，如无特殊需求保持默认配置 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

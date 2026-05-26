# FAnimNode_EmoteSwitchAdapt

- Symbol Type: struct
- Symbol Path: FAnimNode_EmoteSwitchAdapt
- Source JSON Path: cppstruct/detail/FAnimNode_EmoteSwitchAdapt.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_EmoteSwitchAdapt.json
- Mirrored At (UTC): 2026-05-19 08:24:34Z

---

## Description

面部表情骨骼吸附节点
 
  功能：
  - 自动检测当前帧下哪个表情骨骼最接近RefPose位置
  - 将该骨骼吸附到RefPose位置，确保至少有一个完整表情显示
  - 用于解决Linear插值模式下表情切换时的"半表情"问题

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EmoteShowBoneRef | FBoneReference |  |  |
| EmoteAdaptBones | TArray < FEmoteBoneAdaptConfig > |  |  |

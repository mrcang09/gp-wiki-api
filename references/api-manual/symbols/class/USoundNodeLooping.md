# USoundNodeLooping

- Symbol Type: class
- Symbol Path: Others / USoundNodeLooping
- Source JSON Path: class/detail/Others/USoundNodeLooping.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeLooping.json
- Mirrored At (UTC): 2026-05-19 08:23:40Z

---

## Description

Defines how a sound loops; either indefinitely, or for a set number of times.
  Note: The Looping node should only be used for logical or procedural looping such as introducing a delay.
  These sounds will not be played seamlessly. If you want a sound to loop seamlessly and indefinitely,
  use the Looping flag on the Wave Player node for that sound.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LoopCount | int32 | The amount of times to loop |  |
| bLoopIndefinitely | uint32 | If enabled, the node will continue to loop indefinitely regardless of the Loop Count value. |  |

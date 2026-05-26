# UCameraAnimInst

- Symbol Type: class
- Symbol Path: Others / UCameraAnimInst
- Source JSON Path: class/detail/Others/UCameraAnimInst.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UCameraAnimInst.json
- Mirrored At (UTC): 2026-05-19 08:23:25Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CamAnim | UCameraAnim * | which CameraAnim this is an instance of |  |
| InterpGroupInst | UInterpGroupInst * | the UInterpGroupInst used to do the interpolation |  |
| PlayRate | float | Multiplier for playback rate.  1.0 = normal. |  |
| MoveTrack | UInterpTrackMove * | cached movement track from the currently playing anim so we don't have to go find it every frame |  |
| MoveInst | UInterpTrackInstMove * |  |  |
| PlaySpace | TEnumAsByte < ECameraAnimPlaySpace :: Type > |  |  |

## Functions

### SetCurrentTime

Jumps he camera anim to the given (unscaled) time.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewTime | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Stop

Stops this instance playing whatever animation it is playing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bImmediate | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDuration

Changes the running duration of this active anim, while maintaining playback position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDuration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetScale

Changes the scale of the animation while playing.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewDuration | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

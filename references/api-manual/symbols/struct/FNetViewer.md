# FNetViewer

- Symbol Type: struct
- Symbol Path: FNetViewer
- Source JSON Path: cppstruct/detail/FNetViewer.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FNetViewer.json
- Mirrored At (UTC): 2026-05-19 08:24:44Z

---

## Description

stores information on a viewer that actors need to be checked against for relevancy

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Connection | UNetConnection * |  |  |
| InViewer | AActor * | The "controlling net object" associated with this view (typically player controller) |  |
| ViewTarget | AActor * | The actor that is being directly viewed, usually a pawn.  Could also be the net actor of consequence |  |
| ViewLocation | FVector | Where the viewer is looking from |  |
| ViewDir | FVector | Direction the viewer is looking |  |

# FSubmixEffectReverbSettings

- Symbol Type: struct
- Symbol Path: FSubmixEffectReverbSettings
- Source JSON Path: cppstruct/detail/FSubmixEffectReverbSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FSubmixEffectReverbSettings.json
- Mirrored At (UTC): 2026-05-19 08:24:48Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Density | float | Density - 0.0 < 0.85 < 1.0 - Coloration of the late reverb - lower value is more grainy |  |
| Diffusion | float | Diffusion - 0.0 < 0.85 < 1.0 - Echo density in the reverberation decay - lower is more grainy |  |
| Gain | float | Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control |  |
| GainHF | float | Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound |  |
| DecayTime | float | Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb |  |
| DecayHFRatio | float | Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much the quicker or slower the high frequencies decay relative to the lower frequencies. |  |
| ReflectionsGain | float | Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections |  |
| ReflectionsDelay | float | Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection |  |
| LateGain | float | Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb |  |
| LateDelay | float | Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections |  |
| AirAbsorptionGainHF | float | Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption |  |
| WetLevel | float |  |  |

# UGameMapsSettings

- Symbol Type: class
- Symbol Path: Others / UGameMapsSettings
- Source JSON Path: class/detail/Others/UGameMapsSettings.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UGameMapsSettings.json
- Mirrored At (UTC): 2026-05-19 08:23:29Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| EditorStartupMap | FSoftObjectPath | If set, this map will be loaded when the Editor starts up. |  |
| LocalMapOptions | FString | The default options that will be appended to a map being loaded. |  |
| TransitionMap | FSoftObjectPath | The map loaded when transition from one map to another. |  |
| bUseSplitscreen | bool | Whether the screen should be split or not when multiple local players are present |  |
| TwoPlayerSplitscreenLayout | TEnumAsByte < ETwoPlayerSplitScreenType :: Type > | The viewport layout to use if the screen should be split and there are two local players |  |
| ThreePlayerSplitscreenLayout | TEnumAsByte < EThreePlayerSplitScreenType :: Type > | The viewport layout to use if the screen should be split and there are three local players |  |
| bOffsetPlayerGamepadIds | bool | If enabled, this will make so that gamepads start being assigned to the second controller ID in local multiplayer games.<br>	 In PIE sessions with multiple windows, this has the same effect as enabling "Route 1st Gamepad to 2nd Client" |  |
| GameInstanceClass | FSoftClassPath | The class to use when instantiating the transient GameInstance class |  |
| GameDefaultMap | FSoftObjectPath | The map that will be loaded by default when no other map is loaded. |  |
| HSCDefaultMap | FSoftObjectPath |  |  |
| UGCMDefaultMap | FSoftObjectPath |  |  |
| ServerDefaultMap | FSoftObjectPath | The map that will be loaded by default when no other map is loaded (DEDICATED SERVER). |  |
| GlobalDefaultGameMode | FSoftClassPath | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL). |  |
| GlobalDefaultServerGameMode | FSoftClassPath | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL) (DEDICATED SERVERS)<br>	  If not set, the GlobalDefaultGameMode value will be used. |  |
| GameModeMapPrefixes | TArray < FGameModeName > | Overrides the GameMode to use when loading a map that starts with a specific prefix |  |
| GameModeClassAliases | TArray < FGameModeName > | List of GameModes to load when game= is specified in the URL (e.g. "DM" could be an alias for "MyProject.MyGameModeMP_DM") |  |

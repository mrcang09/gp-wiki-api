# UFontFace

- Symbol Type: class
- Symbol Path: Others / UFontFace
- Source JSON Path: class/detail/Others/UFontFace.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UFontFace.json
- Mirrored At (UTC): 2026-05-19 08:23:27Z

---

## Description

A font face asset contains the raw payload data for a source TTFOTF file as used by FreeType.
  During cook this asset type generates a ".ufont" file containing the raw payload data (unless loaded "Inline").

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SourceFilename | FString | The filename of the font face we were created from. This may not always exist on disk, as we may have previously loaded and cached the font data inside this asset. |  |
| Hinting | EFontHinting | The hinting algorithm to use with the font face. |  |
| LoadingPolicy | EFontLoadingPolicy | Enum controlling how this font face should be loaded at runtime. See the enum for more explanations of the options. |  |
| LayoutMethod | EFontLayoutMethod | Which method should we use when laying out the font? Try changing this if you notice clipping or height issues with your font. |  |
| FontFaceData_DEPRECATED | TArray < uint8 > | The data associated with the font face. This should always be filled in providing the source filename is valid. |  |
